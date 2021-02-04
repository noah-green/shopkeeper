# Shopkeeper
A Discord bot that uses Google Sheets to help you automate shopping in your online TTRPG.
## How it Works
When you register your guild with Shopkeeper, you will receive a link to a Google Sheet. This is your Marketplace. In your marketplace you add items with names, prices, quanitities and descriptions. These are the items your players will see and 'purchase' in Discord using the Shopkeeper bot. Your items are divided into Shops, which represent different places your players can procure items. These shops can be opened and closed to control access to shopping. On your Marketplace spreadsheet you will also see a Ledger, which records all purchases your players make.
## Commands
### Registration
* **!register <email>**: Registers your guild with Shopkeeper and shares your Marketplace sheet with you.
* **!share <email>**: Shares your Marketplace sheet to another email address.
### Marketplace
* **!market**: This command sends a list of open shops to the channel.
* **!shop <shop>**: starts a shopping session at the specified store in the users Direct Messages using the Shopping cog.
### Shopping
The **Shopping** cog allows players to buy items from a shop. Shopping sessions are started with the **!shop** command, and take place in Direct Messages. Shopping sessions will end after no commands have been sent for a period of time.
* **!status** : Sends a message telling the user where they are shopping, or is no shopping session is active for them.
* **!browse** : Sends a list of the items that are available at the shop, with prices and stock counts.
* **!inspect <item>** Sends a detailed description of the specified item.
* **!buy <item>** : 'Sell' an item  to the player. Shopkeeper does not currently track currency, so this command simply tells the player how much gold to deduct from their character sheet and records the purchase in the ledger.
## Future Features
* **Player Specific Shop Access**: Barbarian banned from the blacksmith for belligerence?
* **Customizable Shopkeeper Messages**: Add some flavor to your bot!
