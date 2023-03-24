import creds
import discord
from discord.ext import commands
from colorama import Back, Fore, Style
import time
import platform



client = commands.Bot(command_prefix= "$", intents=discord.Intents.all())



@client.event

async def on_ready():
    prfx = (Back.BLACK + Fore.BLUE + time.strftime("%H:%M:%S GMT+8", time.gmtime()
    ) + Back.RESET + Fore.WHITE + Style.BRIGHT)
    print(prfx + " Logged in as " + Fore.BLUE + client.user.name)
    print("Bot is now up!!!")
    

@client.command()

async def test(ctx):
    await ctx.send("Command is working papa")


@client.command()

async def iloveyou(ctx):
    await ctx.send("putang ina mo")


@client.command()

async def poweroff(ctx):
    await ctx.send("Turning off...")
    await ctx.send("Goodbye")
    await client.close()



client.run(creds.login_token)
