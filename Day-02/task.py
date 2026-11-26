
import os
import json
from dotenv import load_dotenv
from langchain_groq import ChatGroq

load_dotenv()

MENU = {
    "plum cake": 500,
    "chocolate cake": 650,
    "cupcake": 80
}

SYSTEM_PROMPT = f"""
You are a friendly assistant for Sweet Crumbs Home Bakery.

Menu: {json.dumps(MENU)}
Orders require 24 hours' notice.
Eggless versions are available for all cakes.

Never promise a delivery time or invent prices.
If unsure, say you will check with the owner.
Keep replies under 50 words.
"""

llm = ChatGroq(
    model="openai/gpt-oss-120b",
    temperature=0,
    groq_api_key=os.getenv("GROQ_API_KEY")
)

# Few-shot message classification
messages = [
    ("system", "Classify the message as order, inquiry, or complaint. Reply with one word."),
    ("human", "I want two chocolate cakes."),
    ("ai", "order"),
    ("human", "What is the cupcake price?"),
    ("ai", "inquiry"),
    ("human", "My cake arrived damaged."),
    ("ai", "complaint"),
    ("human", "I need one plum cake.")
]

print("Category:", llm.invoke(messages).content)

# Conversation memory
history = []
MAX_TURNS = 2

def chat(user_message: str) -> str:
    history.append(("human", user_message))
    history[:] = history[-(MAX_TURNS * 2):]

    response = llm.invoke(
        [("system", SYSTEM_PROMPT)] + history
    )
    history.append(("ai", response.content))
    return response.content

# Price function with type hints
def log_call(func):
    def wrapper(*args):
        print("Function started:", func.__name__)
        result = func(*args)
        print("Function completed!")
        return result
    return wrapper

@log_call
def calculate_price(item: str, quantity: int) -> int:
    return MENU[item.lower()] * quantity

try:
    print("Total:", calculate_price("plum cake", 2))
    print(chat("What cakes are available?"))
except KeyError:
    print("Sorry, this item is not available.")
except Exception as e:
    print("Something went wrong:", e)
