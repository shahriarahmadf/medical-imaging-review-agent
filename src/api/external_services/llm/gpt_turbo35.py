"""Module for gpt-3.5-turbo api call."""

from langchain_openai import ChatOpenAI

from src.api.config.core import OPENAI_API_KEY

def get_gpt_3_5_turbo():
    """Returns gpt-3.5-turbo."""
    print('Returning gpt-3.5-turbo...')
    return ChatOpenAI(
        model_name="gpt-3.5-turbo",
        temperature=0,
        max_tokens=128,
        max_retries=2,
        api_key = OPENAI_API_KEY
    )