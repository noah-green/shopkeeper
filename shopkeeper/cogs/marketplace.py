from discord.ext import commands

class Marketplace(commands.Cog):
    """Handle"""

    def __init__(self, bot):
        """TODO"""
        self.bot = bot

    @commands.command()
    @commands.is_owner()
    async def open(self, ctx, shop):
        """Open the specified shop."""
        pass

    @commands.command()
    @commands.is_owner()
    async def close(self, ctx, shop):
        """Close the specified shop."""
        pass

    @commands.command()
    @commands.is_owner()
    async def openall(self, ctx):
        """Open all shops."""
        pass

    @commands.command()
    @commands.is_owner()
    async def closeall(self, ctx):
        """Close all shops."""

    @commands.command()
    async def market(self, ctx):
        """Report a list of open shops."""
        pass

    @commands.command()
    async def shop(self, ctx, shop):
        """Start a shopping session at the specified shop"""
        pass
