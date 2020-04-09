import discord
from discord.ext import commands
import time
import random
import praw

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

    @commands.command()
    async def meme(self, ctx):
        load = discord.Embed(
            title = 'Loading...',
            color = discord.Color.green()
        )
        await ctx.send(embed=load, delete_after=1)

        reddit =  praw.Reddit(client_id = 'cKtdy4mx7fPopQ',
                        client_secret = 'PuQBb-kfu6EPxayDZQYqydYq6v0',
                        username = 'Connerwolf08',
                        password = 'Sonu ghost@123',
                        user_agent = 'Winter08 v.1.0'
        )

        memes_submissions = reddit.subreddit('memes').hot()
        post_to_pick = random.randint(1, 100)
        for x in range(0, post_to_pick):
            submission = next(x for x in memes_submissions if not x.stickied)
        meme = discord.Embed(
            title = f'``Title :``{submission.title}',
            color = discord.Color.green()
        )
        meme.set_image(url=f'{submission.url}')
        meme.add_field(name=':thumbsup: **Upvotes** :',value= f'{submission.ups}',inline=True)
        meme.add_field(name=':thumbsdown: **Downvotes** :',value= f'{submission.downs}',inline=True)
        await ctx.send(embed=meme)

    @commands.command()
    async def cat(self, ctx):
        load = discord.Embed(
            title = 'Loading...',
            color = discord.Color.green()
        )
        await ctx.send(embed=load, delete_after=1)

        reddit =  praw.Reddit(client_id = 'cKtdy4mx7fPopQ',
                        client_secret = 'PuQBb-kfu6EPxayDZQYqydYq6v0',
                        username = 'Connerwolf08',
                        password = 'Sonu ghost@123',
                        user_agent = 'Winter08 v.1.0'
        )
        cat_images = reddit.subreddit('cats').hot()
        post_to_pick = random.randint(1, 100)
        for x in range(0, post_to_pick):
            submission = next(x for x in cat_images if not x.stickied)
        cat = discord.Embed(
            title = f'``Here take some Cats. `` :heart_eyes_cat:',
            color = discord.Color.green()
        )
        cat.set_image(url=f'{submission.url}')
        await ctx.send(embed=cat)

    @commands.command()
    async def dog(self, ctx):
        load = discord.Embed(
            title = 'Loading...',
            color = discord.Color.green()
        )
        await ctx.send(embed=load, delete_after=1)

        reddit =  praw.Reddit(client_id = 'cKtdy4mx7fPopQ',
                        client_secret = 'PuQBb-kfu6EPxayDZQYqydYq6v0',
                        username = 'Connerwolf08',
                        password = 'Sonu ghost@123',
                        user_agent = 'Winter08 v.1.0'
        )
        dog_images = reddit.subreddit('dogpictures').hot()
        post_to_pick = random.randint(1, 100)
        for x in range(0, post_to_pick):
            submission = next(x for x in dog_images if not x.stickied)
        dog = discord.Embed(
            title = f'``Here take some Dogs. `` :dog:',
            color = discord.Color.green()
        )
        dog.set_image(url=f'{submission.url}')
        await ctx.send(embed=dog)

        

def setup(client):
    client.add_cog(Fun(client))
