# Discord-Bot-Welcomer-Free
# 🤖 Discord Welcome Bot (with Image Cards)

A modern, high-performance Discord bot built with `discord.py` and `easy-pil`. This bot automatically greets new members with a **customized image card**, sends a **private DM with server rules**, and features a professional **"Watching" status**.

## ✨ Features
* 🖼️ **Dynamic Welcome Cards:** Automatically generates an image featuring the new member's avatar and username.
* 📩 **DM Welcome & Rules:** Sends a clean, gold-themed Embed message to the user's DMs upon joining.
* 📡 **Custom Presence:** The bot stays in "Do Not Disturb" mode while "Watching the server."
* 🔒 **Secure Configuration:** Uses a `token.txt` file to keep your bot token safe and off your main code.

## 🚀 Setup Instructions

### 1. Prerequisites
Ensure you have Python 3.8+ installed. You will also need to install the required libraries:
```bash
pip install discord.py easy-pil
2. Discord Developer Portal
Create an application at the Discord Developer Portal.

Navigate to the Bot tab.

Crucial: Enable the Server Members Intent and Message Content Intent.

Reset and copy your Bot Token.

3. Files Required
Place these files in your project folder:

bot.py: The main script.

token.txt: Paste your bot token here (and nothing else).

background.jpg: An 800x450 image to serve as the welcome card background.

4. Running the Bot
Simply run the script via terminal:

Bash
python bot.py
🛠️ Configuration
In bot.py, make sure to update the following variable with your specific server ID:

Python
WELCOME_CHANNEL_ID = your_channel_id using developer mode # Change this to your channel ID
📝 License
This project is open-source and free to use.


---

### Pro-Tip: The `.gitignore` file
When uploading to GitHub, you **must** make sure you don't upload your `token.txt` by accident, or someone could steal your bot. 

Create a file named `.gitignore` in your folder and add this line inside it:
```text
token.txt
