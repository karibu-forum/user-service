from user_service.app.configuration import config
from user_service.remote.rest.client import RestClient

class ForumServiceClient(RestClient):
    def __init__(self, url):
        self.url = url

forum_service_rest_client = ForumServiceClient(
    url=config.FORUM_SERVICE_URL
)
