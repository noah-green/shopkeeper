import os
from discord.ext import commands

bot = commands.Bot(command_prefix='!')

@bot.event
async def on_ready():
    print(f'logged in as {bot.user}')

bot.add_cog(commands.Shopping(bot))

bot.run(os.environ['DISCORD_TOKEN'])
