import discord
from discord.ext import commands
from datetime import datetime

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(intents=intents)

@bot.tree.command(name='role_unban', description='Снятие джоббана')
async def role_unban(intrecation: discord.Interaction, roleban_id: int):
    await intrecation.response.send_message(f'Джоббан {roleban_id} снят.')
    