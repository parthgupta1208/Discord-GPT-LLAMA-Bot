# Discord GPT/LLAMA Bot

This Discord bot interacts with users by responding to messages using a Large Language Model (LLM). It employs the GROQ API internally to generate responses. Before running the bot, users need to configure their GROQ API key and Discord bot token.

## Setup

1. Clone the repository to your local machine:

   ```bash
   git clone https://github.com/parthgupta1208/Discord-GPT-LLAMA-Bot.git
   ```

2. Navigate to the project directory:

    ```bash
    cd Discord-GPT-LLAMA-Bot
    ```

3. Install dependencies:

   ```bash
   pip install -r requirements.txt
   ```

4. Create a `.env` file similar to the sample.env in the root directory of the project and add your GROQ API key and Discord bot token:

   ```
   GROQ_API_KEY=your_groq_api_key
   DISCORD_TOKEN=your_discord_token
   ```
## Creating and Setting Up a Discord Bot (For Newbies to Discord Bots)

1. Go to the [Discord Developer Portal](https://discord.com/developers/applications).

2. Click on the "New Application" button.

3. Name your application and click "Create".

4. In the application settings, navigate to the "Bot" tab and click "Add Bot". Confirm by clicking "Yes, do it!".

5. Under the bot settings, you can customize your bot (e.g., change the username, avatar). Make sure to enable the "MESSAGE CONTENT INTENT" under the "Privileged Gateway Intents" section.

6. Copy the bot token by clicking on the "Copy" button under the "TOKEN" section. This token will be used in the `.env` file you created earlier.

7. To add the bot to your server, go to the "OAuth2" tab, then to the "URL Generator" section. Select the `bot` scope and the permissions your bot needs. This will generate an OAuth2 URL.

8. Open the generated OAuth2 URL in your browser, select the server you want to add the bot to, and click "Authorize".


## Usage

*Please note that this bot is supposed to be used on a dedicated server as it treats all users as same and responds to all texts. To make it respond to certain prefix you can use `command_prefix` or a simple `if-startswith`.*

1. Add the bot to your Discord server.

2. Start the bot:

   ```bash
   python main.py
   ```

3. Once the bot is running, it will listen for messages on the Discord server.

4. Send a message on the server, and the bot will respond with a llama reply.

## Customization

To change the model used by the bot, modify the model in `gpt_utils.py` file.

Available Options are:
- LLaMA3 8b    : "llama3-8b-8192"
- LLaMA3 70b   : "llama3-70b-8192"
- Mixtral 8x7b : "mixtral-8x7b-32768"
- Gemma 7b     : "gemma-7b-it"

Groq API is easily replacable with OpenAI's GPT API without major code modifications.

## Features

- Responds to messages using a Large Language Model (LLM).
- Maintains context for up to 10 conversation messages.
- Utilizes the GROQ API internally.
- Requires users to set up their GROQ API key and Discord bot token.

## Contributing

Contributions are welcome! Please fork the repository and submit pull requests.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.