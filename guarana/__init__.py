__version__ = '0.1.0'
from segment_client import SegmentClient
from loguru import logger

class EventTracker:
    def __init__(self, segment_write_key: str):
        self.segment_client = SegmentClient(segment_write_key)
        logger.info(f"Initialized SegmentClient")

    def identify_user(self, user_id: str, traits: dict):
        sucess, msg = self.segment_client.identify(user_id=user_id, traits=traits)
        if sucess:
            logger.success(msg)
        else:
            logger.warning(msg)



    def track(self, event_name: str, properties: dict, user_id: str = ''):
        sucess, msg = self.segment_client.track(
            event_name=event_name,
            properties=properties,
            user_id=user_id
        )
        if sucess:
            logger.success(msg)
        else:
            logger.warning(msg)