import creds
import discord
from discord.ext import commands


client = commands.Bot(command_prefix= "$", intents=discord.Intents.all())



@client.event

async def on_ready():

    print("Bot is now up!!!")
    

@client.command()

async def test(ctx):
    await ctx.send("Command is working papa")



client.run(creds.login_token)
