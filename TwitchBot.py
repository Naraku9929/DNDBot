import random
import json
import tkinter as tk
import threading
import asyncio
from twitchio.ext import commands
# pip install -r requirements.txt

class Bot(commands.Bot):

    def __init__(self, token, channel, roll_enabled, npc_enabled, loot_enabled, room_enabled, class_enabled, race_enabled, monster_enabled, trap_enabled):
        super().__init__(
            token=token,
            prefix='!',
            initial_channels=[channel]
        )
        self.roll_enabled = roll_enabled
        self.npc_enabled = npc_enabled
        self.loot_enabled = loot_enabled
        self.room_enabled = room_enabled
        self.class_enabled = class_enabled
        self.race_enabled = race_enabled
        self.monster_enabled = monster_enabled
        self.trap_enabled = trap_enabled
        self.rolls = []
        self.npcs = []
        self.loots = []
        self.rooms = []
        self.classes = []
        self.races = []
        self.monsters = []
        self.traps = []
        
        self.room_types = [
            "Throne Room", "Dungeon Cell", "Armory","Library", "Great Hall", "Torture Chamber", "Guard Barracks", "Kitchen", "Ballroom", "Alchemist's Laboratory", "Wizard's Study", "Treasury", "Chapel", "Barracks", "War Room", "Servants' Quarters", "Storage Room", "Hidden Chamber", "Garden Atrium", "Secret Passage", "Scrying Room", "Guest Room", "Stable", "Banquet Hall", "Crypt", "Observatory", "Potion Room", "Music Chamber", "Trophy Room", "Training Ground", "Healer's Room", "Map Room", "Thieves' Guild Hideout", "Hallway", "Narrow Passage", "Dead End", "Collapsed Tunnel", "Abandoned Room", "Partially Flooded Room", "Ruined Chapel", "Secret Corridor", "Hidden Alcove", "Crumbled Stairwell", "Broken Bridge", "Dark Alcove", "Blocked Passage", "Trap-Laden Corridor", "Storage Nook", "Collapsed Ceiling Room", "Old Well Room", "Secret Dead End with False Door", "Half-Destroyed Throne Room", "Ransacked Library"
        ]
        # Add more room types if desired

        self.class_types = [
            "Barbarian", "Bard", "Cleric", "Druid", "Fighter", "Monk", "Paladin", "Ranger", "Rogue", "Sorcerer", "Warlock", "Wizard"
        ]
        # Add more class types if desired
        
        self.race_types = [
            "Human", "Elf", "Dwarf", "Halfling", "Dragonborn", "Gnome", "Half-Elf", "Half-Orc", "Tiefling"
        ]
        # Add more Race types if desired
        
        self.monster_types = [
            "Dragon", "Goblin", "Orc", "Troll", "Skeleton", "Zombie", "Vampire", "Werewolf", 
            "Basilisk", "Chimera", "Hydra", "Manticore", "Minotaur", "Phoenix", "Unicorn",
            "Banshee", "Demon", "Devil", "Ghost", "Lich", "Mind Flayer", "Beholder",
            "Giant Spider", "Owlbear", "Rust Monster", "Gelatinous Cube", "Mimic", "Displacer Beast"
        ]
        # Add more monster types if desired

        self.trap_types = [
            "Pit Trap", "Poison Dart", "Swinging Blade", "Spike Trap", "Rolling Boulder", 
            "Fire Trap", "Acid Spray", "Crushing Ceiling", "Arrow Volley", "Magic Runes",
            "Lightning Bolt", "Net Trap", "Gas Trap", "Flooding Room", "Falling Cage",
            "Frost Trap", "Blade Wall", "Trapdoor", "Collapsing Floor", "Mirror Trap",
            "Teleportation Trap", "Illusion Trap", "Fireball Trap", "Web Trap", "Mind Control Runes"
        ]
        # Add more trap types if desired

    async def event_ready(self):
        bot_name = "MyBotName"  # Replace with your desired bot name
        print(f'Logged in as | {bot_name}')

    @commands.command(name='roll')
    async def roll(self, ctx):
        if self.roll_enabled:
            roll_result = random.randint(1, 20)
            self.rolls.append((ctx.author.name, roll_result))
            await ctx.send(f'@{ctx.author.name}, you rolled a {roll_result}!')

    @commands.command(name='npc')
    async def npc(self, ctx):
        if self.npc_enabled:
            npc_name = ctx.message.content[len('!npc '):].strip()
            self.npcs.append((ctx.author.name, npc_name))
            await ctx.send(f'The Twitch Chat God @{ctx.author.name} is sommoning there power to add {npc_name} to the realm!')

    @commands.command(name='loot')
    async def loot(self, ctx):
        if self.loot_enabled:
            loot_item = ctx.message.content[len('!loot '):].strip()
            self.loots.append((ctx.author.name, loot_item))
            await ctx.send(f'The Twitch Chat God @{ctx.author.name} is sommoning there power to add {loot_item} to the realm!')

    @commands.command(name='room')
    async def room(self, ctx):
        if self.room_enabled:
            room_choice = ctx.message.content[len('!room '):].strip()
            if room_choice:
                if room_choice.title() in self.room_types:
                    self.rooms.append((ctx.author.name, room_choice.title()))
                    await ctx.send(f'The Twitch Chat God @{ctx.author.name} is sommoning there power for a {room_choice.title()}!')
                else:
                    await ctx.send(f'@{ctx.author.name}, you do not have enough power to place that in this dungeon! Available rooms: {", ".join(self.room_types)}')
            else:
                room_choice = random.choice(self.room_types)
                self.rooms.append((ctx.author.name, room_choice))
                await ctx.send(f'The Twitch Chat God @{ctx.author.name} is making a {room_choice}!')

    @commands.command(name='class')
    async def dnd_class(self, ctx):
        if self.class_enabled:
            class_choice = ctx.message.content[len('!class '):].strip()
            if class_choice:
                if class_choice.title() in self.class_types:
                    self.classes.append((ctx.author.name, class_choice.title()))
                    await ctx.send(f'The Twitch Chat God @{ctx.author.name} is trying to change that persons class to {class_choice.title()}!')
                else:
                    await ctx.send(f'@{ctx.author.name}, you do not have enough power to make them that class! Available classes: {", ".join(self.class_types)}')
            else:
                class_choice = random.choice(self.class_types)
                self.classes.append((ctx.author.name, class_choice))
                await ctx.send(f'The Twitch Chat God @{ctx.author.name}, has changed that persons class to {class_choice}!')

    @commands.command(name='race')
    async def dnd_race(self, ctx):
        if self.race_enabled:
            race_choice = ctx.message.content[len('!race '):].strip()
            if race_choice:
                if race_choice.title() in self.race_types:
                    self.races.append((ctx.author.name, race_choice.title()))
                    await ctx.send(f'The Twitch Chat God @{ctx.author.name}, is trying to change that persons Race to {race_choice.title()}!')
                else:
                    await ctx.send(f'@{ctx.author.name}, you do not have enough power to make them that Race! Available races: {", ".join(self.race_types)}')
            else:
                race_choice = random.choice(self.race_types)
                self.races.append((ctx.author.name, race_choice))
                await ctx.send(f'The Twitch Chat God @{ctx.author.name}, makes that person a {race_choice}!')

    @commands.command(name='monster')
    async def monster(self, ctx):
        if self.monster_enabled:
            monster_choice = ctx.message.content[len('!monster '):].strip()
            if monster_choice:
                if monster_choice.title() in self.monster_types:
                    self.monsters.append((ctx.author.name, monster_choice.title()))
                    await ctx.send(f'The Twitch Chat God @{ctx.author.name} is sommoning there power for a {monster_choice.title()}!')
                else:
                    await ctx.send(f'@{ctx.author.name}, sorry that monster is sleeping! Available monsters: {", ".join(self.monster_types)}')
            else:
                monster_choice = random.choice(self.monster_types)
                self.monsters.append((ctx.author.name, monster_choice))
                await ctx.send(f'The Twitch Chat God @{ctx.author.name} is Sommoning a {monster_choice}!')

    @commands.command(name='trap')
    async def trap(self, ctx):
        if self.trap_enabled:
            trap_choice = ctx.message.content[len('!trap '):].strip()
            if trap_choice:
                if trap_choice.title() in self.trap_types:
                    self.traps.append((ctx.author.name, trap_choice.title()))
                    await ctx.send(f'The Twitch Chat God @{ctx.author.name} is sommoning there power for a {trap_choice.title()}!')
                else:
                    await ctx.send(f'@{ctx.author.name}, that flat pack trap kit is missing a part! Available traps: {", ".join(self.trap_types)}')
            else:
                trap_choice = random.choice(self.trap_types)
                self.traps.append((ctx.author.name, trap_choice))
                await ctx.send(f'The Twitch Chat God @{ctx.author.name} is making a {trap_choice}!')

    @commands.command(name='dndhelp')
    async def dndhelp(self, ctx):
        help_message = (
            "Available commands: \n"
            "!roll - Roll a 20-sided die. \n"
            "!npc <name> - Add an NPC with the given name. \n"
            "!loot <item> - Add loot with the given item name. \n"
            "!room [name] - Discover a random room or specify one to find! \n"
            "!class [name] - Get assigned a random class or choose one! \n"
            "!race [name] - Get assigned a random race or choose one! \n"
            "!monster [name] - Encounter a random monster or specify one! \n"
            "!trap [name] - Trigger a random trap or specify one!"
        )
        await ctx.send(help_message)

    async def pick_roll_winner(self):
        if self.rolls:
            winner = random.choice(self.rolls)
            await self.connected_channels[0].send(f'The winner is @{winner[0]} with a roll of {winner[1]}!')
        else:
            await self.connected_channels[0].send('No rolls have been recorded yet.')

    async def pick_npc_winner(self):
        if self.npcs:
            winner = random.choice(self.npcs)
            await self.connected_channels[0].send(f'The Twitch Chat God @{winner[0]}! Spwans an NPCs Named {winner[1]}.')
        else:
            await self.connected_channels[0].send('No NPC names have been recorded yet.')

    async def pick_loot_winner(self):
        if self.loots:
            winner = random.choice(self.loots)
            await self.connected_channels[0].send(f'The Twitch Chat God @{winner[0]}! Spawns a {winner[1]}.')
        else:
            await self.connected_channels[0].send('No loot items have been recorded yet.')

    async def pick_room_winner(self):
        if self.rooms:
            winner = random.choice(self.rooms)
            await self.connected_channels[0].send(f'The Twitch Chat God @{winner[0]}! makes a {winner[1]}.')
        else:
            await self.connected_channels[0].send('No rooms have been recorded yet.')

    async def pick_class_winner(self):
        if self.classes:
            winner = random.choice(self.classes)
            await self.connected_channels[0].send(f'The Twitch Chat God @{winner[0]} uses their power and changes that persons a {winner[1]}.')
        else:
            await self.connected_channels[0].send('No classes have been recorded yet.')

    async def pick_race_winner(self):
        if self.races:
            winner = random.choice(self.races)
            await self.connected_channels[0].send(f'The Twitch Chat God @{winner[0]} uses their power and changes that persons a {winner[1]}.')
        else:
            await self.connected_channels[0].send('No races have been recorded yet.')

    async def pick_monster_winner(self):
        if self.monsters:
            winner = random.choice(self.monsters)
            await self.connected_channels[0].send(f'The Twitch Chat God @{winner[0]}! Sommons a {winner[1]}!')
        else:
            await self.connected_channels[0].send('No monsters have been encountered yet.')

    async def pick_trap_winner(self):
        if self.traps:
            winner = random.choice(self.traps)
            await self.connected_channels[0].send(f'The Twitch Chat God @{winner[0]}! Makes a {winner[1]}!')
        else:
            await self.connected_channels[0].send('No traps have been triggered yet.')

def save_config():
    token = token_entry.get()
    if token == '*' * len(existing_token) and existing_token:
        token = existing_token
    channel = channel_entry.get()
    roll_enabled = roll_var.get()
    npc_enabled = npc_var.get()
    loot_enabled = loot_var.get()
    room_enabled = room_var.get()
    class_enabled = class_var.get()
    race_enabled = race_var.get()
    monster_enabled = monster_var.get()
    trap_enabled = trap_var.get()
    config = {
        'OAUTH_TOKEN': token, 
        'CHANNEL_NAME': channel, 
        'ROLL_ENABLED': roll_enabled, 
        'NPC_ENABLED': npc_enabled, 
        'LOOT_ENABLED': loot_enabled, 
        'ROOM_ENABLED': room_enabled, 
        'CLASS_ENABLED': class_enabled, 
        'RACE_ENABLED': race_enabled,
        'MONSTER_ENABLED': monster_enabled,
        'TRAP_ENABLED': trap_enabled
    }
    with open('config.json', 'w') as config_file:
        json.dump(config, config_file)

def connect_to_twitch():
    def run_bot():
        try:
            with open('config.json', 'r') as config_file:
                config = json.load(config_file)
            token = config.get('OAUTH_TOKEN')
            channel = config.get('CHANNEL_NAME')
            roll_enabled = config.get('ROLL_ENABLED', False)
            npc_enabled = config.get('NPC_ENABLED', False)
            loot_enabled = config.get('LOOT_ENABLED', False)
            room_enabled = config.get('ROOM_ENABLED', False)
            class_enabled = config.get('CLASS_ENABLED', False)
            race_enabled = config.get('RACE_ENABLED', False)
            monster_enabled = config.get('MONSTER_ENABLED', False)
            trap_enabled = config.get('TRAP_ENABLED', False)
            if token and channel:
                asyncio.set_event_loop(asyncio.new_event_loop())
                global bot
                bot = Bot(token, channel, roll_enabled, npc_enabled, loot_enabled, room_enabled, 
                         class_enabled, race_enabled, monster_enabled, trap_enabled)
                bot.run()
        except FileNotFoundError:
            print("Config file not found. Please save the config first.")

    bot_thread = threading.Thread(target=run_bot)
    bot_thread.daemon = True
    bot_thread.start()

def pick_roll_winner():
    if bot:
        asyncio.run_coroutine_threadsafe(bot.pick_roll_winner(), bot.loop)

def pick_npc_winner():
    if bot:
        asyncio.run_coroutine_threadsafe(bot.pick_npc_winner(), bot.loop)

def pick_loot_winner():
    if bot:
        asyncio.run_coroutine_threadsafe(bot.pick_loot_winner(), bot.loop)

def pick_room_winner():
    if bot:
        asyncio.run_coroutine_threadsafe(bot.pick_room_winner(), bot.loop)

def pick_class_winner():
    if bot:
        asyncio.run_coroutine_threadsafe(bot.pick_class_winner(), bot.loop)

def pick_race_winner():
    if bot:
        asyncio.run_coroutine_threadsafe(bot.pick_race_winner(), bot.loop)

def pick_monster_winner():
    if bot:
        asyncio.run_coroutine_threadsafe(bot.pick_monster_winner(), bot.loop)

def pick_trap_winner():
    if bot:
        asyncio.run_coroutine_threadsafe(bot.pick_trap_winner(), bot.loop)

# GUI Setup
root = tk.Tk()
root.title("Twitch Bot Config")

# Load existing config if available
try:
    with open('config.json', 'r') as config_file:
        config = json.load(config_file)
        existing_token = config.get('OAUTH_TOKEN', '')
        existing_channel = config.get('CHANNEL_NAME', '')
        existing_roll_enabled = config.get('ROLL_ENABLED', False)
        existing_npc_enabled = config.get('NPC_ENABLED', False)
        existing_loot_enabled = config.get('LOOT_ENABLED', False)
        existing_room_enabled = config.get('ROOM_ENABLED', False)
        existing_class_enabled = config.get('CLASS_ENABLED', False)
        existing_race_enabled = config.get('RACE_ENABLED', False)
        existing_monster_enabled = config.get('MONSTER_ENABLED', False)
        existing_trap_enabled = config.get('TRAP_ENABLED', False)
except FileNotFoundError:
    existing_token = ''
    existing_channel = ''
    existing_roll_enabled = False
    existing_npc_enabled = False
    existing_loot_enabled = False
    existing_room_enabled = False
    existing_class_enabled = False
    existing_race_enabled = False
    existing_monster_enabled = False
    existing_trap_enabled = False

# Labels and Entries for Token and Channel
tk.Label(root, text="OAuth Token:").grid(row=0, column=0, padx=10, pady=5)
token_entry = tk.Entry(root, width=40)
if existing_token:
    token_entry.insert(0, '*' * len(existing_token))
token_entry.grid(row=0, column=1, padx=10, pady=5)

tk.Label(root, text="Channel Name:").grid(row=1, column=0, padx=10, pady=5)
channel_entry = tk.Entry(root, width=40)
channel_entry.insert(0, existing_channel)
channel_entry.grid(row=1, column=1, padx=10, pady=5)

# Checkbox to Enable Roll Command
roll_var = tk.BooleanVar(value=existing_roll_enabled)
roll_checkbox = tk.Checkbutton(root, text="Enable Roll Command", variable=roll_var)
roll_checkbox.grid(row=2, column=0, pady=5)

# Button to Pick Roll Winner
tk.Button(root, text="Pick Roll Winner", command=pick_roll_winner).grid(row=2, column=1, pady=5)

# Checkbox to Enable NPC Command
npc_var = tk.BooleanVar(value=existing_npc_enabled)
npc_checkbox = tk.Checkbutton(root, text="Enable NPC Command", variable=npc_var)
npc_checkbox.grid(row=3, column=0, pady=5)

# Button to Pick NPC Winner
tk.Button(root, text="Pick NPC Winner", command=pick_npc_winner).grid(row=3, column=1, pady=5)

# Checkbox to Enable Loot Command
loot_var = tk.BooleanVar(value=existing_loot_enabled)
loot_checkbox = tk.Checkbutton(root, text="Enable Loot Command", variable=loot_var)
loot_checkbox.grid(row=4, column=0, pady=5)

# Button to Pick Loot Winner
tk.Button(root, text="Pick Loot Winner", command=pick_loot_winner).grid(row=4, column=1, pady=5)

# Checkbox to Enable Room Command
room_var = tk.BooleanVar(value=existing_room_enabled)
room_checkbox = tk.Checkbutton(root, text="Enable Room Command", variable=room_var)
room_checkbox.grid(row=5, column=0, pady=5)

# Button to Pick Room Winner
tk.Button(root, text="Pick Room Winner", command=pick_room_winner).grid(row=5, column=1, pady=5)

# Checkbox to Enable Class Command
class_var = tk.BooleanVar(value=existing_class_enabled)
class_checkbox = tk.Checkbutton(root, text="Enable Class Command", variable=class_var)
class_checkbox.grid(row=6, column=0, pady=5)

# Button to Pick Class Winner
tk.Button(root, text="Pick Class Winner", command=pick_class_winner).grid(row=6, column=1, pady=5)

# Checkbox to Enable Race Command
race_var = tk.BooleanVar(value=existing_race_enabled)
race_checkbox = tk.Checkbutton(root, text="Enable Race Command", variable=race_var)
race_checkbox.grid(row=7, column=0, pady=5)

# Button to Pick Race Winner
tk.Button(root, text="Pick Race Winner", command=pick_race_winner).grid(row=7, column=1, pady=5)

# Checkbox to Enable Monster Command
monster_var = tk.BooleanVar(value=existing_monster_enabled)
monster_checkbox = tk.Checkbutton(root, text="Enable Monster Command", variable=monster_var)
monster_checkbox.grid(row=8, column=0, pady=5)

# Button to Pick Monster Winner
tk.Button(root, text="Pick Monster Winner", command=pick_monster_winner).grid(row=8, column=1, pady=5)

# Checkbox to Enable Trap Command
trap_var = tk.BooleanVar(value=existing_trap_enabled)
trap_checkbox = tk.Checkbutton(root, text="Enable Trap Command", variable=trap_var)
trap_checkbox.grid(row=9, column=0, pady=5)

# Button to Pick Trap Winner
tk.Button(root, text="Pick Trap Winner", command=pick_trap_winner).grid(row=9, column=1, pady=5)

# Buttons to Save Config and Connect to Twitch
tk.Button(root, text="Save Config", command=save_config).grid(row=10, column=0, columnspan=2, pady=10)
tk.Button(root, text="Connect to Twitch", command=connect_to_twitch).grid(row=11, column=0, columnspan=2, pady=10)

root.mainloop()