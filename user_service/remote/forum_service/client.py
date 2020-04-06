from user_service.app.configuration import config

class ForumServiceClient:
    def __init__(self, url):
        self.url = url

forum_service_rest_client = ForumServiceClient(
    url=config.FORUM_SERVICE_URL
)
