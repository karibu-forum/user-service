import os
from flask import Flask, jsonify, request, abort

from user_service.app import initialize, config
from user_service.api.rest import exceptions
from user_service.db.session import get_session

import logging

unauthenticated_endpoints = {'/health'}


def create_app(force=False):
    """
    Configure stuff on app startup
    """
    initialize()

    # instantiate the app
    app = Flask(__name__, instance_relative_config=True)
    app.config['TESTING'] = False

    from user_service.api.rest.user import user_api
    app.register_blueprint(user_api)

    @app.before_request
    def request_check_api_key():
        if not config.REQUIRE_API_AUTHENTICATION:
            return

        if request.path in unauthenticated_endpoints:
            return
        # TODO add api key authorization here
        abort(401)

    @app.errorhandler(exceptions.APIException)
    def handle_invalid_usage(error):
        response = jsonify(error.to_dict())
        response.status_code = error.status_code
        return response

    @app.route('/health')
    def health():
        return 'OK'

    @app.after_request
    def db_conn_cleanup(response):
        session = get_session()
        session.remove()
        return response

    return app
