
"""
Day 1 Task: Sweet Crumbs Home Bakery Assistant
DriveReady OPC 2026 - Agentic AI Track
"""

import os
from dotenv import load_dotenv
from langchain_groq import ChatGroq

# 1. Load API key from .env file
load_dotenv()

api_key = os.getenv("GROQ_API_KEY")

if not api_key:
    raise ValueError(
        "GROQ_API_KEY is missing. Please add it to your .env file."
    )

# 2. Bakery menu
BAKERY_MENU = {
    "Plum cake": 500,
    "Chocolate cake": 650,
    "Cupcake": 80
}

# 3. System prompt
SYSTEM_PROMPT = f"""
You are a helpful assistant for Sweet Crumbs Home Bakery.

ROLE:
Help customers with bakery products and orders.

FACTS:
- Menu and prices: {BAKERY_MENU}
- We bake cakes to order.
- Orders require at least 24 hours' notice.
- Eggless versions are available for all cakes.

RULES:
- Never promise a delivery time.
- If you do not know an answer, say you will check with the owner.
- Do not invent products or prices.

FORMAT:
- Reply politely and clearly.
- Keep every reply under 50 words.
"""

# 4. Connect to Groq model
def get_bakery_llm():
    return ChatGroq(
        model="openai/gpt-oss-120b",
        temperature=0,
        groq_api_key=api_key
    )

# 5. Ask the bakery assistant
def ask_bakery(question: str) -> str:
    llm = get_bakery_llm()

    messages = [
        ("system", SYSTEM_PROMPT),
        ("human", question)
    ]

    response = llm.invoke(messages)
    return response.content

# 6. Main program
def main():
    print("=" * 50)
    print("Sweet Crumbs Home Bakery Assistant")
    print("=" * 50)

    questions = [
        "What cakes do you have and what are their prices?",
        "Do you have eggless chocolate cake?",
        "Can I order a cake for tomorrow morning?"
    ]

    for question in questions:
        print("\nCustomer:", question)

        try:
            answer = ask_bakery(question)
            print("Assistant:", answer)
        except Exception as error:
            print("Error:", error)

    print("\nExecution completed!")


if __name__ == "__main__":
    main()
