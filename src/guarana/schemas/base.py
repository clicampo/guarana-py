from uuid import UUID

from pydantic import BaseModel as PydanticBaseModel


class BaseModel(PydanticBaseModel):
    user_id: UUID

    def __init__(self, **kwargs):
        kwargs["user_id"] = kwargs["id_customer"]
        super().__init__(**kwargs)

    class Config:
        json_encoders = {
            UUID: lambda x: str(x),
        }
