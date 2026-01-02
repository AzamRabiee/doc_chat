from langchain_openai import ChatOpenAI

from config.settings import settings


def get_model(
    max_completion_tokens: int = 2000, temperature: float = 0.3
) -> ChatOpenAI:
    """
    Create and return a ChatOpenAI model instance with specified parameters.

    Args:
        max_tokens: Maximum number of tokens to generate (default: 2000)
        temperature: Sampling temperature, 0.0 to 2.0 (default: 0.3)

    Returns:
        ChatOpenAI model instance configured with the specified parameters
    """
    return ChatOpenAI(
        model=settings.OPENAI_MODEL_NAME,
        temperature=temperature,
        max_completion_tokens=max_completion_tokens,
        openai_api_key=settings.OPENAI_API_KEY,
    )
