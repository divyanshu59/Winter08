import discord
from discord.ext import commands


class Music(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(pass_context=True)
    async def join(self, ctx):
        channel = ctx.message.author.voice.channel
        await channel.connect()

    @commands.command(pass_context=True)
    async def leave(self, ctx):
        server = ctx.message.guild.voice_client
        await server.disconnect()

def setup(client):
    client.add_cog(Music(client))