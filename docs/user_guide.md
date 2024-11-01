**User Guide for TwitchBot**

### Introduction

TwitchBot is a custom bot designed for interacting with your Twitch chat, providing fun features like rolling dice, adding NPCs, generating loot, and much more—all at your command. This guide will walk you through the various commands and features that TwitchBot offers, as well as how to make the most of its functionality.

### Getting Started

To start the bot, you need to have set up the configuration through the installation process. Once configured, run the bot by executing:
```sh
python TwitchBot.py
```
This will open a GUI where you can connect the bot to your Twitch channel and enable specific features.

### Chat Commands

Once the bot is running, you can interact with it using the following commands in Twitch chat. These commands can enhance your Twitch stream by allowing viewers to engage with your content.

#### Available Commands

- **`!roll`**: Rolls a 20-sided die.
  - Example: `!roll`
  - The bot will announce the roll result, e.g., "@username, you rolled a 15!"

- **`!npc <name>`**: Adds an NPC with the given name to the game.
  - Example: `!npc Geralt`
  - The bot will announce: "The Twitch Chat God @username is summoning their power to add Geralt to the realm!"

- **`!loot <item>`**: Adds loot with the given item name.
  - Example: `!loot Sword of Destiny`
  - The bot will announce: "The Twitch Chat God @username is summoning their power to add Sword of Destiny to the realm!"

- **`!room [name]`**: Discovers a random room or lets you specify one.
  - Example (random): `!room`
  - Example (specified): `!room Throne Room`
  - The bot will announce: "The Twitch Chat God @username is making a Throne Room!"

- **`!class [name]`**: Assigns a random class or lets you choose one.
  - Example (random): `!class`
  - Example (specified): `!class Bard`
  - The bot will announce: "The Twitch Chat God @username has changed that person’s class to Bard!"

- **`!race [name]`**: Assigns a random race or lets you choose one.
  - Example (random): `!race`
  - Example (specified): `!race Elf`
  - The bot will announce: "The Twitch Chat God @username makes that person an Elf!"

- **`!monster [name]`**: Summons a random monster or lets you specify one.
  - Example (random): `!monster`
  - Example (specified): `!monster Dragon`
  - The bot will announce: "The Twitch Chat God @username is summoning a Dragon!"

- **`!trap [name]`**: Sets off a random trap or lets you choose one.
  - Example (random): `!trap`
  - Example (specified): `!trap Spike Trap`
  - The bot will announce: "The Twitch Chat God @username is making a Spike Trap!"

- **`!dndhelp`**: Displays a list of available commands.
  - Example: `!dndhelp`
  - The bot will provide a summary of all commands.

### Picking Winners

TwitchBot includes commands to pick winners from viewer submissions, such as rolls or created NPCs. These can be accessed through the GUI:

- **Pick Roll Winner**: Chooses a winner based on previous roll submissions.
- **Pick NPC Winner**: Chooses a winner from the added NPCs.
- **Pick Loot Winner**: Chooses a winner from the added loot items.

The bot will announce the selected winner in Twitch chat.

### Using the GUI

The GUI interface provides easy access to configure and control the bot. From the GUI, you can:

- **Save Configuration**: Click "Save Config" to store your settings in `config.json` for future use.
- **Connect to Twitch**: Click "Connect to Twitch" to have the bot join your channel.
- **Enable or Disable Features**: You can enable or disable commands like rolling, adding NPCs, loot, etc., to fit the needs of your stream.
- **Pick Winners**: Use the available buttons in the GUI to pick winners for each category.

### Best Practices

- **Interacting with Viewers**: Use commands to engage viewers and keep them entertained. Encourage them to add their own NPCs or suggest loot to make the game more interactive.
- **Bot Reliability**: Always keep your `config.json` file updated to avoid any issues when connecting to Twitch.
- **Testing**: Before going live, test the bot in a private channel to ensure everything is working as expected.

### Troubleshooting Tips

- **Bot Not Connecting**: Ensure that the OAuth token and channel name are correct in the configuration. Verify your internet connection and try again.
- **Commands Not Responding**: Make sure the commands are enabled in the GUI. You can also check the console for error messages.
- **Dependencies Issues**: If you get errors related to missing Python modules, ensure you have installed all packages from `requirements.txt`:
  ```sh
  pip install -r requirements.txt
  ```

### Security Considerations

- **OAuth Token Security**: Keep your **OAuth Token** private. Anyone with this token can control the bot in your Twitch channel, so treat it like a password.
- **Regular Updates**: Regularly update Python packages to avoid security vulnerabilities.

### Stopping the Bot

To stop the bot, you can:

- **Close the GUI**: This will terminate the bot session.
- **Keyboard Interrupt**: Press `Ctrl + C` in the terminal where the bot is running.

### Feedback and Support

If you encounter issues or have suggestions for new features, feel free to contribute to the project or contact the developer through the provided repository link.

Enjoy using TwitchBot to enhance your stream's interactivity and make your Twitch community feel involved in the game!

