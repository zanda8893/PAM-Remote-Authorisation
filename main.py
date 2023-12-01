from os import getenv
from time import sleep
import asyncio

from dotenv import load_dotenv

import discord_bot

load_dotenv()


async def retrieve_event():
    # Simulating retrieving an event
    with open("/tmp/py-c") as pipe:
        data = pipe.read()
        print(data)
