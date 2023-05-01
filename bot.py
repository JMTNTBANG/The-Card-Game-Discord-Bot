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
        for guild in client.guilds:
            bot.guilds.append(Guild(guild))
        pass

    client.run(token)
