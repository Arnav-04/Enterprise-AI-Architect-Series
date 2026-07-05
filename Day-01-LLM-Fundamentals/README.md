# Day 1 – Enterprise LLM Fundamentals

## Enterprise AI Architect – Building Real Solutions

---

## Overview

This project demonstrates how to run a Large Language Model (LLM) locally using **Microsoft Phi-3** through **Ollama** and interact with it using Python.

The objective is to understand the architecture behind local AI inference before moving toward enterprise-grade cloud AI services such as Azure OpenAI.

---

# Business Problem

Organizations want to leverage AI while:

- Keeping sensitive information private
- Reducing cloud inference costs
- Experimenting with AI locally
- Understanding AI architecture before production deployment

This project demonstrates how a locally hosted LLM can solve these challenges.

---

# Objectives

- Install Ollama
- Download Microsoft Phi-3
- Create a Python application
- Communicate with the model
- Understand local AI inference
- Learn enterprise architecture fundamentals

---

# Architecture

User

↓

Python Application

↓

Ollama

↓

Microsoft Phi-3

↓

AI Response

---

# Technologies Used

- Python
- Ollama
- Microsoft Phi-3
- VS Code

---

# Project Structure

Day-01-LLM-Fundamentals/

app.py

README.md

requirements.txt

architecture.png

.gitignore

---

# Installation

Clone repository

Install Ollama

Download Phi-3

Install requirements

```
pip install -r requirements.txt
```

Run

```
python app.py
```

---

# Features

Interactive CLI chatbot

Local AI inference

No cloud cost

No API key required

Modular code

Easy to extend

---

# Key Learnings

- What an LLM is
- How Ollama works
- Running local AI models
- Python SDK integration
- Modular application design
- Separation of Concerns

---

# Enterprise Perspective

Although this project uses a local model, the architecture closely resembles production AI systems.

The local model can later be replaced with:

- Azure OpenAI
- Azure AI Foundry
- OpenAI API
- Anthropic Claude
- Google Gemini

without significantly changing the application flow.

---

# Future Improvements

Conversation Memory

Streaming Responses

Prompt Templates

RAG Integration

FastAPI Backend

Streamlit UI

Azure OpenAI Integration

Authentication

Logging

Monitoring

---

# Author

Arnav Munshi

Enterprise AI Architect – Building Real Solutions Series