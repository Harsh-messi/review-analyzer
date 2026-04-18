# Review Analyzer using LLM

## Description
This project is a Python-based application that extracts product reviews from a webpage, processes and cleans the data, and uses an OpenAI-compatible LLM API to generate sentiment analysis and concise summaries.

## Features
- Scrapes product reviews from a URL
- Cleans and preprocesses text
- Handles long reviews using chunking
- Generates:
  - Sentiment (Positive/Negative/Neutral)
  - Summary
- Stores output in CSV format
- Basic error handling

## Tech Stack
- Python
- requests
- BeautifulSoup
- pandas
- OpenAI API
- dotenv

## How to Run
1. Install dependencies:
   ```bash
   pip install -r requirements.txt
