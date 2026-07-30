import asyncio
import os

from dotenv import load_dotenv

load_dotenv()


def build_chatbot():
    try:
        from autogen_agentchat.agents import AssistantAgent
        from autogen_ext.models.ollama import OllamaChatCompletionClient
    except ImportError as exc:
        raise RuntimeError(
            "AutoGen Ollama packages are missing or incompatible. "
            "Install them with: pip install 'autogen-agentchat' 'autogen-core' 'autogen-ext[ollama]'"
        ) from exc

    model = os.getenv("LOCAL_MODEL", "phi3")
    host = os.getenv("OLLAMA_HOST", "http://localhost:11434")

    model_client = OllamaChatCompletionClient(
        model=model,
        host=host,
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
