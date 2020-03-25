import discord
from discord.ext import commands
import asyncio

class Mod(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.command(aliases=['k'])
    @commands.has_permissions(kick_members=True)
    async def kick(self, ctx, member: discord.Member=None, *,reason=None):
        if not member:
            await ctx.send('Please specify a memeber')
            return
        await member.kick(reason=reason)
        embed = discord.Embed(
        title = f'``Logs :`` User {member} has been Kicked by {ctx.author}',
        description = f'```Reason :``` > **{reason}**',
        color = discord.Color.green()
        )
        await ctx.send(embed=embed)    

    @commands.command(aliases=['b'])
    @commands.has_permissions(ban_members=True)
    async def ban(self, ctx, member: discord.Member=None, *,reason=None):
        if not member:
            await ctx.send('Please specify a member')
            return
        await member.ban(reason=reason)
        embed = discord.Embed(
        title = f'``Logs :`` User {member} has been Banned by {ctx.author}',
        description = f'```Reason :``` >  **{reason}**',
        color = discord.Color.green()
        )
        await ctx.send(embed=embed)

    @commands.command(aliases=['ub'])
    @commands.has_permissions(ban_members=True)
    async def unban(self, ctx, member:discord.Member, *,reason=None):
        banned_users = await ctx.guild.bans()
        member_name, member_discriminator = member.split('#')

        for ban_entry in banned_users:
            user = ban_entry.user

            if (user.name, user.discriminator) == (member_name, member_discriminator):
                await ctx.guild.unban(user,reason=reason)
                embed = discord.Embed(
                title = f'``Logs :`` User {member} has been Unbanned by {ctx.author}',
                description = f'```Reason :``` >  **{reason}**',
                color = discord.Color.green()
                )
                await ctx.send(embed=embed)
                return
                
    @commands.command(aliases=['m'])
    @commands.has_permissions(kick_members=True)
    async def mute(self, ctx, member: discord.Member=None,mute_minutes=0, *,reason=None):
        role = discord.utils.get(ctx.guild.roles, name='Muted')
        if not member:
            await ctx.send('Please specify a member')
            return
        
        await member.add_roles(role,reason=reason)
        mute = discord.Embed(
        title = f'``Logs :`` User {member} has been Muted by {ctx.author}',
        description = f'```Reason :``` >  **{reason}** ```Time :``` >  **{mute_minutes}m**',
        color = discord.Color.green()
        )
        await ctx.send(embed=mute)

        if mute_minutes > 0:
            await asyncio.sleep(mute_minutes * 60)
            await member.remove_roles(role,reason='Times up')
            unmute = discord.Embed(
                title = f'``Logs :`` User {member} has been Unmuted',
                description = '```Reason :``` >  Times up',
                color = discord.Color.green()
            )
            await ctx.send(embed=unmute)

    @commands.command(aliases=['um'])
    @commands.has_permissions(kick_members=True)
    async def unmute(self, ctx, member: discord.Member=None, *,reason=None):
        role = discord.utils.get(ctx.guild.roles, name='Muted')
        if not member:
            await ctx.send('Please specify a member')
            return
        
        await member.remove_roles(role,reason=reason)
        embed = discord.Embed(
        title = f'``Logs :`` User {member} has been Unmuted by {ctx.author}',
        description = f'```Reason :``` >  **{reason}**',
        color = discord.Color.green()
        )
        await ctx.send(embed=embed)

    @commands.command(aliases=['c','clear'])
    @commands.has_permissions(manage_messages=True)
    async def purge(self, ctx, amount: 10):
        channel = ctx.channel
        embed = discord.Embed(
        title = f'``Logs :`` {ctx.author} deleted {amount} messages',
        color = discord.Color.green()
        )
        await channel.purge(limit=amount)
        await ctx.send(embed=embed,delete_after=2)  

def setup(client):
    client.add_cog(Mod(client))