from sqlalchemy import select
from data import *
from sqlalchemy.orm import Session
from roles import ROLES
from typing import Optional, Dict, Any
from player_api.player_api import player_api
import asyncio
# with Session(engine) as session:
#     find_user_id = session.execute(select(Player.user_id).where(Player.last_seen_user_name == ckey)).scalar()
#     bans = session.execute(select(Ban).outerjoin(Unban, Ban.server_role_ban_id == Unban.ban_id).where(Ban.player_user_id == find_user_id).filter(Unban.ban_id == None)).scalars()
#     count = 0
#     # find_role_id = session.execute(select(Ban.role_id).where(Player.user_id == find_user_id)).all()
#     for ban in bans:
#         find_role_id = ban.role_id
#         if ROLES[find_role_id] == otdel:
#             session.execute(insert(Unban).values(ban_id = ban.server_role_ban_id, unban_time = datetime.datetime.now().isoformat(), unbanning_admin = username))
