import discord
from discord.ext import commands

class Basic(commands.Cog):
    def __init__(self,client):
        self.client = client

    @commands.command(aliases = ["hey","sup"])
    async def hi(self, ctx):
        member = ctx.author.name
        embed = discord.Embed(
        title = f'``Bot :`` Hello, from the other side, {member}',
        colour = discord.Colour(0xff000)
        )
        await ctx.send(embed=embed)

    @commands.command()
    async def me(self,ctx):
        embed = discord.Embed(
            title = 'About You:',
            description = f'''
            ``User Name :`` **{ctx.author.name}**
            ``User ID :`` **{ctx.author.id}**
            ``User Status :`` **{ctx.author.status}**
            ``User Highest Role :`` **{ctx.author.top_role}**
            ``User Joined At :`` **{ctx.author.joined_at}**
            ''',
            colour = discord.Colour.green()
            )
        embed.set_image(url=f'{ctx.author.avatar_url}')
        embed.set_footer(
            text = f'{ctx.author}',
            icon_url = f'{ctx.author.avatar_url}'
            )
    
        await ctx.send(embed=embed)

    @commands.command()
    async def whois(self, ctx, user: discord.Member):
        embed = discord.Embed(
            title = f'About Them :',
            description = f'''
            ``User Name :`` **{user.name}**
            ``User ID :``**{user.id}**
            ``User Status :``**{user.status}**
            ``User Highest Role :``**{user.top_role}**
            ``User Joined At :``**{user.joined_at}**
            ''',
            colour = discord.Colour.green()
            )
        embed.set_image(url=f'{user.avatar_url}')
        embed.set_footer(
            text = f'{ctx.author}',
            icon_url = f'{ctx.author.avatar_url}'
            )
    
        await ctx.send(embed=embed)



def setup(client):
    client.add_cog(Basic(client))