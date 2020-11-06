from discord.ext import commands
from .model.registry import Registry

class Shopkeeper(commands.Cog):
    """Todo Docstring"""

    def __init__(self, bot):
        self.bot = bot
        self.registry = Registry()
        self.shoppers = {}

    def update_stock_list():
        pass

    @commands.command()
    @commands.guild_only()
    @commands.has_permissions(administrator=True)
    async def register(self, ctx, email):
        """Register a guild and share the market spreadsheet."""
        if self.registry.get_market(ctx.guild):
            await ctx.send('This server is already registered with Shopkeeper.')
            return
        self.registry.create_market(ctx.guild)
        self.registry.share_market(ctx.guild, email)
        await ctx.send('Created a new Market spreadsheet. Check your email!')

    @commands.command()
    @commands.guild_only()
    @commands.has_permissions(administrator=True)
    async def share(self, ctx, email):
        """Share the market spreadsheet."""
        if not self.registry.get_market(ctx.guild):
            await ctx.send('This server is not registered with Shopkeeper.')
            return
        self.registry.share_market(ctx.guild, email)
        await ctx.send(f'Shared the spreadsheet with {email}.')

    @commands.command()
    @commands.guild_only()
    @commands.has_permissions(administrator=True)
    async def open(self, ctx, shop_name):
        """Open the specified shop."""
        if not self.registry.get_market(ctx.guild):
            await ctx.send('This server is not registered with Shopkeeper.')
            return
        try:
            self.registry.get_market(ctx.guild).open_shop(shop_name)
            await ctx.send(f'Successfully opened {shop_name}.')
        except:
            await ctx.send(f'Could not open {shop_name}.')

    @commands.command()
    @commands.guild_only()
    @commands.has_permissions(administrator=True)
    async def close(self, ctx, shop_name):
        """Close the specified shop."""
        if not self.registry.get_market(ctx.guild):
            await ctx.send('This server is not registered with Shopkeeper.')
            return
        try:
            self.registry.get_market(ctx.guild).close_shop(shop_name)
            await ctx.send(f'Successfully closed {shop_name}.')
        except:
            await ctx.send(f'Could not close {shop_name}.')

    @commands.command()
    @commands.guild_only()
    @commands.has_permissions(administrator=True)
    async def openall(self, ctx):
        """Open all shops."""
        if not self.registry.get_market(ctx.guild):
            await ctx.send('This server is not registered with Shopkeeper.')
            return
        self.registry.get_market(ctx.guild).open_all_shops()
        await ctx.send('Opened all shops.')

    @commands.command()
    @commands.guild_only()
    @commands.has_permissions(administrator=True)
    async def closeall(self, ctx, shop_name):
        """Close all shops."""
        if not self.registry.get_market(ctx.guild):
            await ctx.send('This server is not registered with Shopkeeper.')
            return
        self.registry.get_market(ctx.guild).close_all_shops()
        await ctx.send('Closed all shops.')

    @commands.command()
    @commands.guild_only()
    async def market(self, ctx):
        """Report a list of open shops."""
        market = self.registry.get_market(ctx.guild)
        if not market:
            await ctx.send('This server is not registered with Shopkeeper.')
            return
        shop_list = '\n'.join(shop for shop in market.get_open_shops())
        await ctx.send(f"""These shops are open today:\n{shop_list}""")

    @commands.command()
    @commands.guild_only()
    async def shop(self, ctx, shop_name):
        """Start a shopping session at the specified shop."""
        market = self.registry.get_market(ctx.guild)
        if not market:
            await ctx.send('This server is not registered with Shopkeeper.')
            return
        if shop_name not in market.get_shops():
            await ctx.send('That shop is not in the market.')
            return
        if shop_name in market.get_shops() and shop_name not in market.get_open_shops():
            await ctx.send('That shop is not currently open.')
            return
        shop = market.get_shop(shop_name)
        dm = await ctx.author.create_dm()
        stock_message = await dm.send(shop.get_stock_message())
        await stock_message.pin()
        self.shoppers[ctx.author.id] = {
            'shop': shop,
            'stock_message': stock_message,
            'ledger' : market.get_ledger()
        }
        await ctx.send(f'Started a shopping at {shop_name}. Check your DMs!')


    @commands.command()
    @commands.dm_only()
    async def status(self, ctx):
        """Report the user's shopping session status."""
        if not ctx.author.id in self.shoppers:
            await ctx.send('You are not currently shopping anywhere.')
        else:
            shop = self.shoppers[ctx.author.id]['shop'].get_name()
            await ctx.send(f'You are shopping at {shop}.')

    @commands.command()
    @commands.dm_only()
    async def inspect(self, ctx, item_name):
        """View a detailed description of the specified item."""
        if not ctx.author.id in self.shoppers:
            await ctx.send('You are not currently shopping anywhere.')
            return
        try:
            await ctx.send(self.shoppers[ctx.author.id]['shop'].get_description(item_name))
        except ValueError:
            await ctx.send('Sorry, I dont carry that item')


    @commands.command()
    @commands.dm_only()
    async def buy(self, ctx, amount, item_name):
        """Buy the specified number of the specified item."""
        if not ctx.author.id in self.shoppers:
            await ctx.send('You are not currently shopping anywhere.')
            return
        try:
            shop = self.shoppers[ctx.author.id]['shop']
            ledger = self.shoppers[ctx.author.id]['ledger']
            amount = int(amount)
            price = amount * shop.get_price(item_name)
            shop.buy_item(item_name, amount)
            ledger.append_row([ctx.author.name, shop.get_name(), item_name, amount, price])
            await ctx.send(f'Purchased {amount} {item_name}(s)')
        except ValueError:
            await ctx.send('Could not complete purchase')

    @commands.command()
    @commands.dm_only()
    async def end(self, ctx):
        """End the shopping session."""
        del self.shoppers[ctx.author.id]
        await ctx.send('Ended your shopping session.')

def setup(bot):
    bot.add_cog(Shopkeeper(bot))
