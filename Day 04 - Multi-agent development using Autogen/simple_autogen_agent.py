import asyncio
import os

from dotenv import load_dotenv

load_dotenv()


def build_chatbot():
    try:
        from autogen_agentchat.agents import AssistantAgent
        from autogen_ext.models.openai import OpenAIChatCompletionClient
    except ImportError as exc:
        raise RuntimeError(
            "AutoGen packages are missing or incompatible. Install them with: "
            "pip install 'autogen-agentchat' 'autogen-core' 'autogen-ext[openai]'"
        ) from exc

    model = os.getenv("LOCAL_MODEL", "phi3")
    base_url = os.getenv("OLLAMA_BASE_URL", "http://localhost:11434/v1")

    model_client = OpenAIChatCompletionClient(
        model=model,
        api_key="ollama",
        base_url=base_url,
        model_info={
            "vision": False,
            "function_calling": True,
            "json_output": True,
            "family": "llama",
            "structured_output": True,
        },
    )

    return AssistantAgent(
        name="local_helper",
        model_client=model_client,
        system_message="Answer briefly, clearly, and creatively.",
    )


async def ask_about_dragons():
    chatbot = build_chatbot()
    response = await chatbot.run(task="Tell me three interesting facts about dragons.")
    print(response)


if __name__ == "__main__":
    asyncio.run(ask_about_dragons())
