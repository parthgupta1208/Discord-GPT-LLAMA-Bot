import os
from dotenv import load_dotenv
from groq import Groq

load_dotenv()

client = Groq(
    api_key=os.getenv("GROQ_API_KEY"),
)
system_prompt=[{"role": "system","content": "Stricly limit response under 2000 characters. You are a Discord Bot built to provide information and have friendly conversations. Sound informal like a friend"}]
messages=[]
def gpt_response(message):
    global messages
    if len(messages)>20:
        messages.pop(0)
        messages.pop(0)
    messages.append({"role": "user", "content" : message})
    response = client.chat.completions.create(model="llama3-70b-8192",
        messages = system_prompt+messages
        )
    messages.append({"role": "assistant", "content" : response.choices[0].message.content})
    return response.choices[0].message.content