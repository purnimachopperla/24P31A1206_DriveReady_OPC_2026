# Day 2 – Prompts, Memory and Python Concepts

## Task Description

The objective of Day 2 was to improve the Sweet Crumbs Home Bakery chatbot by learning prompts, conversation memory, JSON, and important Python concepts.

## Topics Covered

- Messages and roles: system, user, and assistant.
- System prompts using Role, Facts, Rules, and Format.
- Few-shot prompting with examples.
- Asking the AI model to return JSON.
- Conversation memory using chat history.
- Python dictionaries and JSON.
- Functions and type hints.
- Decorators.
- Error handling using try/except.

## Implementation

- Created a bakery menu using a Python dictionary.
- Designed a system prompt with bakery information and rules.
- Used few-shot examples to classify customer messages.
- Used a function to calculate item prices.
- Added a decorator to log function calls.
- Maintained conversation history so the chatbot could remember previous messages.
- Limited the conversation history using `MAX_TURNS`.
- Used try/except to handle errors gracefully.

## Technologies Used

- Python
- Google Colab
- Groq API
- LangChain Groq
- JSON

## Learning Outcome

Learned how to create structured prompts, maintain chatbot memory, work with JSON and dictionaries, use functions and decorators, classify customer messages, and handle errors gracefully.