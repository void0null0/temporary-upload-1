import discord
from discord import app_commands
from discord.ext import commands

import json

config = json.load(open('config.json'))

class ping(commands.Cog):
    def __init__(self, bot:commands.Bot) -> None:
        self.bot = bot

    @app_commands.command(
        name = 'ping',
        description = 'Displays the latency of the bot.'
    )
    async def ping(self, interaction:discord.Interaction) -> None:
        embed = discord.Embed(
            color = discord.Color.blurple(),
            description = f'Pong! {round(self.bot.latency * 100)}ms'
        )
        await interaction.response.send_message(embed=embed, ephemeral=True)

async def setup(bot:commands.Bot) -> None:
    await bot.add_cog(
        ping(bot),
        guild = discord.Object(id=config['guild_id'])
    )