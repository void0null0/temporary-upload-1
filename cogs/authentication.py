import discord
from discord import app_commands
from discord.ext import commands
from discord.ui import Button, View, Modal, TextInput

from backend.db.models import Users, session, engine
from backend.client.Authentication import Auth

Auth.get_new_cookies()

import json

config = json.load(open('config.json'))
db_session = session(bind=engine)

class Buttons(View):
    @discord.ui.button(label='Login', style=discord.ButtonStyle.green)
    async def login_button_callback(self, interaction:discord.Interaction, button:Button):
        await interaction.response.send_modal(MyModal())

    @discord.ui.button(label='Logout', style=discord.ButtonStyle.danger)
    async def logout_button_callback(self, interaction:discord.Interaction, button:Button):
        view = Buttons()
        user = db_session.query(Users).get({'id' : interaction.user.id})
        db_session.delete(user)
        db_session.commit()
        logout_button = [item for item in view.children if item.label == 'Logout'][0]
        logout_button.disabled = True
        await interaction.response.edit_message(content='Logged out...', view=view)

class MyModal(Modal, title='Login'):
    username = TextInput(label='username', style=discord.TextStyle.short, placeholder='username', required=True, max_length=10)
    password = TextInput(label='password', style=discord.TextStyle.short, placeholder='password', required=True, max_length=10)
    async def on_submit(self, interaction:discord.Interaction) -> None:
        view = Buttons()
        db_session.add(Users(
            id = interaction.user.id,
            cookie = f'{self.username} {self.password}',
            json = dict({'x' : 1})
        ))
        db_session.commit()
        login_button = [item for item in view.children if item.label == 'Login'][0]
        login_button.disabled = True
        await interaction.response.edit_message(content='Logged in...', view=view)

class Authentication(commands.Cog):
    def __init__(self, bot:commands.Bot) -> None:
        self.bot = bot

    @app_commands.command(
        name = 'authentication',
        description = 'Login/Logout with your riot account'
    )
    async def authentication(self, interaction:discord.Interaction) -> None:
        view = Buttons()
        user = db_session.query(Users).get({'id' : interaction.user.id})
        login_button = [item for item in view.children if item.label == 'Login'][0]
        logout_button = [item for item in view.children if item.label == 'Logout'][0]
        if user == None:
            logout_button.disabled = True
        else:
            login_button.disabled = True
        await interaction.response.send_message(content='test', view=view, ephemeral=True)

async def setup(bot:commands.Bot) -> None:
    await bot.add_cog(
        Authentication(bot),
        guild = discord.Object(id=config['guild_id'])
    )