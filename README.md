# Shopkeeper
A Discord bot that uses Google Sheets to help you automate shopping in your online TTRPG.
## How it Works
When you register your guild with Shopkeeper, you will receive a link to a Google Sheet. This is your Marketplace. In your marketplace you add items with names, prices, quanitities and descriptions. These are the items your players will see and 'purchase' using the Shopkeeper bot. Your items are divided into Shops, which represent different places your players can procure items. These shops can be opened and closed depending on where your players have access to
## Cogs
### Registration
The **Registration** cog sets up your guild with Shopkeeper. All of its commands are owner only.
* **!register <email>**: Registers your guild with Shopkeeper and shares your Marketplace sheet with you.
* **!share <email>**: Shares your Marketplace sheet to another email address.
* **!reset**: Replace your Marketplace document with a fresh one. This will delete all data that you don't have saved somewhere else, so be careful!  
### Marketplace
The **Marketplace** cog lives in a public channel lives in a public channel and manages your shops, as well as sending updates when a player makes a purchase.
* **!open <shop>**: Opens the specified shop for the players to access. This command is owner only.
* **!close <shop>**: Closes the specified shop for player access. This command is owner only.
* **!market**: This command sends a list of open shops to the channel.
* **!shop <shop>**: starts a shopping session at the specified store in the users Direct Messages using the Shopping cog.
### Shopping
The **Shopping** cog allows players to buy items from a shop. Shopping sessions are started with the **!shop** command, and take place in Direct Messages. Shopping sessions will end after no commands have been sent for a period of time.
* **!status** : Sends a message telling the user where they are shopping, or is no shopping session is active for them.
* **!browse** : Sends a list of the items that are available at the shop, with prices and stock counts.
* **!inspect <item>** Sends a detailed description of the specified item.
* **!buy <item>** : 'Sell' an item  to the player. Shopkeeper does not currently track currency, so what this currently does is tell the player how much currency to deduct from their character sheet and send an update to the Marketplace channel that they have bought the item.
* **!buysecret <item>**: Allows a player to purchase an item without sending an update to the marketplace channel. Instead, it will send a direct message update to the owner. There are no secrets from the Dungeon Master...
## Future Features
* **Player Specific Shop Access**: Barbarian banned from the blacksmith for belligerence?
* **Customizable Shopkeeper Messages**: Add some flavor to your bot!
