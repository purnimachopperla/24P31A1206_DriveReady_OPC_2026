\# Bloom \& Blossom – Flower Shop AI Agent



\## Project Overview

Bloom \& Blossom is an AI-powered flower shop assistant built using Python, LangChain and Groq. It helps customers explore bouquets, check prices, get delivery information and place flower orders.



\## Objectives

\- Build an AI agent using LangChain.

\- Create custom tools using the `@tool` decorator.

\- Validate customer orders using Pydantic.

\- Save customer orders in a CSV file.

\- Connect the agent to a Groq language model.



\## Flower Menu



| Bouquet | Price |

|---|---:|

| Rose Bouquet | ₹499 |

| Lily Bouquet | ₹699 |

| Tulip Bouquet | ₹899 |

| Mixed Flower Bouquet | ₹999 |

| Premium Wedding Bouquet | ₹1,499 |



\## Technologies Used

\- Python

\- LangChain

\- LangChain Groq

\- Groq LLM (`openai/gpt-oss-20b`)

\- Pydantic

\- CSV

\- Python-dotenv



\## AI Agent Tools



1\. \*\*get\_bouquet\_price()\*\* – Calculates bouquet prices based on quantity.

2\. \*\*check\_flower\_availability()\*\* – Checks whether a bouquet is listed in the menu.

3\. \*\*get\_delivery\_details()\*\* – Provides home delivery and store pickup information.

4\. \*\*save\_flower\_order()\*\* – Validates and saves customer orders into a CSV file.



\## Order Validation

The Pydantic `FlowerOrder` model validates:

\- Customer name

\- Bouquet type

\- Quantity

\- Flower colour

\- Delivery date

\- Delivery address

\- Greeting message



\## Project Structure



```text

Day-04-Flower-Shop/

│

├── task.py

├── README.md

├── bloom\_blossom\_orders.csv

└── .env

```



\*\*Note:\*\* The `.env` file contains the Groq API key and must not be uploaded to GitHub.



\## Installation



Install the required packages:



```bash

pip install langchain langchain-groq pydantic python-dotenv

```



\## Configuration



Create a `.env` file in the project folder:



```text

GROQ\_API\_KEY=your\_groq\_api\_key

```



\## How to Run



Run the following command:



```bash

python task.py

```



The AI agent will start interacting with customers in the terminal.



Type `exit` to stop the agent.



\## Sample Order



| Field | Value |

|---|---|

| Customer | Priya |

| Bouquet | Rose Bouquet |

| Quantity | 2 |

| Colour | Red |

| Delivery Date | 30 November |

| Address | Ravulapalem |

| Total | ₹998 |



\## Learning Outcomes

\- Understanding AI agents and tool calling.

\- Creating custom tools using LangChain.

\- Using Pydantic for structured data validation.

\- Connecting an LLM using Groq.

\- Managing customer orders using CSV files.

\- Building a practical AI-powered business application.



\## Conclusion

Bloom \& Blossom demonstrates how an AI agent can automate basic flower shop operations, assist customers and manage orders using Python, LangChain and Groq.

