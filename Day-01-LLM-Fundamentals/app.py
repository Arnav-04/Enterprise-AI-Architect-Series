from ollama import chat

print("Enterprise AI Architect - Building real solutions")
print("Day 1 - LLM Fundamentals")

question=input("\nAsk your question: ")

response=chat(
    model="phi3",
    messages=[
        {
            "role": "user",
            "content": question,
        }
    ]
)

print("\nAI Response:\n")
print(response["message"]["content"])