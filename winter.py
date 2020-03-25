import discord
from discord.ext import commands
import os

token = "" # token goes here
prefix = '$'
client = commands.Bot(command_prefix = prefix, owner_id = 450223497021489163)
client.remove_command('help')

# Login:

@client.event
async def on_ready():
    print(f"Logged in as {client.user}")
    await client.change_presence(activity=discord.Game(name = f'in {str(len(client.guilds))} Servers'))

@client.command()
@commands.is_owner()
async def test(ctx):
    embed = discord.Embed(
        title = 'Test Pass !!',
        colour = discord.Color.green()
        )
    await ctx.send(embed=embed)

@client.command(aliases = ["pong","latency"])
async def ping(ctx):
    embed = discord.Embed(
        title = f':ping_pong:**Ping :** ``{round((client.latency * 1000))}ms``',
        colour = discord.Colour(0xff0000)
    )

    await ctx.send(embed = embed)


# Cogs

@client.command()
@commands.is_owner()
async def load(ctx,extension):
    client.load_extension(f'cogs.{extension}')
    embed = discord.Embed(
        title = f'```System :```Cog `{extension}` has been loaded',
        color = discord.Color.green()
        )
    await ctx.send(embed=embed)

@client.command()
@commands.is_owner()
async def unload(ctx,extension):
    client.unload_extension(f'cogs.{extension}')
    embed = discord.Embed(
        title = f'```System :```Cog `{extension}` has been unloaded',
        color = discord.Color.green()
        )
    await ctx.send(embed=embed)

@client.command()
@commands.is_owner()
async def reload(ctx,extension):
    client.unload_extension(f'cogs.{extension}')
    client.load_extension(f'cogs.{extension}')
    embed = discord.Embed(
        title = f'```System :```Cog `{extension}` has been reloaded',
        color = discord.Color.green()
        )
    await ctx.send(embed=embed)

for filename in os.listdir('./cogs'):
    if filename.endswith('.py'):
        client.load_extension(f'cogs.{filename[:-3 ]}')

client.run(token)
