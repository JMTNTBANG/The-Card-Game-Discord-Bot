import discord
from dotenv import load_dotenv
import os
load_dotenv()
token = os.getenv('TOKEN')

''' 
Game Types:
0: UNO
'''


class Bot:
    def __init__(self):
        self.guilds = []


class Guild:
    def __init__(self, guild: discord.Guild):
        self.games = []
        self.guild = guild


class Game:
    def __init__(self, game_type: int, leader: discord.Member):
        self.game_type = game_type
        self.pending = True
        self.leader = leader
        if game_type == 0:
            self.game = uno.Game()


intents = discord.Intents.default()
intents.guilds = True
intents.members = True
intents.message_content = True
client = discord.Client(intents=intents)
commands = discord.app_commands.CommandTree(client)
command_list = []
bot = Bot()
def run():
    @client.event
    async def on_ready():
        for command in os.listdir('commands'):
            if command.endswith('py'):
                if '__init__.py' not in command:
                    if 'template.py' not in command:
                        if command not in command_list:
                            exec(f'import commands.{command[:-3]}')
                            exec(
                                f'commands.{command[:-3]}.import_command()')
                            command_list.append(command)
        await commands.sync()
        for guild in client.guilds:
            bot.guilds.append(Guild(guild))
        pass

    client.run(token)
