import analytics

class SegmentClient:
    def __init__(self, write_key: str):
        analytics.write_key = write_key

    def identify(self, user_id: str, traits: dict):
        analytics.identify(user_id=user_id, traits=traits)

    def track(
        self,
        event_name: str,
        properties: dict,
        user_id: str = "",
    ):
        analytics.track(
            event=event_name,
            properties=properties,
            user_id=user_id,
        )