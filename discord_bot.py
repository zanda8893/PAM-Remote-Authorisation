#!./venv/bin/python3
import sys
from os import getenv
import asyncio

import main

import discord
from discord import Intents
from discord.ext import commands
from discord.utils import get
from dotenv import load_dotenv

load_dotenv()

if getenv('DEBUG'):
    print("PRODUCTION MODE")
    sys.tracebacklimit = 0

intents = Intents.default()
intents.members = True
intents.message_content = True

bot = discord.Bot(command_prefix="!", intents=intents)


@bot.event
async def on_ready():  # When bot is ready
    print(f'Logged on as {bot.user}!')

    bot.guild = bot.guilds[0]  # Get the first server the bot has joined (TODO: Make this configurable)

    bot.channel = get(bot.guild.channels, name="approval")
    await bot.channel.send("Bot online")
    bot.loop.create_task(check_events())


async def check_events():
    while True:
        event_data = await main.retrieve_event()
        if event_data:
            await approve()
        await asyncio.sleep(5)


@bot.command(description="status")
async def status(ctx):  # (TODO: add more to status)
    """
    This function is called when a user types !verify-me
    """
    await ctx.respond(f"Working")


async def approve():
    await bot.channel.send("Called from main")

bot.run(getenv('DISCORD_TOKEN'))

if __name__ == "__main__":
    bot.run(getenv('DISCORD_TOKEN'))
