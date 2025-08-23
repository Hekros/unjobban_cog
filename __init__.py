from .role_unban_cog import RoleUnBanCog
import os
from dotenv import load_dotenv

load_dotenv()
TOKEN = os.getenv('TOKEN')

def setup(bot):
    bot.add_cog(RoleUnBanCog(bot))
    bot.run(TOKEN)