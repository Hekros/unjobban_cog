import discord
from discord.ext import commands
from datetime import datetime
from data import *

class RoleUnBanCog(commands.Cog):
    def __init__(self, bot: discord.Bot):
        self.bot = bot
        
    @commands.slash_command(name='role_unban', description='Снятие джоббана')
    async def role_unban(self, ctx: discord.ApplicationContext, roleban_id: int):
        username = ctx.author.name
        with Session(engine) as session:
            # Ищу строку с подходящим айди джоббана
            row = session.query(Ban).filter(Ban.server_role_ban_id == roleban_id).first()
            exists = session.query(Unban).filter(Unban.role_unban_id == roleban_id).first()
            if row and not exists:
                # Записываю эту строку в таблицу анбана
                new_row = Unban(role_unban_id=roleban_id, ban_id=roleban_id, unban_time=datetime.now().isoformat(), unbanning_admin=username)
                session.add(new_row)
                session.commit()
                await ctx.respond(f'Джоббан {roleban_id} снят.')
            if not row: 
                await ctx.respond('Такого джоббана нет.')
            if exists:
                await ctx.respond('Этот джоббан уже снят.')
