from typing import Final
import os
from dotenv import load_dotenv
from discord import Intents, Client, Message
import responses
import datetime


now = datetime.datetime.now()
load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')

intents = Intents.default()
intents.message_content = True
intents.members = True
client = Client(intents=intents)


async def handle_moderation_command(message, command_parts):
    """Handle moderation commands like kick, ban, mute"""
    if not message.guild:
        await message.channel.send("Moderation commands can only be used in servers.")
        return

    # Check if bot has admin permissions
    bot_member = message.guild.get_member(client.user.id)
    if not bot_member.guild_permissions.administrator:
        await message.channel.send("I need administrator permissions to use moderation commands.")
        return

    # Check if user has admin permissions
    if not message.author.guild_permissions.administrator:
        await message.channel.send("You need administrator permissions to use moderation commands.")
        return

    command = command_parts[0].lower()
    
    if len(command_parts) < 2:
        await message.channel.send(f"Usage: `!{command} @user [reason]`")
        return

    # Try to get the mentioned user
    if len(message.mentions) == 0:
        await message.channel.send("Please mention a user to moderate.")
        return

    target_user = message.mentions[0]
    target_member = message.guild.get_member(target_user.id)
    
    if not target_member:
        await message.channel.send("User not found in this server.")
        return

    # Check if target is the bot itself
    if target_member.id == client.user.id:
        await message.channel.send("I cannot moderate myself!")
        return

    # Check if target is the command user
    if target_member.id == message.author.id:
        await message.channel.send("You cannot moderate yourself!")
        return

    # Check if target has higher or equal permissions
    if target_member.top_role >= message.author.top_role and message.author.id != message.guild.owner_id:
        await message.channel.send("You cannot moderate someone with equal or higher permissions.")
        return

    reason = " ".join(command_parts[2:]) if len(command_parts) > 2 else "No reason provided"

    try:
        if command == "kick":
            await target_member.kick(reason=f"Kicked by {message.author}: {reason}")
            await message.channel.send(f"✅ {target_user.mention} has been kicked. Reason: {reason}")
        
        elif command == "ban":
            await target_member.ban(reason=f"Banned by {message.author}: {reason}")
            await message.channel.send(f"✅ {target_user.mention} has been banned. Reason: {reason}")
        
        elif command == "mute":
            # Try to timeout the user for 10 minutes
            timeout_duration = datetime.timedelta(minutes=10)
            await target_member.timeout(timeout_duration, reason=f"Muted by {message.author}: {reason}")
            await message.channel.send(f"✅ {target_user.mention} has been muted for 10 minutes. Reason: {reason}")
        
    except Exception as e:
        await message.channel.send(f"Failed to {command} {target_user.mention}: {str(e)}")


async def send_message(message, user_message) -> None:
    if not user_message:
        print("Intents were likely not set correctly - Message was empty")
        return

    is_private = user_message[0] == '-'
    is_public = False
    is_command = user_message[0] == "!"
    send_data = False
    
    # Handle moderation commands
    if is_command:
        command_parts = user_message[1:].split()
        if command_parts and command_parts[0].lower() in ['kick', 'ban', 'mute']:
            await handle_moderation_command(message, command_parts)
            return

    if client.user.mentioned_in(message) and not message.author.bot or "xivbot" in str(message.content).lower():
        # Clean the user's message by removing the bot mention
        clean_message = user_message
        if client.user.mentioned_in(message):
            clean_message = clean_message.replace(f'<@{client.user.id}>', '').strip()
        
        # Just use the actual user message instead of the context message
        context_message = clean_message if clean_message else "Hello!"
        is_public = True

    if is_private:
        user_message = user_message[1:]

    try:
        if is_public:
            response = await responses.getresponses_async(context_message, str(message.author.id))
        elif is_command or is_private:
            response = await responses.getresponses_async(user_message, str(message.author.id))
        else:
            return

        if is_private:
            await message.author.send(response)
        elif is_public:
            await message.channel.send(response)
        elif is_command:
            await message.author.send(response)

    except Exception as e:
        await message.author.send(f"""Your message '{user_message}' was unable to be processed by the bot.
                Error message: {e}. **Try rephrasing it or shortening it**""")
        print(e)


@client.event
async def on_ready() -> None:
    print(f'{client.user} is now running!')


metadata = []
@client.event
async def on_message(message: Message):
    if message.author == client.user:
        return

    username: str = str(message.author)

    user_message: str = str(message.content)

    channel: str = str(message.channel)

    server: str = str(message.guild)


    print(f'{username} said "{user_message}" in "{channel}" in the server "{server}"')
    await send_message(message, user_message)



def main() -> None:
    client.run(token=TOKEN)


if __name__ == "__main__":
    main()

