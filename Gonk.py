import os
import random
import discord
from dotenv import load_dotenv

load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')
TOKEN = str(TOKEN).replace('{','').replace('}','')
TOKEN = TOKEN[:-1]
#For some reason importing from a .env file does not work unless you trim the {}'s 
#It also adds a 'n' character at the very end. I am assuming this is from a \n in the string?

intents = discord.Intents.default()
client = discord.Client(intents=intents)

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if client.user.mentioned_in(message):
        readings = [
            'Gonk Gonk (True)',
            'Gonk Gonk (Mostly True)',
            'Gonk Gonk (Not getting involved in this...)',
            'Gonk Gonk (Mostly False)',
            'Gonk Gonk (False)'
        ]

        response = random.choice(readings)
        await message.channel.send(response)

client.run(TOKEN)