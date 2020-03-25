import discord
from discord.ext import commands
import time
import random

class Fun(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.command(aliases=["q"])
    async def question(self, ctx, *, question):
        responses = [
            "Yes",
            "Obviously No",
            "Maybe..",
            "Not Sure",
            "Are u sure about that??",
            "Nope",
            "I don't know",
            "Ask me something else",
            "Hmmm",
            "What kind of question is that",
            "Thatz a Nice question",
            "Ugh..."]
        question = discord.Embed(
            title = f'**Question:** ``{question}``',
            description = f'**Response: ** ``{random.choice(responses)}``',
            colour = discord.Colour(0xff0000))
        question.set_footer(text= f'{ctx.author}', icon_url = f'{ctx.author.avatar_url}')

        await ctx.send(embed=question)

    @commands.command()
    async def flip(self, ctx):
        coin = ('Heads','Tails')
        r = random.choice(coin)
        flip = discord.Embed(
            title = '```Bot :```Flipping a Coin...',
            colour = discord.Colour(0xff000)
        )
        result= discord.Embed(
            title = f'```Result :``` {r}',
            colour = discord.Colour(0xff000)
        )
        await ctx.send(embed=flip)
        time.sleep(2)
        await ctx.send(embed=result)

def setup(client):
    client.add_cog(Fun(client))