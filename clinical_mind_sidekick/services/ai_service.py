from ..core.openai_client import get_openai_client

async def process_ai_query(query: str, model: str) -> str:
    client = get_openai_client()
    completion = client.chat.completions.create(
        model=model,
        messages=[
            {"role": "user", "content": query}
        ]
    )
    return completion.choices[0].message.content