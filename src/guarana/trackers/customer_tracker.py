from typing import Optional

import guarana
from guarana.schemas.customer import CustomerCall


class CustomerTracker(guarana.EventTracker):
    def __init__(self, segment_write_key: str):
        super().__init__(segment_write_key=segment_write_key)

    def identify_customer(self, customer_call: CustomerCall, anonymous_id: Optional[str] = None, **kwargs):
        customer_call_info = {
            **customer_call.dict(exclude_none=True, exclude_unset=True),
            **kwargs
        }

        self.segment_client.identify(
            user_id=str(customer_call.user_id),
            anonymous_id=anonymous_id,
            traits=customer_call_info
        )

        
