import discord

from discord.ext import commands
from colorama import Back, Fore, Style
import time
import creds
import os

client = commands.Bot(command_prefix= "sudo ", intents=discord.Intents.all())

@client.event

async def on_ready():
    prfx = (Back.BLACK + Fore.BLUE + time.strftime("%H:%M:%S GMT+8", time.gmtime()
    ) + Back.RESET + Fore.WHITE + Style.BRIGHT)
    await client.change_presence(status=discord.Status.idle, activity=discord.Game('sex'))
    print(prfx + " Logged in as " + Fore.BLUE + client.user.name)
    print("Bot is now up!!!")


    command_cogs = []

    for filename in os.listdir('./cogs'):
        if filename.endswith('.py'):
            command_cogs.append("cogs." + filename[:-3])

    if __name__ == '__main__':
        for cogs in command_cogs:
            await client.load_extension(cogs)
        

client.run(creds.discord_token)
