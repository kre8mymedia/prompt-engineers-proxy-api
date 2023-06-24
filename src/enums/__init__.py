from enum import Enum

from src.config.prompts import (SYSTEM_MESSAGE_CHATGPT,
                                SYSTEM_MESSAGE_CONTEXTGPT)


class PromptConfig(Enum):
    SYSTEM_MESSAGE_CONTEXTGPT = SYSTEM_MESSAGE_CONTEXTGPT
    SYSTEM_MESSAGE_CHATGPT = SYSTEM_MESSAGE_CHATGPT