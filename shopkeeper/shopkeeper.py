import os
import atexit

from discord.ext import commands

import cogs

bot = commands.Bot(command_prefix='!')

@bot.event
async def on_ready():
    print(f'logged in as {bot.user}')

bot.add_cog(cogs.Registration(bot))
bot.add_cog(cogs.Marketplace(bot))
bot.add_cog(cogs.Shopping(bot))

bot.run(os.environ['DISCORD_TOKEN'])
