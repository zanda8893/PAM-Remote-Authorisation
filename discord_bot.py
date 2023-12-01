#!./venv/bin/python3
import sys
from os import getenv

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

bot = discord.Bot(command_prefix="!", intents=intents)


def has_not_role(ctx) -> bool:

    if get(bot.guild.roles, name="Members") not in ctx.author.roles:
        return True
    raise commands.CheckFailure(f"{ctx.author} is already verified!")


@bot.event
async def on_ready():  # When bot is ready
    print(f'Logged on as {bot.user}!')

    bot.guild = bot.guilds[0]  # Get the first server the bot has joined (TODO: Make this configurable)

    channel = discord.utils.get(bot.guild.channels, name="approval")


@bot.event
async def on_member_join(member: discord.member.Member):  # When a member joins the server
    pass


@bot.command(description="status")
async def status(ctx):  # (TODO: add more to status)
    """
    This function is called when a user types !verify-me
    """
    await ctx.respond(f"Working")

if __name__ == "__main__":
    bot.run(getenv('DISCORD_TOKEN'))
