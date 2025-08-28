from sqlalchemy import select
from data import *
from sqlalchemy.orm import Session
from roles import ROLES

# with Session(engine) as session:
#     find_user_id = session.execute(select(Player.user_id).where(Player.last_seen_user_name == ckey)).scalar()
#     bans = session.execute(select(Ban).outerjoin(Unban, Ban.server_role_ban_id == Unban.ban_id).where(Ban.player_user_id == find_user_id).filter(Unban.ban_id == None)).scalars()
#     count = 0
#     # find_role_id = session.execute(select(Ban.role_id).where(Player.user_id == find_user_id)).all()
#     for ban in bans:
#         find_role_id = ban.role_id
#         if ROLES[find_role_id] == otdel:
#             session.execute(insert(Unban).values(ban_id = ban.server_role_ban_id, unban_time = datetime.datetime.now().isoformat(), unbanning_admin = username))

async def get_player_info(
    self, player_id: Optional[str] = None, discord_id: Optional[int] = None
) -> Optional[Dict[str, Any]]:
    players = {
        207784361959882752: {'id': 3462, 'discordId': 207784361959882752,
                             'userId': 'd35106f2-6dda-4e9f-82a6-f1016156b41c', 'hours': 0, 'crystal': 0, 'coin': 0}
    }
    return players.get(discord_id, None)