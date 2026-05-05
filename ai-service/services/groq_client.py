import os
import time
from dotenv import load_dotenv
from groq import Groq

# Load environment variables
load_dotenv()

# Get API key
api_key = os.getenv("GROQ_API_KEY")

# Initialize Groq client
client = Groq(api_key=api_key)


def call_groq(prompt):
    start_time = time.time()

    try:
        # 🔥 Call Groq API
        response = client.chat.completions.create(
            model="mixtral-8x7b-32768",
            messages=[
                {"role": "user", "content": prompt}
        ],
        temperature=0.7,
        max_tokens=500
     )

        output = response.choices[0].message.content

        return {
            "result": output,
            "is_fallback": False,
            "response_time": round(time.time() - start_time, 2)
        }

    except Exception as e:
        # 🔍 Print error for debugging (very important)
        print("🔥 GROQ ERROR:", str(e))

        # 🚨 Fallback response
        return {
            "result": "AI service temporarily unavailable. Showing fallback response.",
            "is_fallback": True,
            "response_time": round(time.time() - start_time, 2)
        }