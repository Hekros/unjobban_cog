import discord
from discord import Option
from discord.ext import commands
from datetime import datetime
from sqlalchemy import select
from .data import *
from sqlalchemy.orm import Session
from sqlalchemy import insert
import datetime
from .roles import ROLES

class RoleUnBanCog(commands.Cog):
    def __init__(self, bot: discord.Bot):
        self.bot = bot
    def get_ckeys():
        a = []
        with Session(engine) as session:
            results = session.execute(select(Player.last_seen_user_name)).scalars()
            for result in results:
                a.append(result)
            return a

    @commands.slash_command(name='role_unban', description='Снятие джоббана')
    async def role_unban(self, ctx: discord.ApplicationContext, 
                         ckey: Option(str, 'Введите сикей', choices=get_ckeys()), # type: ignore
                         department: Option(str, 'Выберите отдел', choices=dict.keys(ROLES))): # type: ignore
        username = ctx.author.name
        with Session(engine) as session:
            find_user_id = session.execute(select(Player.user_id).where(Player.last_seen_user_name == ckey)).scalar()
            bans = session.execute(select(Ban).outerjoin(Unban, Ban.server_role_ban_id == Unban.ban_id).where(Ban.player_user_id == find_user_id).filter(Unban.ban_id == None)).scalars()
            count = 0
            for ban in bans:
                find_role_id = ban.role_id
                if ban.role_id in ROLES[department]:
                    session.execute(insert(Unban).values(ban_id = ban.server_role_ban_id, unban_time = datetime.datetime.now().isoformat(), unbanning_admin = username))
                    count += 1
            session.commit()
            if count != 0:
                await ctx.respond(f'Джоббан с игрока {ckey} снят.')
            else:
                await ctx.respond('Такого джоббана нет.')