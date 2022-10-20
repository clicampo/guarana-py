import guarana
from guarana.schemas.events import OrderTrackEvents
from guarana.schemas.order import OrderCall


class OrderTracker(guarana.EventTracker):
    def __init__(self, segment_write_key: str):
        super().__init__(segment_write_key=segment_write_key)

    def track_order_placed(self, order_call: OrderCall, email: str, **kwargs):
        order_track_properties = order_call.dict(exclude_none=True, exclude_unset=True)
        identify_payload = {"email": email}

        self.segment_client.track(
            event_name=OrderTrackEvents.order_completed,
            user_id=str(order_call.user_id),
            properties={**order_track_properties, **kwargs, "email": email},
        )

        match str(order_call.id_order_category):
            case "055ebaa9-7583-4d47-9ce8-a5d772f7a91d":
                # Sampling order
                identify_payload |= {
                    "last_sampling_order_placed_ts": order_call.created_at,
                    "last_sampling_order_placed_id": str(order_call.id_order),
                    "last_sampling_order_placed_total": order_call.total,
                }
            case "44895221-7870-4aeb-b570-4ceb251e9663":
                # Standard order
                identify_payload |= {
                    "last_standard_order_placed_ts": order_call.created_at,
                    "last_standard_order_placed_id": str(order_call.id_order),
                    "last_standard_order_placed_total": order_call.total,
                }
            case "c3ebe8d1-fde0-4a62-af3e-2e0ce5642408":
                # Return order
                identify_payload |= {
                    "last_return_order_placed_ts": order_call.created_at,
                    "last_return_order_placed_id": str(order_call.id_order),
                    "last_return_order_placed_total": order_call.total,
                }

        identify_payload |= {
            "last_order_placed_ts": order_call.created_at,
            "last_order_placed_id": str(order_call.id_order),
            "last_order_placed_total": order_call.total,
        }

        if order_call.id_coupon:
            identify_payload |= {"last_coupon_used_id": str(order_call.id_coupon)}

        self.segment_client.identify(
            user_id=str(order_call.user_id),
            traits=identify_payload,
        )
