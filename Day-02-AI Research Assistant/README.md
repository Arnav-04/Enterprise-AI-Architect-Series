# AI Research Assistant

AI Research Assistant is a small-scale agentic AI application that helps users research a topic by gathering information from the web, summarizing it, and answering follow-up questions with grounded, source-based responses.

The assistant fetches web pages, extracts and cleans their content, splits the material into token-aware chunks, and uses an LLM to produce concise and reliable answers.

## Overview

Manual research is often time-consuming and inconsistent. Users may need to open many web pages, read through irrelevant content, and manually combine the information into a useful answer. Important context can be missed, and results are hard to reproduce.

This project demonstrates an AI-assisted research workflow that can:

- accept a research question or topic from the user
- retrieve relevant content from web sources
- extract and clean webpage text
- split content into manageable chunks
- summarize and synthesize information from multiple sources
- answer questions using grounded responses with source references

## Project Goals

The goal of this project is to make research faster, more structured, and more consistent by combining:

- web retrieval
- content extraction
- chunking
- language model reasoning
- source-aware summarization

## Architecture

The workflow is designed around the following steps:

1. The user submits a question or topic.
2. The system retrieves relevant web pages.
3. The content is cleaned and parsed from HTML.
4. The text is split into chunks that fit model context limits.
5. The LLM processes the chunks and generates a concise answer.
6. The final response is returned with source-backed information.

## Tech Stack

This project uses:

- Python for application logic
- LangChain for orchestration and workflow management
- Ollama with the Phi-3 model for reasoning and summarization
- BeautifulSoup for HTML parsing and content extraction
- tiktoken for token-aware chunking and counting

## Prerequisites

Before running the project, make sure you have:

- Python 3.10 or newer
- Ollama installed and running
- The Phi-3 model downloaded locally

You can pull the model with:

```bash
ollama pull phi3
```