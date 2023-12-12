from os import getenv
from time import sleep
import asyncio
import aiofiles

from dotenv import load_dotenv

load_dotenv()


async def retrieve_event():
    data_dict = {
        "user": "",
        "cmd": "",
        "approve": 0,
        "message": None
    }
    # Simulating retrieving an event
    async with aiofiles.open('/tmp/py-c', mode='r') as pipe:
        data = await pipe.read()
        data = data.split(" ")
        data_dict["user"] = data[0]
        data_dict["cmd"] = data[1]
        return data_dict


if __name__ == "__main__":
    test = asyncio.run(retrieve_event())
    print(test)
