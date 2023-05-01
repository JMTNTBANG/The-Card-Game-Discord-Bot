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


