from typing import Any

import segment.analytics as analytics
from loguru import logger


class SegmentClient:
    def __init__(self, write_key: str):
        self.client = analytics
        self.client.write_key = write_key
        self.client.on_error = self.on_error
    

    def identify(self, user_id: str, traits: dict) -> Any:
        try:
            self.client.identify(user_id=user_id, traits=traits)
            return { "success": True, "msg": "Identify method called successfully" }
        except Exception as e:
            return { "success": False, "msg": e }

    def track(
        self,
        event_name: str,
        properties: dict,
        user_id: str = None,
        anonymous_id: str = None,
    ) -> Any:   

        try:
            self.client.track(
                event=event_name,
                properties=properties,
                user_id=str(user_id),
                anonymous_id=str(anonymous_id),
            )
            return { "success": True, "msg": "Event logged successfully" }
        except Exception as e:
            return { "success": False, "msg": e }

    def on_error(error, items):
        logger.error(f'Error: {error} - {items != None: items | dict() }')
