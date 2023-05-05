# Discord Wake On LAN Bot

This is a Discord bot that can be used to turn on a PC remotely using the Wake-on-LAN protocol. The bot runs on a Raspberry Pi or other device and responds to a specific command in a Discord server.

## Setup

To use the bot, you need to perform the following steps:

1. Install the required Python packages by running `pip install -r requirements.txt`.
2. Obtain the MAC address of the target PC and replace the `addr` variable in `main.py` with it.
3. Generate a secret key by defining a random key in the `secret_key` variable in `main.py`.
4. Generate a QR code for the TOTP secret by running `qrcode.make(uri)` and saving it to a file (e.g. `qrcode.png`). 
5. Create a new Discord bot and obtain its token. You can follow the instructions in the [Discord Developer Portal](https://discord.com/developers/docs/intro).
6. Replace the `Token` variable in `main.py` with the Discord bot token.
7. Run the bot using `python main.py`.

## Usage

Once the bot is running, you can use the `!wake` command in any channel where the bot is present to wake up the PC. The command must be followed by a valid TOTP code generated from the secret key, which is valid for a short period of time (usually 30 seconds). If the TOTP code is correct, the bot will send a Wake-on-LAN packet to the target PC and confirm that it was sent. If the code is incorrect or missing, the bot will reply with an error message.

### Discord
[Leoon v2 git hub](https://discord.gg/vDZsqU3jC8)
