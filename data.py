from ctypes.wintypes import BYTE
from datetime import timezone
from dotenv import load_dotenv
from sqlalchemy import DateTime, func
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column
from sqlalchemy.ext.asyncio import create_async_engine, AsyncSession, async_sessionmaker
import datetime

engine = create_async_engine(r"postgresql+asyncpg://postgres:topanbro228@localhost:8000/C:\Users\sam92\Downloads\SS14.Server_win-x64\data\preferences.db", echo=False)

async_session = async_sessionmaker(engine, class_=AsyncSession, expire_on_commit=False)

class Base(DeclarativeBase):
    pass

class Ban(Base):
    __tablename__ = 'server_role_ban'
    server_role_ban_id: Mapped[int] = mapped_column(primary_key=True, nullable=False)
    hwid: Mapped[str]
    player_user_id: Mapped[str]
    reason: Mapped[str] = mapped_column(nullable=False)
    role_id: Mapped[str] = mapped_column(nullable=False)

class Unban(Base):
    __tablename__ = 'server_role_unban'
    role_unban_id: Mapped[int] = mapped_column(nullable=False, primary_key=True)
    ban_id: Mapped[int] = mapped_column(nullable=False)
    unban_time: Mapped[str] = mapped_column(nullable=False)
    unbanning_admin: Mapped[str]

class Player(Base):
    __tablename__ = "player"
    player_id: Mapped[int] = mapped_column(nullable=False, primary_key=True)
    user_id: Mapped[int] = mapped_column(nullable=False)
    first_seen_time: Mapped[datetime.datetime] = mapped_column(DateTime(timezone=True), server_default=func.now())
    last_seen_user_name: Mapped[str] = mapped_column(nullable=False)
    last_seen_time: Mapped[datetime.datetime] = mapped_column(DateTime(timezone=True), server_default=func.now(), nullable=False)
    last_seen_address: Mapped[int] = mapped_column(nullable=False)
    last_seen_hwid: Mapped[str]
    last_read_rules: Mapped[datetime.datetime] = mapped_column(DateTime(timezone=True), server_default=func.now())