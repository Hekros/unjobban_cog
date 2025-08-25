from ctypes.wintypes import BYTE
from dotenv import load_dotenv
from sqlalchemy import INT, Text, DateTime, LargeBinary, Text, create_engine, Column, Integer, Text
from sqlalchemy.orm import DeclarativeBase

engine = create_engine(r"sqlite:///C:\Users\sam92\Downloads\SS14.Server_win-x64\data\preferences.db", echo=True)
# Базовый класс для создания таблиц
class Base(DeclarativeBase):
    pass

# Воссоздаю айди джоббанов из таблицы
class Ban(Base):
    __tablename__ = 'server_role_ban'
    server_role_ban_id = Column(Integer, primary_key=True, nullable=False)
    hwid = Column(Text)
    player_user_id = Column(Text)
    reason = Column(Text, nullable=False)

# Воссоздаю анбаны из таблицы полностью
class Unban(Base):
    __tablename__ = 'server_role_unban'
    role_unban_id = Column(Integer, primary_key=True, nullable=False)
    ban_id = Column(Integer, nullable=False)
    unban_time = Column(Text, nullable=False)
    unbanning_admin = Column(Text)

class Player(Base):
    __tablename__ = "player"
    player_id = Column(Integer, nullable=False, primary_key=True)
    user_id = Column(Text, nullable=False)
    first_seen_time = Column(DateTime(timezone=True), nullable=False)
    last_seen_user_name = Column(Text, nullable=False)
    last_seen_time = Column(DateTime(timezone=True), nullable=False)
    last_seen_address = Column(INT, nullable=False)
    last_seen_hwid = Column(Text)
    last_read_rules = Column(DateTime(timezone=True))