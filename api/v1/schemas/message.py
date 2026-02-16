from pydantic import BaseModel, ConfigDict


class MessageOut(BaseModel):
    id: int
    text: str

    model_config = ConfigDict(from_attributes=True)
