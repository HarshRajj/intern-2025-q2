
# Q2: Prompt Template with Variables

This repository contains the solution for Question 2.

## Description

A minimal Python script that generates tweets using a prompt template and the Google Gemini LLM. The script demonstrates dynamic prompt construction and secure API key management using a `.env` file.

## Key Features
* Reusable Function: A core generate_tweet() function can be easily reused with different inputs.
* Dynamic Prompting: Uses f-strings to create a precise, variable-driven prompt for the LLM.
* Clean Architecture: Sample tweet configurations are stored in a separate list, making the code clean and easy to modify.
* Secure: Manages the API key securely using a .env file, which is excluded from version control.

## Usage

1.  **Clone the repository:**
    ```bash
    git clone https://github.com/your-username/your-q2-repo.git
    cd your-q2-repo
    ```

2.  **Install dependencies:**
    ```bash
    pip install -r requirements.txt
    ```

3.  **Create a `.env` file** and add your Google API key:
    ```
    GOOGLE_API_KEY="YOUR_API_KEY_HERE"
    ```

4.  **Run the script:**
    ```bash
    python main.py
    ```

## Demo

[**▶️ Run on Google Colab**](https://colab.research.google.com/drive/1E3bOCfEmSpX-vOBsB1cmMAlPGGXlE9a9?usp=sharing)