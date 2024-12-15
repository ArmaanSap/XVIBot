from typing import Final
import os
from dotenv import load_dotenv
from discord import Intents, Client, Message
import responses

load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')

intents = Intents.default()

intents.message_content = True
client = Client(intents=intents)


async def send_message(message, user_message) -> None:
    if not user_message:
        print("Intents were likely not set correctly - Message was empty")
        return

    if message.mentions.users.has(client.user.id) & message.author.bot:



    is_private = user_message[0] == '?'
    is_public = user_message[0] == '!'

    if is_private:
        user_message = user_message[1:]

    try:
        response = responses.getresponses(user_message)
        if is_private:
            await message.author.send(response)
        elif is_public:
            await message.channel.send(response)

    except Exception as e:
        print(e)


@client.event
async def on_ready() -> None:
    print(f'{client.user} is now running!')

@client.event
async def on_message(message: Message) -> None:
    if message.author == client.user:
        return

    username: str = str(message.author)

    user_message: str = str(message.content)

    channel: str = str(message.channel)

    print(f'{username} said "{user_message}" in "{channel}"')
    await send_message(message, user_message)

def main() -> None:
    client.run(token=TOKEN)


if __name__ == "__main__":
    main()



