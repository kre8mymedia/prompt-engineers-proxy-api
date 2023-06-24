from typing import Any

from pydantic import BaseModel, Field

from src.enums import PromptConfig


class RequestBodyContextChat(BaseModel):
    question: str = Field(example="Can you provide a react code sample to render a form?")
    system: str = Field(example=PromptConfig.SYSTEM_MESSAGE_CONTEXTGPT.value)
    temperature: float or int = Field(example=0.9)
    model: str = Field(example='gpt-3.5-turbo-16k')
    sources: bool = Field(example=False)
    context: Any = Field({
        'faiss': {
            "bucket_name": "prompt-engineers-dev",
            "path": "formio.pkl",
        }
    })