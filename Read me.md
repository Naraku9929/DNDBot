Installation Guide for TwitchBot

Prerequisites

Python 3.8+: Make sure you have Python 3.8 or higher installed.

Download from: Python Downloads

Twitch Developer Account:

Create a Twitch account if you don't have one.

Register a new application on Twitch to get an OAuth token for the bot.

Visit Twitch Developer Console and create an application to get your OAuth Token.

Install Required Python Packages:

Use pip to install the necessary packages by running the following command in your terminal:

pip install -r requirements.txt

File Structure

TwitchBot.py: The main bot script.

config.json: Configuration file to save bot settings (automatically created after the first setup).

requirements.txt: List of required Python packages.

Setting Up the Bot

Download the Files

Ensure you have TwitchBot.py saved in a directory where you want to run the bot.

Configure the Bot

Run the bot script using the command:

python TwitchBot.py

A graphical window will open, prompting you to enter:

OAuth Token: This is required to connect to Twitch.

Channel Name: The Twitch channel where the bot will operate.

Configure the features you'd like to enable, such as roll, NPC, loot, room, class, race, monster, and trap commands.

Save Configuration

Click Save Config to store your settings in a config.json file.

Connect to Twitch

Click Connect to Twitch to initiate the bot. The bot will connect to the specified channel and begin monitoring chat commands.

Running the Bot

Once connected, you can use the following commands in Twitch chat:

!roll: Rolls a 20-sided die.

!npc <name>: Adds an NPC with the given name.

!loot <item>: Adds loot with the given item name.

!room [name]: Discovers a random room or allows you to specify one.

!class [name]: Assigns a random class or lets you choose one.

!race [name]: Assigns a random race or lets you choose one.

!monster [name]: Summons a random monster or allows you to specify one.

!trap [name]: Sets off a random trap or lets you choose one.

Picking Winners

The bot has several commands for picking winners from previous submissions. You can use the GUI to pick a winner for rolls, NPCs, loot, etc. Click the respective buttons to have the bot announce the winner in Twitch chat.

Troubleshooting

Missing Config File: Ensure you save the configuration before attempting to connect.

Twitch Authentication Issues: Double-check your OAuth token and ensure it has the correct permissions.

Dependencies Not Installed: If you face issues related to missing modules, ensure all required Python packages are installed by running:

pip install -r requirements.txt

(The requirements.txt file includes the necessary packages for the bot to run.)

Stopping the Bot

To stop the bot, close the GUI window or press Ctrl + C in your terminal.

Additional Notes

Make sure to keep your OAuth Token secure to prevent unauthorized access.

You can update the bot configuration anytime by reopening the script and editing the settings through the GUI.