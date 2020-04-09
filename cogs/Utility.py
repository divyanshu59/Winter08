import discord
from discord.ext import commands
import winter
import random
import asyncio

client = commands.Bot

class Utility(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.command(aliases = ["info", "bot"])
    async def version(self, ctx):
        embed = discord.Embed(
            title = '**:wolf: Winter v1.0.11 :**',
            description = f'''
    ``Changelog: ``
    :pushpin: **Memes command is here :heart_eyes:**
    :pushpin: ** Random Dog and Cat Images are here :dog: :cat:** 
    :pushpin: **Added a mute command :mute:**
    :pushpin: **Performance Fixes :fast_forward:**
    :pushpin: **More Coming Soon :slight_smile:**

    ``Bugs: ``
    :pushpin: **Moderation Commands Usage** :white_check_mark:
    :pushpin: **Error Handling Issues** :white_check_mark:
    ''',
            colour = discord.Colour(0xff0000)
            )
        embed.set_footer(text = f'{ctx.author}', icon_url = f'{ctx.author.avatar_url}')

        await ctx.send(embed=embed)

    @commands.command()
    async def random(self, ctx, first: int, second: int):
        n = random.randrange(first,second)
        run = discord.Embed(
            title = f'Generating a random number between `{first}` and `{second}`',
            color = discord.Color.green()
        )
        result = discord.Embed(
            title = f'Result: `{n}`',
            color = discord.Color.green()
        )
        await ctx.send(embed=run,delete_after=3)
        await asyncio.sleep(2)
        await ctx.send(embed=result)
           
       

    
def setup(client):
    client.add_cog(Utility(client))
