import discord
from discord.ext import commands
import traceback
import sys

class Error(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.Cog.listener()
    async def on_command_error(self, ctx , error):
        if  isinstance(error, commands.CommandNotFound):
            e = discord.Embed(
                title = f'```Error :``` {error}',
                color = discord.Color.green()
            )
            await ctx.send(embed=e)

        if isinstance(error, commands.MissingRequiredArgument):
            e = discord.Embed(
                title = f'```Error :``` {error}',
                color = discord.Color.green()
            )
            await ctx.send(embed=e)

        if isinstance(error, commands.MissingPermissions):
            e = discord.Embed(
                title = f'```Error :``` {error}',
                color = discord.Color.green()
            )
            
            await ctx.send(embed=e)

        if isinstance(error, commands.UserInputError):
            e = discord.Embed(
                title = f'```Error :``` {error}',
                color = discord.Color.green()
            )
            
            await ctx.send(embed=e)


def setup(client):
    client.add_cog(Error(client))