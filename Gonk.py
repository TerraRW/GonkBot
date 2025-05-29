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
            'Gonk Gonk (Mostly Harmless)',
            'Gonk Gonk (You are not the Father)',
            'Gonk Gonk (Not getting involved in this...)',
            'Gonk Gonk (Mostly False)',
            'Gonk Gonk (False)'
        ]
        gonks = [
            'Gonk Gonk',
            'GONK GONK!',
            'gonk gonk',
            'gOnK gOnK',
            'gonk GONK!',
            'GONK! gonk',
            '𝕘𝕠𝕟𝕜 𝕘𝕠𝕟𝕜',
            '𝓰𝓸𝓷𝓴 𝓰𝓸𝓷𝓴',
            'ʞuoɓ ʞuoɓ',
            '01100111 01101111 01101110 01101011',

            'g̵̛̮͈̫̟͈͛̓̈́̄ð̸̨̼͚̜͙̅̅́͋͠ñ̶̟̼͍̺̝̾͒̀̊͝k̶̡̛͚̩̭̱̿̐̈̋ ̸̗̞͓̲̪͋͒́̃͆g̴͇͓̞̫͇̽̔̋̾̈́ð̴̧̣̮̯̟́̏̈́̊̋ṇ̶͓͖͈̃̑̌̀̈́̎͜k̸͖̱̫̠̿͋̋͐̚ͅ',

        ]
        response = random.choice(gonks)
        if '?' in message.content:
            response = random.choice(readings)

        await message.channel.send(response)

client.run(TOKEN)