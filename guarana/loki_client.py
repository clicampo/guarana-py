import logging_loki
from multiprocessing import Queue



class LokiClient:

    def __init__(self, loki_url: str, loki_username: str, loki_password: str, queue: bool):
        if queue:
            self.handler = self.set_handler_loki_queue(loki_url, loki_username, loki_password)
        else:
            self.handler = self.set_handler_loki(loki_url, loki_username, loki_password)

    def set_handler_loki(self, loki_url: str, loki_username: str, loki_password: str, app_name: str = "my-app"):
        handler = logging_loki.LokiHandler(
            url=loki_url, 
            tags={"application": app_name},
            auth=(loki_username, loki_password),
            version="1",
        )
        return handler

    def set_handler_loki_queue(self,  loki_url: str, loki_username: str, loki_password: str, app_name: str = "my-app"):
        handler = logging_loki.LokiQueueHandler(
            Queue(-1),
            url=loki_url, 
            tags={"application": app_name},
            auth=(loki_username, loki_password),
            version="1",
        )
        return handler

