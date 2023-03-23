import discord
from discord.ext import commands


client = commands.Bot(command_prefix= "$", intents=discord.Intents.all())
login_token = "MTA4Nzk0NDY3Mzk5NTI3MjIzMg.G5ZJ7G.5szT9fyd6Q3090E2-IpJK3PSgRtBXZLe_HHzD0"


@client.event

async def on_ready():

    print("Bot is now up!!!")
    

@client.command()

async def test(ctx):
    await ctx.send("Command is working papa")

client.run(login_token)
