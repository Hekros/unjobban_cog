from .role_unban_cog import RoleUnBanCog

def setup(bot):
    bot.add_cog(RoleUnBanCog(bot))