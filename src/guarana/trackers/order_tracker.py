import guarana
from guarana.schemas.events import OrderTrackEvents
from guarana.schemas.order import OrderCall


class OrderTracker(guarana.EventTracker):
    def __init__(self, segment_write_key: str):
        super().__init__(segment_write_key=segment_write_key)

    def track_order_placed(self, order_call: OrderCall, email: str, **kwargs):
        order_track_properties = order_call.dict(exclude_none=True, exclude_unset=True)

        self.segment_client.track(
            event_name=OrderTrackEvents.order_completed,
            user_id=order_call.user_id,
            properties={**order_track_properties, **kwargs, 'email': email}
        )

        self.segment_client.identify(
            user_id=order_call.user_id,
            traits=dict(
                email=email,
                last_order_placed=order_call.created_at
            )
        )
