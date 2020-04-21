import discord
from discord.ext import commands
import sqlite3
import datetime
import time

class Logging(commands.Cog):
    def  __init__(self, client):
        self.client = client

    @commands.Cog.listener()
    async def on_message(self, message):
        Guild = str(message.guild.name)
        User = str(message.author.name)
        Msg = str(message.content)
        Time = datetime.datetime.now()

        con = sqlite3.connect("logs.db")
        c = con.cursor()
        if message.author == self.client.user:
            return
        elif message.author.id == 450223497021489163:
            return
        elif message.guild.id == 264445053596991498:
            return
        else:
            c.execute("INSERT INTO Userinfo VALUES ('{}','{}','{}','{}')".format(Time, Guild, User, Msg))
            con.commit()
            con.close()

    @commands.command()
    @commands.is_owner()
    async def make(self, ctx):
        con = sqlite3.connect("logs.db")
        c = con.cursor()
        c.execute("CREATE TABLE Userinfo (Time text,Guild text, User text, Msg text)")
        con.commit()
        con.close()
        await ctx.send("Log Table is Ready !!!")

    @commands.command()
    @commands.is_owner()
    async def remake(self, ctx):
        con = sqlite3.connect("logs.db")
        c = con.cursor()
        c.execute("DROP TABLE Userinfo")
        con.commit()
        con.close()
        con = sqlite3.connect("logs.db")
        c = con.cursor()
        c.execute("CREATE TABLE Userinfo (Time text,Guild text, User text, Msg text)")
        con.commit()
        con.close()
        await ctx.send("Log Table is Ready !!!")

    @commands.command()
    @commands.is_owner()
    async def unmake(self, ctx):
        con = sqlite3.connect("logs.db")
        c = con.cursor()
        c.execute("DROP TABLE Userinfo")
        con.commit()
        con.close()
        await ctx.send("Log Table Dropped !!!")

    @commands.command()
    @commands.is_owner()
    async def logs(self, ctx, time = 60):
        con = sqlite3.connect("logs.db")
        c = con.cursor()
        c.execute("SELECT *  FROM Userinfo WHERE Msg IS NOT NULL;")
        for row in c.fetchall():
            embed = discord.Embed(
                title = 'Logs :',
                description = f"{row}",
                color = discord.Color.green()
            )
            await ctx.send(embed=embed, delete_after=time)

    
    
def setup(client):
    client.add_cog(Logging(client))