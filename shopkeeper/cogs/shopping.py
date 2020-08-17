from discord.ext import commands

class Shopping(commands.Cog):
    def __init__(self):
        self.sessions = {}

    @commands.command()
    @commands.dm_only()
    def status(self, ctx):
        if not ctx.user.id in self.sessions:
            ctx.send('You are not currently shopping anywhere.')
