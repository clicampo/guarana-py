from datetime import date, datetime
from decimal import Decimal
from uuid import UUID

from guarana.schemas.base import BaseModel


class OrderCall(BaseModel):
    subtotal: Decimal
    discount: Decimal
    total: Decimal
    created_at: datetime
    pricing_reference_date: date
    id_order: UUID
    id_commercial: int
    id_order_category: UUID
    id_customer: UUID
    id_coupon: UUID
    created_at: datetime

