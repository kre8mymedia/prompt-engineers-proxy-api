from pydantic import BaseModel, Field


class ResponseBodyContextChat(BaseModel):
    status: str = Field(example="success")
    channel: str = Field(example='1687483806518')
    message: str = Field(example="Message successfully sent!")