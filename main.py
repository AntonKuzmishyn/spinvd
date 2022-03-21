import time
from telethon import TelegramClient
import json


f = open('api_config.json')
data = json.load(f)

api_id = data["api_id"]
api_hash = data["api_hash"]
dicks = data["orcs"]
message = data["message"]
number_of_messages = int(data["number_of_messages"])

client = TelegramClient('anon', api_id, api_hash)


async def main():
    for dick in dicks:
        for i in range(number_of_messages):
            await client.send_message(dick, message)
            print(f"{dick} is spammed!")
            time.sleep(1)


with client:
    client.loop.run_until_complete(main())
