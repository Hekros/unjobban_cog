import os
import discord
from dotenv import load_dotenv
from role_unban_cog import RoleUnBanCog

intents = discord.Intents.default()
intents.members = True
intents.messages = True

bot = discord.Bot(intents=intents)

load_dotenv()
TOKEN = os.getenv('TOKEN')

for dir in os.listdir('./cogs'):
    bot.load_extension(f"cogs.{dir}")
bot.run(TOKEN)