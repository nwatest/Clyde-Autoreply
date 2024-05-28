import discord
import os
import asyncio
import datetime
import pytz
import requests
from discord.ext import tasks, commands
from dotenv import load_dotenv
from keep_alive import keep_alive

load_dotenv()
TOKEN = os.getenv('TOKEN')

client = discord.Client(intents=discord.Intents.default())
messaged = []

@client.event
async def on_ready():
    print("Client Ready")

@client.event
async def on_message(message):
    if message.author.id == client.user.id:
        return

    if not message.guild:
        if message.author.id in messaged:
            return
    
        messaged.append(message.author.id)
        await asyncio.sleep(20)
        async with message.channel.typing():
            await asyncio.sleep(3)
            await message.channel.send(f"<:Clyde:1243626359465443408> **Thanks for messaging me,** {message.author.mention}\n\n<:WumpGift2:1241240919533948970> I want to say that I have received your request for **Discord Nitro!**\n<:wumpusplushie:1241165391078883348> Unfortunately, due to stock delays, it will take **3** days for me to send you the code.\n\n> <:one_:1244200748179525642> `)` If you want the Nitro **instantly**, please invite __**+3**__ more users and they must join. <a:blue_nitro:1198148964025905152>\n\n> <:two_:1244200749253132299> `)` If you are unable to do __**+3**__ invites, wait two days! <:blurpleCheck:1198149081470619821>")

keep_alive()
client.run(TOKEN, bot=False)
