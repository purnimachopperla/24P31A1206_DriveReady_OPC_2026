
"""
Bloom & Blossom Flower Shop AI Agent
Day 04 - Tools, Structured Output and Order Management
"""

import os
import csv
from typing import Literal
from dotenv import load_dotenv
from pydantic import BaseModel, Field
from langchain.tools import tool
from langchain.agents import create_agent
from langchain_groq import ChatGroq


# 1. Load API key
load_dotenv()

api_key = os.getenv("GROQ_API_KEY")

if not api_key:
    raise ValueError("Please set GROQ_API_KEY in your .env file.")

# 2. Connect Groq model
llm = ChatGroq(
    model="openai/gpt-oss-20b",
    temperature=0.2,
    max_retries=3
)

# 3. Flower shop menu
MENU = {
    "rose bouquet": 499,
    "lily bouquet": 699,
    "tulip bouquet": 899,
    "mixed flower bouquet": 999,
    "premium wedding bouquet": 1499
}

ORDERS_FILE = "bloom_blossom_orders.csv"


# 4. Pydantic order validation
class FlowerOrder(BaseModel):
    name: str = Field(description="Customer's name")

    bouquet: Literal[
        "rose bouquet",
        "lily bouquet",
        "tulip bouquet",
        "mixed flower bouquet",
        "premium wedding bouquet"
    ]

    quantity: int = Field(ge=1)
    flower_colour: str
    delivery_date: str
    delivery_address: str
    message: str = "No message"


# 5. Flower shop tools

@tool
def get_bouquet_price(bouquet: str, quantity: int = 1) -> str:
    """Get the price of a bouquet and calculate the total cost."""

    price = MENU.get(bouquet.lower().strip())

    if price is None:
        return f"Sorry, {bouquet} is not available in our menu."

    if quantity < 1:
        return "Quantity must be at least 1."

    return f"{quantity} x {bouquet} = Rs. {price * quantity}"


@tool
def check_flower_availability(bouquet: str) -> str:
    """Check whether a bouquet is available in the menu."""

    if bouquet.lower().strip() in MENU:
        return f"{bouquet.title()} is listed in our menu."

    return f"{bouquet.title()} is not listed in our menu."


@tool
def get_delivery_details(delivery_type: str) -> str:
    """Provide information about home delivery or store pickup."""

    delivery_type = delivery_type.lower().strip()

    if delivery_type == "home delivery":
        return "Home delivery is available. Please provide the complete delivery address."

    elif delivery_type == "store pickup":
        return "Store pickup is available at Bloom & Blossom."

    return "Please choose home delivery or store pickup."


@tool
def save_flower_order(
    name: str,
    bouquet: str,
    quantity: int,
    flower_colour: str,
    delivery_date: str,
    delivery_address: str,
    message: str = "No message"
) -> str:
    """Validate and save a confirmed flower order to a CSV file."""

    try:
        order = FlowerOrder(
            name=name,
            bouquet=bouquet.lower().strip(),
            quantity=quantity,
            flower_colour=flower_colour,
            delivery_date=delivery_date,
            delivery_address=delivery_address,
            message=message
        )

        total = MENU[order.bouquet] * order.quantity

        file_exists = (
            os.path.exists(ORDERS_FILE)
            and os.path.getsize(ORDERS_FILE) > 0
        )

        with open(
            ORDERS_FILE,
            "a",
            newline="",
            encoding="utf-8"
        ) as file:

            writer = csv.writer(file)

            if not file_exists:
                writer.writerow([
                    "Name", "Bouquet", "Quantity", "Colour",
                    "Delivery Date", "Address", "Message", "Total"
                ])

            writer.writerow([
                order.name,
                order.bouquet,
                order.quantity,
                order.flower_colour,
                order.delivery_date,
                order.delivery_address,
                order.message,
                total
            ])

        return f"Order saved! Total amount: Rs. {total}"

    except Exception as e:
        return f"Could not save the order: {e}"


# 6. Agent instructions
SYSTEM = """
You are a friendly AI assistant for Bloom & Blossom Flower Shop.

Help customers choose bouquets and place flower orders.

RULES:
1. Use get_bouquet_price to check prices.
2. Use check_flower_availability to check bouquets.
3. Use get_delivery_details for delivery information.
4. Collect the customer's name, bouquet, quantity,
   flower colour, delivery date and address.
5. Ask for confirmation before saving an order.
6. Use save_flower_order only after confirmation.
7. Never invent prices or menu items.
8. Be polite, helpful and concise.
"""


# 7. Create AI agent
agent = create_agent(
    model=llm,
    tools=[
        get_bouquet_price,
        check_flower_availability,
        get_delivery_details,
        save_flower_order
    ],
    system_prompt=SYSTEM
)


# 8. Interactive chat
history = []

def chat(user_input: str) -> str:
    global history

    try:
        result = agent.invoke({
            "messages": history + [
                {"role": "user", "content": user_input}
            ]
        })

        history = result["messages"]

        return history[-1].content

    except Exception as e:
        print("Agent error:", e)
        return "Sorry, something went wrong. Please try again."


# 9. Run the flower shop agent
if __name__ == "__main__":

    print("\nWelcome to Bloom & Blossom Flower Shop!")
    print("Type 'exit' to stop the agent.\n")

    for item, price in MENU.items():
        print(f"{item.title()}: Rs. {price}")

    print("\nHow can I help you today?")

    while True:
        user_input = input("\nYou: ")

        if user_input.lower().strip() == "exit":
            print("Thank you for visiting Bloom & Blossom!")
            break

        if not user_input.strip():
            continue

        response = chat(user_input)
        print("\nBloom & Blossom:", response)
