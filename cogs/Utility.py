import discord
from discord.ext import commands
import winter

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
    :pushpin: **All New Music :musical_note:** [WIP] [Coming Soon]
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

    
def setup(client):
    client.add_cog(Utility(client))
