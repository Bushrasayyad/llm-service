from langchain_groq import ChatGroq
from langchain_core.messages import SystemMessage, HumanMessage
from app.config import settings

llm = ChatGroq(
    model=settings.default_model,
    api_key=settings.groq_api_key,
    temperature=0,
    max_retries=0,          # fail fast — matches your earlier debugging setup
    timeout=settings.request_timeout,
)

async def generate(prompt: str) -> dict:
    messages = [
        SystemMessage(content="You are a helpful assistant."),
        HumanMessage(content=prompt),
    ]

    result = await llm.ainvoke(messages)

    # LangChain returns usage metadata when the provider supports it
    usage = getattr(result, "usage_metadata", None) or {}

    return {
        "response": result.content,
        "model": settings.default_model,
        "tokens_used": usage.get("total_tokens", 0),
    }