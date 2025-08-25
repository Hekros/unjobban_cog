from sqlalchemy import select
from data import *
from sqlalchemy.orm import Session

with Session(engine) as session:
    find_user_id = session.execute(select(Player.user_id).where(Player.last_seen_user_name == 'AroJan')).scalar()
    bans = session.execute(select(Ban).outerjoin(Unban, Ban.server_role_ban_id == Unban.ban_id).where(Ban.player_user_id == find_user_id).filter(Unban.ban_id == None)).scalars()
    for ban in bans:
        print(ban.reason)