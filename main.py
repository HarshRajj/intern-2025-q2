import os
from google import generativeai as genai
from dotenv import load_dotenv

GEMINI_MODEL = 'gemini-2.0-flash'

TWEET_SAMPLES = [
    {"topic": "the future of renewable energy", "tone": "optimistic", "max_words": 30},
    {"topic": "tips for effective remote work", "tone": "professional", "max_words": 25},
    {"topic": "the joy of discovering new music", "tone": "enthusiastic", "max_words": 35},
]

def generate_tweet(topic: str, tone: str, max_words: int) -> None:
    try:
        prompt = (
            f"Generate a tweet about the following topic: '{topic}'. "
            f"The tone of the tweet should be {tone}. "
            f"Please ensure the tweet is under {max_words} words. "
            f"Do not include any hashtags or URLs."
        )

        model = genai.GenerativeModel(GEMINI_MODEL)
        response = model.generate_content(prompt)
        
        print("--- Sample Tweet ---")
        print(f"Topic: {topic}, Tone: {tone}, Max Words: {max_words}")
        print(f"Tweet: {response.text.strip()}")
        print("-" * 20 + "\n")

    except Exception as e:
        print(f"An error occurred while generating tweet for topic '{topic}': {e}")

def main() -> None:
    load_dotenv()
    api_key = os.getenv("GOOGLE_API_KEY")

    if not api_key:
        print("Error: GOOGLE_API_KEY was not found. Please check your .env file.")
        return

    genai.configure(api_key=api_key)

    for sample in TWEET_SAMPLES:
        generate_tweet(
            topic=sample["topic"], 
            tone=sample["tone"], 
            max_words=sample["max_words"]
        )

if __name__ == "__main__":
    main()