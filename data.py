from ctypes.wintypes import BYTE
from datetime import timezone
from dotenv import load_dotenv
from sqlalchemy import INT, Text, DateTime, LargeBinary, Text, create_engine, Integer, Text
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column
from sqlalchemy.ext.asyncio import create_async_engine, AsyncSession
from sqlalchemy.orm import sessionmaker

engine = create_async_engine(r"sqlite:///C:\Users\sam92\Downloads\SS14.Server_win-x64\data\preferences.db", echo=False)

async_session = sessionmaker(engine, class_=AsyncSession, expire_on_commit=False)

class Base(DeclarativeBase):
    pass

class Ban(Base):
    __tablename__ = 'server_role_ban'
    server_role_ban_id: Mapped[int] = mapped_column(primary_key=True, nullable=False)
    hwid: Mapped[Text]
    player_user_id: Mapped[Text]
    reason: Mapped[Text] = mapped_column(nullable=False)
    role_id: Mapped[Text] = mapped_column(nullable=False)

class Unban(Base):
    __tablename__ = 'server_role_unban'
    role_unban_id: Mapped[int] = mapped_column(nullable=False, primary_key=True)
    ban_id: Mapped[int] = mapped_column(nullable=False)
    unban_time: Mapped[Text] = mapped_column(nullable=False)
    unbanning_admin: Mapped[Text]

class Player(Base):
    __tablename__ = "player"
    player_id: Mapped[int] = mapped_column(nullable=False, primary_key=True)
    user_id: Mapped[int] = mapped_column(nullable=False)
    first_seen_time: Mapped[DateTime] = mapped_column(timezone=True)
    last_seen_user_name: Mapped[Text] = mapped_column(nullable=False)
    last_seen_time: Mapped[DateTime] = mapped_column(nullable=False, timezone=True)
    last_seen_address: Mapped[Text] = mapped_column(nullable=False)
    last_seen_hwid:  Mapped[Text]
    last_read_rules:  Mapped[DateTime] = mapped_column(timezone=True)