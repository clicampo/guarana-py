import analytics


class SegmentClient:
    def __init__(write_key: str):
        analytics.write_key = write_key

    
    def identify(user_id: str, traits: dict):
        analytics.identify(user_id=user_id, traits=traits)


    def track(
        event_name: str,
        properties: dict,
        user_id: str = None,
    ):
        analytics.track(
            event_name=event_name,
            properties=properties,
            user_id=user_id,
        )