from discord.ext import commands

from model import Model

bot = commands.Bot(command_prefix='!')
model = Model()

@bot.event
async def on_ready():
    print(f'logged in as {bot.user}')
