# Customer Service LLM Pipeline

This repository contains a Python-based pipeline that utilizes the OpenAI API to handle customer service queries. The pipeline is designed to classify user inquiries into primary and secondary categories, extract relevant product information, and provide appropriate responses to the user.

## Features

- Classifies customer service queries into primary categories (Billing, Technical Support, Account Management, General Inquiry) and corresponding secondary categories.
- Extracts relevant product information based on user queries.
- Generates human-like responses to provide the requested information to the user.
- Includes strategies to prevent prompt injection and ensure the LLM follows the desired behavior.
- Utilizes the OpenAI Moderation API to filter out inappropriate or malicious content.

## Prerequisites

To run the code in this repository, you need to have the following:

- Python 3.x installed
- OpenAI API key (stored in a `.env` file)
- Required Python packages listed in `requirements.txt`

## Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/Alami64/Customer-Service-LLM-Pipeline.git
   ```
2. Install the required packages:
   ```bash
   pip install -r requirements.txt
   ```
3. 3. Set up your OpenAI API key:
- Create a `.env` file in the project directory.
- Add your OpenAI API key in the following format: `OPENAI_API_KEY=your-api-key`.

## Usage

1. Run the main script:
   ```bash
   python main.py
   ```
2. Interact with the LLM pipeline by providing customer service queries.
3. The pipeline will classify the query, extract relevant product information, and generate an appropriate response.

## Code Structure

- `main.py`: The main script that runs the pipeline and handles user interactions.
- `utils.py`: Contains utility functions for extracting product information and generating responses.
- `products.py`: Defines the available products and their details.
- `moderation.py`: Implements the OpenAI Moderation API for content filtering.
