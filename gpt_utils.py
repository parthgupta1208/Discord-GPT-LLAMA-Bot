import os
from dotenv import load_dotenv
from groq import Groq

load_dotenv()

client = Groq(
    api_key=os.getenv("GROQ_API_KEY"),
)

def gpt_response(message):
    chat_completion = client.chat.completions.create(
        messages=[
            {
                "role": "system",
                "content": "Stricly limit response under 2000 characters.",
            },
            {
                "role": "user",
                "content": message,
            }
        ],
        model="llama3-8b-8192",
    )
    return chat_completion.choices[0].message.content