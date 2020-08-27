from discord.ext import commands

class Shopping(commands.Cog):
    """Manage shopping sessions and handle commands."""

    def __init__(self, bot):
        self.bot = bot
        self.sessions = {}

    @commands.command()
    @commands.dm_only()
    async def status(self, ctx):
        """Report status of user's shopping session."""
        if not ctx.author.id in self.sessions:
            await ctx.send('You are not currently shopping anywhere.')
        else:
            await ctx.send('You are shopping somewhere.')

    @commands.command()
    @commands.dm_only()
    async def browse(self, ctx):
        """Report avaliable items for the user's shopping session."""
        if not ctx.author.id in self.sessions:
            await ctx.send('You are not currently shopping anywhere.')
        else:
            shop = self.sessions[ctx.author.id]['shop']

    @commands.command()
    @commands.dm_only()
    async def inspect(self, ctx, item):
        """Report detailed description for the given item."""
        if not ctx.author.id in self.sessions:
            await ctx.send('You are not currently shopping anywhere.')
            return
        shop = self.sessions[ctx.author.id]['shop']

    @commands.command()
    @commands.dm_only()
    async def buy(self, ctx, item):
        """Deduct the item the player has purchased from stock counts."""
        if not ctx.author.id in self.sessions:
            await ctx.send('You are not currently shopping anywhere.')
        else:
            shop = self.sessions[ctx.author.id]['shop']
