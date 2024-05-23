from pydantic import BaseModel


class ScrapperRequest(BaseModel):
    words: str
    amount: int