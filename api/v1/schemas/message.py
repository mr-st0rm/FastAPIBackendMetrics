from pydantic import BaseModel


class MessageOut(BaseModel):
    id: int
    text: str

    class Config:
        orm_mode = True
