# Q2: Prompt Template with Variables
The script demonstrates the use of a reusable prompt template to generate dynamic content from the Google Gemini LLM.
---
## Description
This Python script generates tweets based on a dynamic template that accepts three parameters: topic, tone, and max_words. It showcases professional coding practices by separating configuration from logic, using clear function definitions, and including error handling. The script produces three sample tweets as required.
### Key Features
* Reusable Function: A core generate_tweet() function can be easily reused with different inputs.
* Dynamic Prompting: Uses f-strings to create a precise, variable-driven prompt for the LLM.
* Clean Architecture: Sample tweet configurations are stored in a separate list, making the code clean and easy to modify.
* Secure: Manages the API key securely using a .env file, which is excluded from version control.
---
## Usage
To run this script on your local machine, follow these steps.
### 1. Prerequisites
* Python 3.8+
* A Google Gemini API key
### 2. Setup
First, clone the repository to your local machine:
` bash
Next, install the required Python packages:
` bash
### 3. Configuration
Create a file named .env in the root of the project folder. This file will store your secret API key. Add your key to this file as shown below:
`
### 4. Execution
Run the script from your terminal:
` bash
The script will print three sample tweets to the console.
---
## Demo
A live, interactive demo of this script is available on Google Colab. The notebook allows you to run the code and see the output without any local setup.

Run on Google colab(https://colab.research.google.com/drive/1E3bOCfEmSpX-vOBsB1cmMAlPGGXlE9a9?usp=sharing)