from datetime import datetime
from uuid import UUID

from pydantic import BaseModel as PydanticBaseModel


class BaseModel(PydanticBaseModel):
    user_id: UUID
