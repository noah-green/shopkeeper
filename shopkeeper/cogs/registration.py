from discord.ext import commands

import model.registry as registry

class Registration(commands.Cog):
    """Handle guild registration and administration."""

    def __init__(self, bot):
        self.bot = bot
        self.registry = registry.Registry()

    @commands.command()
    @commands.is_owner()
    async def register(self, ctx, email):
        """Register a guild and share the market spreadsheet."""
        if self.registry.get_market(ctx.guild.id):
            await ctx.send('This server is already registered with Shopkeeper.')
        else:
            self.registry.create_market(ctx.guild.id)
            self.registry.share_market(ctx.guild.id, email)
            await ctx.send('Created a new Market spreadsheet. Check your email!')
