import discord
from discord.ext import commands

class Utility(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.command(aliases = ["info", "bot"])
    async def version(self, ctx):
        embed = discord.Embed(
            title = '**:wolf: Winter v1.0.11 :**',
            description = '''
    ``Changelog: ``
    # **Flip Improved visuals**
    # **Added a mute command**
    # **Performance Fixes**
    # **More Coming Soon**

    ``Bugs: ``
    # **Moderation Commands Usage** :white_check_mark:
    # **Error Handling Issues** :white_check_mark:
    ''',
            colour = discord.Colour(0xff0000)
            )
        embed.set_footer(text = f'{ctx.author}', icon_url = f'{ctx.author.avatar_url}')

        await ctx.send(embed=embed)

    
def setup(client):
    client.add_cog(Utility(client))