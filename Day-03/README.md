\# Day 03 – Your First AI Agent with LangChain



\## Project: Sweet Crumbs Home Bakery



\### Objective

To understand AI agents and build a simple bakery assistant using LangChain and Groq.



\### Topics Covered

1\. Introduction to AI Agents

2\. Difference between Chatbots and AI Agents

3\. Four components of an Agent:

&#x20;  - Brain – Large Language Model (LLM)

&#x20;  - Instructions – System Prompt

&#x20;  - Tools – Python Functions

&#x20;  - Memory – Conversation History

4\. Agent Loop: Think → Act → Observe → Repeat

5\. LangChain Prompt Templates

6\. LangChain Expression Language (LCEL)

7\. Conversation Memory

8\. CSV-based Automated Testing

9\. Creating an Agent using `create\_agent`



\### Technologies Used

\- Python

\- Google Colab

\- LangChain

\- LangChain Groq

\- Groq LLM (`openai/gpt-oss-120b`)

\- CSV



\### Project Description

Built a simple AI assistant for Sweet Crumbs Home Bakery. The assistant answers customer questions about cake prices, eggless options, and order requirements.



\### Bakery Information

| Product | Price |

|---|---:|

| Plum Cake | Rs 500 |

| Chocolate Cake | Rs 650 |

| Cupcake | Rs 80 |



\- Orders require 24 hours' notice.

\- Eggless versions are available.

\- Unknown information is referred to the bakery owner.



\### Implementation

\- Configured the Groq LLM.

\- Created a system prompt using `ChatPromptTemplate`.

\- Built a LangChain chain using LCEL.

\- Added conversation history for memory.

\- Created CSV-based tests to evaluate responses.

\- Created a basic agent using LangChain's `create\_agent`.



\### Learning Outcomes

\- Understood the basic concept of AI agents.

\- Learned how LangChain connects prompts and LLMs.

\- Implemented conversation memory.

\- Practiced automated testing using CSV files.

\- Created a basic AI agent.



\### Files

\- `Day-03.ipynb` – Google Colab notebook containing the implementation.

\- `task.py` – Python source code.

\- `README.md` – Project documentation.



\### Conclusion

Successfully explored the fundamentals of Agentic AI and built a simple Sweet Crumbs Home Bakery assistant using LangChain and Groq.

