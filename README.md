
# XIV Bot v2 - Discord AI Utility Bot By Armaan Sapra

XIV Bot is a Discord bot powered by Groq's Llama model, designed to serve as an AI utility bot for Discord communities. The bot provides conversational AI capabilities along with moderation features. 

## Features

- **AI Conversations**: Powered by Groq's Llama 3 8B model for natural language interactions
- **User Memory**: Maintains individual chat histories for each user
- **Moderation Commands**: Kick, ban, and mute functionality for administrators
- **Multiple Interaction Modes**: 
  - Public mentions (bot responds when mentioned or "xivbot" is said)
  - Private messages (prefix with `-`)
  - Direct messages

## Setup Instructions

### Prerequisites

- Python 3.12 or higher
- Discord Developer Account
- Groq API Account

### Step 1: Discord Bot Setup

1. Go to the [Discord Developer Portal](https://discord.com/developers/applications)
2. Create a new application and bot
3. Copy the bot token
4. Invite the bot to your server with appropriate permissions:
   - Send Messages
   - Read Message History
   - Use Slash Commands
   - Kick Members (for moderation)
   - Ban Members (for moderation)
   - Moderate Members (for timeout/mute)

### Step 2: Groq API Setup

1. Visit [Groq](https://groq.com/) and create an account
2. Generate an API key
3. Copy the API key for configuration

### Step 3: Environment Configuration

Create a `.env` file in the root directory with the following variables:

```env
DISCORD_TOKEN=your_discord_bot_token_here
GROQ_API_KEY=your_groq_api_key_here
```

### Step 4: Installation

The bot will automatically install required dependencies when run on Replit. The main dependencies are:

- `discord.py` - Discord API wrapper
- `groq` - Groq API client
- `python-dotenv` - Environment variable management
- `flask` - Web framework (for keep-alive functionality)

### Step 5: Running the Bot

On Replit, simply click the **Run** button or use the "Run Discord Bot" workflow.

For local development:
```bash
python discordbot1.py
```

## Usage

### Conversation Modes

**Public Mentions**: Mention the bot or say "xivbot" in any channel
```
@XIVBot Hello, how are you?
```
or
```
Hey xivbot, what's the weather like?
```

**Private Messages**: Send a direct message to the bot
```
Hello XIV Bot!
```

**Command Mode**: Prefix with `!` for private command responses
```
!help
!users
!list
```

### Moderation Commands

Available to users with administrator permissions:

- `!kick @user [reason]` - Kick a user from the server
- `!ban @user [reason]` - Ban a user from the server  
- `!mute @user [reason]` - Timeout a user for 10 minutes

## Project Structure

```
├── discordbot1.py      # Main bot file with Discord event handling
├── geminitest.py       # Groq AI integration and chat history management
├── responses.py        # Response handling and async wrapper
├── .env               # Environment variables (not tracked)
├── pyproject.toml     # Python project dependencies
└── README.md          # This file
```

## Key Files

- **`discordbot1.py`**: Main Discord bot logic, event handlers, and moderation commands
- **`geminitest.py`**: AI conversation management using Groq's Llama model with persistent chat histories
- **`responses.py`**: Async wrapper for AI responses to prevent blocking Discord events

## Bot Personality

XIV Bot is designed to be:
- Conversational and friendly
- Responsive in first person
- Concise when appropriate, detailed when needed
- Community-focused utility bot

The bot remembers individual user conversations and can reference users by their Discord username or ping them directly.

## Deployment

This bot is designed to run either locally or to be hosted on the cloud, it was originally designed in PyCharm.

## Technical Details

- **AI Model**: Groq Llama 3 8B (8192 tokens)
- **Framework**: discord.py 2.5.2+
- **Python Version**: 3.12+
- **Hosting**: Local or Cloud-based

## Contributing

This bot was created by Armaan Sapra. Feel free to fork and modify for your own Discord communities.

## License

XIVBot is licensed under the MIT Free-use license. See LICENSE file for details.

## Support

For issues or questions, contact the bot developer or check the Discord server where the bot is deployed. Note that the bot does not come with any warranties or guarantee. By using the bot, you waive all responsibility from the creator and contributors for what it does and its use-cases.
