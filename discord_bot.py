#!./venv/bin/python3
import sys
from os import getenv
import asyncio

import main

import discord
from discord import Intents
from discord.ext import commands, tasks
from discord.utils import get
from dotenv import load_dotenv

load_dotenv()

if getenv('DEBUG'):
    print("PRODUCTION MODE")
    sys.tracebacklimit = 0

intents = Intents.default()
intents.members = True
intents.message_content = True
intents.reactions = True

bot = discord.Bot(command_prefix="!", intents=intents)


@bot.event
async def on_ready():  # When bot is ready
    print(f'Logged on as {bot.user}!')

    bot.guild = bot.guilds[0]  # Get the first server the bot has joined (TODO: Make this configurable)

    bot.channel = get(bot.guild.channels, name="approval")
    await bot.channel.send("Bot online")
    #bot.loop.create_task(test_task())
    bot.loop.create_task(check_events())
    bot.approvals = []

async def test_task():
    while True:  # Replace this with your task's condition
        print("Bluh")
        await asyncio.sleep(60)  # For example, wait for 60 seconds

async def check_events():
    while True:
        event_data = await main.retrieve_event()
        if event_data:
            await approve(event_data)
        await asyncio.sleep(5)


@bot.command(description="status")
async def status(ctx):  # (TODO: add more to status)
    """
    This function is called when a user types !verify-me
    """
    await ctx.respond(f"Working")


async def approve(data):
    data['message'] = await bot.channel.send(f"{data['user']} is attempting to run {data['cmd']} approve?")
    bot.approvals.append(data)


@bot.event
async def on_reaction_add(reaction, user):
    message = reaction.message  # our embed
    if message.channel.id == bot.channel.id:  # checking if it's the same channel
        if message.author == bot.user:  # checking if it's sent by the bot
            if str(reaction.emoji) == "👍":  # checking the emoji
                for approve in bot.approvals:
                    if approve['message'].id == message.id:
                        approve['approve'] = 1
                        print(bot.approvals)

bot.run(getenv('DISCORD_TOKEN'))

if __name__ == "__main__":
    bot.run(getenv('DISCORD_TOKEN'))
