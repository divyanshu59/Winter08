import discord
from discord.ext import commands

class Help(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.command()
    async def help(self, ctx):
        guild_msg = discord.Embed(
            title = f'```Bot :``` Help arrived in your Dms ``{ctx.message.author}``',
            colour=discord.Colour(0xff000)
            )
        dm_msg = discord.Embed(
            title = '**Basic Commands: \n**',
            colour = discord.Colour(0xff000))
        dm_msg.add_field(name = 'Command -- ``"hi"``: ', value = '>``You will be greeted by the Bot.``', inline = 'false')
        dm_msg.add_field(name = 'Command -- ``"ping"``: ', value = '>``Returns the latency/ping of the Bot.``', inline = 'false')
        dm_msg.add_field(name = 'Command -- ``"version"``: ', value = '>``Returns the Bot information.``', inline = 'false' )
        dm_msg.add_field(name = 'Command -- `` "question x <your question>"``: ', value = '>``Responses to your question randomly.``')
        dm_msg.add_field(name = 'Command -- `` "flip"``: ', value = '>``Flips a coin a displays either Head or Tails.``', inline = 'false')
        dm_msg.add_field(name = 'Command -- `` "me(Your Info) or whois <user> (Info of Tagged User)"``: ', value = '>``Displays some info about the target user.``',inline = 'false')
        dm_msg.set_footer(text = f'{ctx.author}', icon_url = f'{ctx.author.avatar_url}')

        dm_msg2 = discord.Embed(
            title = '**Moderation Commands: \n**',
            colour = discord.Colour(0xff000)
            )
        dm_msg2.add_field(name = 'Command -- ``"kick + <user> + reason"`` :', value = '>``Will kick the target from the guild``', inline = 'false')
        dm_msg2.add_field(name = 'Command -- ``"ban + <user> + reason"`` :', value = '>``Will ban the target from the guild``', inline = 'false')
        dm_msg2.add_field(name = 'Command -- ``"unban + <user> + reason"``: ', value = '``>Will unban the target from the guild``', inline = 'false')
        dm_msg2.add_field(name = 'Command -- ``"mute + <user> + reason"``: ', value = '``>Will Mute the person for given time in Minutes``', inline = 'false')
        dm_msg2.add_field(name = 'Command -- ``"unmute + <user> + reason"``: ', value = '``>Will Unmute the person for given time in Minutes``', inline = 'false')
        dm_msg2.add_field(name = 'Command -- ``"purge + <amount> ,default amount = 10"``: ', value = '``>Will purge specified number of messages from the guild``', inline = 'false')
        dm_msg2.set_footer(text = f'{ctx.author}', icon_url = f'{ctx.author.avatar_url}')

        dm_msg3 = discord.Embed(
            title = '**Help Commands: ** \n',
            colour = discord.Colour(0xff000)
            )
        dm_msg3.add_field(name= 'Command -- ``"help"``:', value = '``>Displays this messages.``', inline = 'false')
        dm_msg3.add_field(name = 'Command -- ``"support"``:', value = '``>Provides the link for the support/test server for Winter.``', inline = 'false')
        dm_msg3.add_field(name = 'Command -- ``"vote"``:', value = '``>UpVote for Winter :).``', inline = 'false')
        dm_msg3.set_footer(text = f'{ctx.author}', icon_url = f'{ctx.author.avatar_url}')

        await ctx.send(embed=guild_msg)
        await ctx.author.send(embed=dm_msg)
        await ctx.author.send(embed=dm_msg2)
        await ctx.author.send(embed=dm_msg3)
    
    @commands.command()
    async def support(self, ctx):
        dm = discord.Embed(
            title = '```Bot :``` Here a link to my test/support server: ',
            description = 'Link: https://discord.gg/yENwXPx',
            colour = discord.Color(0xff000)
            )
        guild = discord.Embed(
            title = f'```Bot :```Support arrived in Dms ``{ctx.message.author}``',
            colour = discord.Colour(0xff000)
            )
        
        await ctx.author.send(embed=dm)
        await ctx.send(embed=guild)

    @commands.command()
    async def vote(self, ctx):
        embed = discord.Embed(
            title = 'Vote For Winter:',
            description = 'https://top.gg/bot/586553956843388942/vote',
            colour = discord.Colour.green()
            )
        await ctx.send(embed=embed)

    
def setup(client):
    client.add_cog(Help(client))