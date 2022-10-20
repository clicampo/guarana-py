from datetime import datetime, time
from typing import Optional
from uuid import UUID

from pydantic import Field, root_validator

from guarana.schemas.base import BaseModel


class CustomerCall(BaseModel):
    email: str
    id_customer: UUID
    name: Optional[str] = Field(alias="firstname")
    street: Optional[str]
    number: Optional[str]
    complement: Optional[str]
    address: Optional[str]
    state: Optional[str]
    city: Optional[str]
    contact_name: Optional[str]
    cellphone: Optional[str] = Field(alias="phone")
    neighborhood: Optional[str] = Field(alias="bairro")
    payment_schedule_in_days: Optional[int]
    cep: Optional[str] = Field(alias="zip")
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
    business_hours_open: Optional[time]
    business_hours_close: Optional[time]
    address_type: Optional[str]
    address_reference: Optional[str]
    cuisine_category: Optional[str]
    blocked_by_credit_threshold: Optional[bool]
    id_customer_origin: Optional[UUID]
    customer_type: Optional[str]
    is_blocked: Optional[bool]
    notes: Optional[str]
    id_delivery_category: Optional[UUID]

    @root_validator
    def build_address(cls, values) -> dict:
        address_string = ""
        if values["street"]:
            address_string = values["street"]
        else:
            return values
        if values["number"]:
            address_string += f", {values['number']}"
        if values["complement"]:
            address_string += f" - {values['complement']}"

        values["address"] = address_string

        return values
