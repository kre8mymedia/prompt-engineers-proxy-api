from pydantic import BaseModel, Field


class ResponseBodyContextChat(BaseModel):
    status: str = Field(example="success")
    channel: str = Field(example='2142315325')
    message: float or int = Field(example="Message was sent successfully!")