import discord
from discord.ext import commands
from datetime import datetime
from sqlalchemy import create_engine, Column, Integer
from sqlalchemy.orm import Session, DeclarativeBase

engine = create_engine(r"sqlite:///C:\Users\sam92\Downloads\SS14.Server_win-x64\data\preferences.db", echo=True)

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(intents=intents)

class Base(DeclarativeBase):
    pass

class Unban(Base):
    __tablename__ = 'server_role_ban'
    server_role_ban_id = Column(Integer, primary_key=True, nullable=False)

@bot.tree.command(name='role_unban', description='Снятие джоббана')
async def role_unban(intrecation: discord.Interaction, roleban_id: int):
    with Session(engine) as session:
        row = session.query(Unban).filter(Unban.server_role_ban_id == roleban_id).first()
        if row:
            session.delete(row)
            session.commit()
            await intrecation.response.send_message(f'Джоббан {roleban_id} снят.')
        else: 
            await intrecation.response.send_message('Такого джоббана нет.')