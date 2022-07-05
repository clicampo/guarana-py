__version__ = '0.1.0'
import logging
from loki_client import LokiClient
from segment_client import SegmentClient

class EventTracker:
    def __init__(self, segment_write_key: str, loki_url: str, loki_username: str, loki_password: str, queue: bool = True):
        self.segment_client = SegmentClient(segment_write_key)
        self.loki_client = LokiClient(
            loki_url=loki_url,
            loki_username=loki_username,
            loki_password=loki_password,
            queue=False
        )
        self.logger = logging.getLogger('segment')
        self.logger.addHandler(self.loki_client.handler)


    def identify_user(self, user_id: str, traits: dict):
        self.segment_client.identify(user_id=user_id, traits=traits)


    def track(self, event_name: str, properties: dict, user_id: str = None):
        self.segment_client.track(
            event_name=event_name,
            properties=properties,
            user_id=user_id
        )