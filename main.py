import discord
from discord.ext import commands
from datetime import datetime
from sqlalchemy import create_engine, Column, Integer, Text, DateTime
from sqlalchemy.orm import Session, DeclarativeBase

engine = create_engine(r"sqlite:///C:\Users\sam92\Downloads\SS14.Server_win-x64\data\preferences.db", echo=True)

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(intents=intents)

class Base(DeclarativeBase):
    pass

class Ban(Base):
    __tablename__ = 'server_role_ban'
    server_role_ban_id = Column(Integer, primary_key=True, nullable=False)

class Unban(Base):
    __tablename__ = 'server_role_unban'
    role_unban_id = Column(Integer, primary_key=True, nullable=False)
    ban_id = Column(Integer, nullable=False)
    unban_time = Column(Text, nullable=False)
    unbanning_admin = Column(Text)

@bot.tree.command(name='role_unban', description='Снятие джоббана')
async def role_unban(interaction: discord.Interaction, roleban_id: int):
    username = interaction.user.display_name
    with Session(engine) as session:
        row = session.query(Ban).filter(Ban.server_role_ban_id == roleban_id).first()
        if row:
            new_row = Unban(role_unban_id=roleban_id, ban_id=roleban_id, unban_time=datetime.now().isoformat(), unbanning_admin=username)
            session.add(new_row)
            session.commit()
            await interaction.response.send_message(f'Джоббан {roleban_id} снят.')
        else: 
            await interaction.response.send_message('Такого джоббана нет.')