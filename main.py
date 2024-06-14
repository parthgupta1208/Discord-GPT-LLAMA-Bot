# bot.py
import os
from gpt_utils import gpt_response
import discord
from dotenv import load_dotenv

load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')
intent=discord.Intents.default()
intent.message_content=True
client = discord.Client(intents=intent)

@client.event
async def on_message(message):
    if message.author == client.user:
        return
    if message.content:
         await message.channel.send(gpt_response(message.content))

client.run(TOKEN)