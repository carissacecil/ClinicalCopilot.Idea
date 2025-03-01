from openai import OpenAI
from .config import get_settings
from functools import lru_cache

@lru_cache()
def get_openai_client():
    settings = get_settings()
    return OpenAI(api_key=settings.openai_api_key)