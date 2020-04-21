import discord
from discord.ext import commands
from discord.utils import get

class guild(commands.Cog):
    def __init__(self, client):
        self.client = client
 
 
    @commands.Cog.listener()
    async def on_member_join(self, member):
        for channel in member.guild.channels:
            if str(channel) == "join-leave":
                embed = discord.Embed(
                    title = f"Wecome to {member.guild.name} :partying_face: :partying_face: :partying_face:",
                    description = f"{member.name}",
                    color = discord.Color.gold()
                )
                embed.set_image(url=f"{member.avatar_url}")
                await channel.send(embed=embed)

    @commands.Cog.listener()
    async def on_member_remove(self, member):
        for channel in member.guild.channels:
            if str(channel) == "join-leave":
                embed = discord.Embed(
                    title = f"Goodbye , we will miss you. :sob::sob::sob:",
                    description = f"{member.name}",
                    color = discord.Color.gold()
                )
                embed.set_image(url=f"{member.avatar_url}")
                await channel.send(embed=embed)
    
    async def on_message_edit(self, before, after, channel, member):
        for channel in member.guild.channels:
            if str(channel) == "server-log":
                fmt = '**{0.author}** edited their message:\n{0.content} -> {1.content}'
                await channel.send(fmt.format(before, after))

    @commands.command()
    async def setup(self, ctx, mode= None,args = None):
        if args == "memberlog" and mode == "enable":
            guild = ctx.message.guild
            await guild.create_text_channel('join-leave')

        elif args == "guildlog" and mode == "enable":
            guild = ctx.message.guild
            await guild.create_text_channel('server-log')

        else:
            embed = discord.Embed(
                title = 'Setup: ',
                description = ''' 1) **memberlog** = Will create a seprate channel for join and leave logs.

                ``Usage`` = setup enable/disable <choice>
                ''',
                color = discord.Color.green()
            )
            await ctx.send(embed=embed)

    @commands.command()
    @commands.is_owner()
    async def guilds(self, ctx, time=10):
        for guild in self.client.guilds:
            embed = discord.Embed(
                title = f'''{guild}''',
                color = discord.Color.green()
            )
            await ctx.send(embed=embed, delete_after=time)





def setup(client):
    client.add_cog(guild(client))