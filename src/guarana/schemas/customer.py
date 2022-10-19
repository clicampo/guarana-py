from datetime import datetime
from typing import Optional
from uuid import UUID

from guarana.schemas.base import BaseModel


class CustomerCall(BaseModel):
    email: str
    id_customer: str
    name: Optional[str]
    firstname: Optional[str]
    street: Optional[str]
    number: Optional[str]
    complement: Optional[str]
    address: Optional[str]
    neighborhood: Optional[str]
    bairro: Optional[str]
    state: Optional[str]
    city: Optional[str]
    contact_name: Optional[str]
    cellphone: Optional[str]
    phone: Optional[str]
    payment_schedule_in_days: Optional[int]
    cep: Optional[str]
    zip: Optional[str]
    cpf: Optional[str]
    cnpj: Optional[str]
    is_shopping_enabled: Optional[bool]
    id_customer_group: Optional[UUID]
    id_location: Optional[UUID]
    id_commercial: Optional[int]
    potential: Optional[str]
    corporate_name: Optional[str]
    tax_regime: Optional[str]
    ibge_city_code: Optional[str]
    nfe_validated: Optional[bool]
    nfe_validated_at: Optional[datetime]
    nfe_validated: Optional[bool]
    nfe_validated_at: Optional[datetime]
    crm_validated: Optional[bool]
    crm_validated_at: Optional[datetime]
    business_hours_open: Optional[str]
    business_hours_close: Optional[str]
    address_type: Optional[str]
    address_reference: Optional[str]
    cuisine_category: Optional[str]
    blocked_by_credit_threshold: Optional[bool]
    id_customer_origin: Optional[UUID]
    customer_type: Optional[str]
    is_blocked: Optional[bool]
    notes: Optional[str]
    id_delivery_category: Optional[str]

    def __init__(self, **kwargs):
        kwargs["firstname"] = kwargs["name"]
        kwargs["address"] = f'{kwargs["street"]} {kwargs["number"]} {kwargs["complement"]}'
        kwargs["bairro"] = kwargs["neighborhood"]
        kwargs["phone"] = kwargs["cellphone"]
        kwargs["zip"] = kwargs["cep"]

        super().__init__(**kwargs)
