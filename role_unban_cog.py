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
from player_api.player_api import PlayerAPIClient

class RoleUnBanCog(commands.Cog):
    def __init__(self, bot: discord.Bot):
        self.bot = bot

    @commands.slash_command(name='role_unban', description='Снятие джоббана отдела')
    async def role_unban(self, ctx: discord.ApplicationContext, 
                         ckey: Option(str, 'Введите сикей'), # type: ignore
                         department: Option(str, 'Выберите отдел', choices=dict.keys(ROLES))): # type: ignore
        username = PlayerAPIClient.get_player_info(Player.player_id, None)
        async with async_session(engine) as session:
            find_user_id = await session.execute(select(Player.user_id).where(Player.last_seen_user_name == ckey)).scalar()
            count = 0
            if not find_user_id:
                await ctx.respond('Такого сикея нет.')
            else:
                bans = await session.execute(select(Ban).outerjoin(Unban, Ban.server_role_ban_id == Unban.ban_id).where(Ban.player_user_id == find_user_id).filter(Unban.ban_id == None)).scalars()
                for ban in bans:
                    if ban.role_id in ROLES[department]:
                        await session.execute(insert(Unban).values(ban_id = ban.server_role_ban_id, unban_time = datetime.datetime.now().isoformat(), unbanning_admin = username))
                        count += 1
                await session.commit()
                if count != 0:
                    await ctx.respond(f'Джоббан с отдела {department} снят.')
                else:
                    await ctx.respond('Такого джоббана нет.')