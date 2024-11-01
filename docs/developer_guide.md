**Developer Guide for TwitchBot**

### Overview

This guide is intended for developers who want to modify or extend TwitchBot. The bot is designed to be modular and easy to enhance, with various sections that can be freely edited to customize its functionality. Below, we outline the different parts of the codebase and provide tips for making changes.

### Areas You Can Freely Edit

1. **Commands and Features**
   - **File**: `TwitchBot.py`
   - **Section**: Command Definitions (`@commands.command` functions)
   - **Description**: You can add new commands or modify existing ones by editing the functions decorated with `@commands.command`. Each function defines how the bot responds to a specific command from chat.
   - **Example**: To add a new command, you can define a function like:
     ```python
     @commands.command(name='greet')
     async def greet(self, ctx):
         await ctx.send(f'Hello, @{ctx.author.name}!')
     ```
   - **Tips**: Ensure that each command has a unique name to avoid conflicts and that it follows the overall tone and functionality of the bot.

2. **Pre-Populated Lists**
   - **File**: `TwitchBot.py`
   - **Section**: Class Attributes (e.g., `self.room_types`, `self.class_types`, `self.race_types`)
   - **Description**: You can add or remove entries from pre-populated lists, such as room types, classes, races, monsters, or traps. These lists are used by the bot to generate responses for commands like `!room`, `!class`, or `!monster`.
   - **Example**: To add a new monster to the list:
     ```python
     self.monster_types.append('Golem')
     ```
   - **Tips**: Ensure that the items added are relevant to your stream’s theme to maintain immersion.

3. **Configuration Settings**
   - **File**: `config.json`
   - **Section**: Bot Settings
   - **Description**: The `config.json` file stores the configuration details like OAuth token, channel name, and enabled features. You can edit this file to change how the bot behaves or which features are enabled by default.
   - **Tips**: Changes can also be made through the GUI, but editing `config.json` directly can be more efficient if you need to make bulk updates.

4. **Graphical User Interface (GUI)**
   - **File**: `TwitchBot.py`
   - **Section**: GUI Setup (`tk.Tk()` and related components)
   - **Description**: You can modify the GUI to add new settings or change the layout. The GUI is built using the `tkinter` library and provides an interface for configuring the bot.
   - **Example**: To add a new checkbox for enabling/disabling a custom feature:
     ```python
     custom_feature_var = tk.BooleanVar(value=False)
     custom_feature_checkbox = tk.Checkbutton(root, text="Enable Custom Feature", variable=custom_feature_var)
     custom_feature_checkbox.grid(row=10, column=0, pady=5)
     ```
   - **Tips**: Keep the GUI simple and intuitive, focusing on ease of use for streamers who may not be technically inclined.

5. **Event Handling**
   - **File**: `TwitchBot.py`
   - **Section**: Event Methods (`async def event_ready(self)`)
   - **Description**: You can add new event handlers or modify existing ones to customize how the bot reacts to Twitch events (e.g., when it connects to the channel).
   - **Example**: Modify the `event_ready` function to send a custom welcome message when the bot goes live:
     ```python
     async def event_ready(self):
         print(f'Logged in as | {self.nick}')
         await self.connected_channels[0].send('The bot is now online! Let the games begin!')
     ```
   - **Tips**: Be cautious when modifying core events, as they are critical for the bot’s functionality.

6. **Adding Custom Features**
   - **File**: `TwitchBot.py`
   - **Section**: Bot Initialization (`__init__` method)
   - **Description**: You can introduce new features by adding new attributes and methods to the bot class. This allows you to expand the bot's capabilities beyond the existing features.
   - **Example**: To add a new feature for weather information:
     ```python
     self.weather_enabled = True

     @commands.command(name='weather')
     async def weather(self, ctx, location):
         # Add logic to fetch weather data for the given location
         await ctx.send(f'The current weather in {location} is Sunny, 25°C.')
     ```
   - **Tips**: Keep new features modular by encapsulating them in separate methods or helper functions to make the code easier to maintain.

### Guidelines for Modifications

- **Keep it Modular**: When adding new features, try to create separate methods or classes to keep the code organized and easy to understand.
- **Follow Naming Conventions**: Use descriptive and consistent names for commands, variables, and functions.
- **Error Handling**: Add appropriate error handling to commands, particularly when interacting with user input or external APIs.
- **Testing**: Test changes thoroughly in a private Twitch channel before deploying them in a live stream to ensure they work as expected without disrupting the viewer experience.

### Example Enhancements

- **Custom Commands**: Add commands that reflect the theme of the game or stream (e.g., `!spell <name>` for magic spells).
- **Interactive Mini-Games**: Create small interactive games that viewers can play directly in chat (e.g., `!riddle` to solve puzzles).
- **Integrate with APIs**: Use external APIs to enhance functionality, such as adding a `!weather` command using a weather API or a `!crypto` command to get cryptocurrency prices.

### Summary

This developer guide provides an overview of the different areas of TwitchBot that can be freely modified to add new functionality or customize the bot for specific needs. By understanding the command structure, pre-populated lists, configuration settings, and the GUI, developers can easily expand the capabilities of TwitchBot to better serve the community and keep viewers engaged.

Happy coding, and may your TwitchBot bring endless fun to your streams!

