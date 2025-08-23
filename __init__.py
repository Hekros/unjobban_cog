from role_unban_cog import RoleUnBanCog
import os
from dotenv import load_dotenv

def setup(bot):
    bot.add_cog(RoleUnBanCog(bot))