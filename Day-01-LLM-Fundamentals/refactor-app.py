from ollama import chat

def print_banner():
    print("Enterprise AI  Architect - Building Real Solutions")
    print("Day 1 - Enterprise LLM Fundamentals")

def get_ai_response(question):
    response=chat(
        model="phi3",
        messages=[
            {
                "role": "user",
                "content": question
            }
        ]
    )

    return response["message"]["content"]

def main():

    print_banner()

    print("\n Type 'exit' anytime to quit.\n")

    while True:

        question=input("You: ")

        if question.lower()=="exit":
            print("\nThank you for using Enterprise AI Architect!")
            break

        try:

            answer=get_ai_response(question)

            print("\nAI:\n")
            print(answer)
            print("\n")
        
        except Exception as ex:
            print(f"Error: {ex}\n")
        
if __name__ == "__main__":
    main()