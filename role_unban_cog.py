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
from player_api.player_api import player_api

class RoleUnBanCog(commands.Cog):
    def __init__(self, bot: discord.Bot):
        self.bot = bot

    @commands.slash_command(name='role_unban', description='Снятие джоббана отдела')
    async def role_unban(self, ctx: discord.ApplicationContext,
                         ckey: Option(str, 'Введите сикей'), # type: ignore
                         department: Option(str, 'Выберите отдел', choices=dict.keys(ROLES))): # type: ignore
        a = await player_api.get_player_info(discord_id=ctx.author.id)
        admin_user_id = a.get("userId")
        async with async_session() as session:
            find_user_i = await session.execute(select(Player.user_id).where(Player.last_seen_user_name == ckey))
            find_user_id = find_user_i.scalar_one_or_none()
            count = 0
            if not find_user_id:
                await ctx.respond('❌ Такого сикея нет.')
                return
            banss = await session.execute(select(Ban).outerjoin(Unban, Ban.server_role_ban_id == Unban.ban_id).where(
                Ban.player_user_id == find_user_id, Unban.ban_id == None,
                # Ban.role_id == ROLES[department
                ))
            bans = banss.scalars()
            for ban in bans:
                if ban.role_id in ROLES[department]:
                    await session.execute(insert(Unban).values(ban_id = ban.server_role_ban_id, unban_time = datetime.datetime.now().isoformat(), unbanning_admin = admin_user_id))
                    count += 1
            await session.commit()
            if count == 0:
                await ctx.respond('❌ Такого джоббана отдела нет.')
                return
            await ctx.respond(f'✅ Джоббан с отдела {department} снят.')
                