from dotenv import load_dotenv
from sqlalchemy import create_engine, Column, Integer, Text, DateTime
from sqlalchemy.orm import Session, DeclarativeBase

engine = create_engine(r"sqlite:///C:\Users\sam92\Downloads\SS14.Server_win-x64\data\preferences.db", echo=True)
# Базовый класс для создания таблиц
class Base(DeclarativeBase):
    pass

# Воссоздаю айди джоббанов из таблицы
class Ban(Base):
    __tablename__ = 'server_role_ban'
    server_role_ban_id = Column(Integer, primary_key=True, nullable=False)

# Воссоздаю анбаны из таблицы полностью
class Unban(Base):
    __tablename__ = 'server_role_unban'
    role_unban_id = Column(Integer, primary_key=True, nullable=False)
    ban_id = Column(Integer, nullable=False)
    unban_time = Column(Text, nullable=False)
    unbanning_admin = Column(Text)