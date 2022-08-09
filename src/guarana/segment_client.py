from typing import Any
import analytics
from loguru import logger


class SegmentClient:
    def __init__(self, write_key: str):
        self.client = analytics.Client(write_key)
        self.client.on_error = self.on_error
    

    def identify(self, user_id: str, traits: dict) -> Any:
        status, msg = self.client.identify(user_id=user_id, traits=traits)
        return status, msg

    def track(
        self,
        event_name: str,
        properties: dict,
        user_id: str = None,
        anonymous_id: str = None,
    ) -> Any:   

        succes, msg = self.client.track(
            event=event_name,
            properties=properties,
            user_id=str(user_id),
            anonymous_id=str(anonymous_id),
        )
        return succes, msg

    def on_error(error, items):
        logger.error(f'Error: {error} - {items != None: items | dict() }')
