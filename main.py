import discord
from discord.ext import commands

import json
import os

config = json.load(open('config.json'))

extensions = []
for filename in os.listdir('./cogs'):
    if filename.endswith('.py'):
        extensions.append(f'cogs.{filename[:-3]}')

class MyBot(commands.Bot):
    def __init__(self) -> None:
        super().__init__(
            command_prefix = config['prefix'],
            intents = discord.Intents.all(),
            application_id = config['application_id'],
            help_command = None
        )

    async def setup_hook(self):
        for extension in extensions:
            await self.load_extension(extension)
        await bot.tree.sync(guild=discord.Object(id=config['guild_id']))

bot = MyBot()
bot.run(config['token'])