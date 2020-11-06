import os
import atexit

from discord.ext import commands

import cogs.shopkeeper

bot = commands.Bot(command_prefix='!')

@bot.event
async def on_ready():
    print(f'logged in as {bot.user}')

bot.load_extension('cogs.shopkeeper')

bot.run(os.environ['DISCORD_TOKEN'])
