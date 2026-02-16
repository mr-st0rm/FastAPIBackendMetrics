from pydantic import BaseModel, constr


class ProcessRequest(BaseModel):
    data: str = constr(min_length=1, max_length=500)
