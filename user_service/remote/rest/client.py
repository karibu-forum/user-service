from easydict import EasyDict
import requests

from user_service.remote import exceptions
from user_service.lib import get_logger

logger = get_logger(__name__)


class RestClient:
    def __init__(self, base_url, enabled=True):
        self.base_url = base_url.rstrip('/')
        self.session = requests.Session()
        self.enabled = enabled

    def build_url(self, url):
        full_url = '{}/{}'.format(self.base_url, url.lstrip('/'))
        return full_url

    def _get_auth_header(self):
        return {}

    def get(self, url, data=None, timeout=None, response_content_type=None):
        if not self.enabled:
            return

        full_url = self.build_url(url)
        headers = self._get_auth_header()
        response = self.session.get(full_url, params=data, headers=headers, timeout=timeout)
        return self._handle_response(response, response_content_type)

    def post(self, url, data=None, timeout=None):
        if not self.enabled:
            return

        full_url = self.build_url(url)
        headers = self._get_auth_header()
        response = self.session.post(full_url, json=data, headers=headers, timeout=timeout)
        return self._handle_response(response)

    def patch(self, url, data=None):
        if not self.enabled:
            return

        full_url = self.build_url(url)
        headers = self._get_auth_header()
        response = self.session.patch(full_url, json=data, headers=headers)
        return self._handle_response(response)

    def _handle_response(self, response, response_content_type=None):
        return response


class RestServiceClient(RestClient):
    def __init__(self, api_key, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.api_key = api_key

    def _get_auth_header(self):
        if self.api_key:
            return {'Authorization': 'Bearer {}'.format(self.api_key)}
        else:
            return {}

    def _handle_response(self, response):
        status_code = response.status_code
        if status_code in (200, 201):
            json_data = response.json()
            return EasyDict(json_data)
        if status_code == 404:
            raise exceptions.NotFoundError()
        elif 400 <= status_code < 500:
            # expecting an error object with message, code
            data = response.json()
            error_message = data.get('message', None)
            error_code = data.get('code', None)
            raise exceptions.BadRequestError(
                message=error_message,
                code=error_code,
            )
        elif status_code >= 500:
            raise exceptions.ServerError(
                message='Server error',
            )
