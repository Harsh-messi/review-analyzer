import os
from openai import OpenAI
from dotenv import load_dotenv

load_dotenv()

client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

def analyze_review(review):
    try:
        prompt = f"""
        Analyze the following review:
        1. Sentiment (Positive, Negative, Neutral)
        2. Short summary (1-2 lines)

        Review:
        {review}
        """

        response = client.chat.completions.create(
            model="gpt-4o-mini",
            messages=[{"role": "user", "content": prompt}],
            max_tokens=100
        )

        return response.choices[0].message.content

    except Exception as e:
        return f"Error in LLM: {str(e)}"