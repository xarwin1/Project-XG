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



@client.command(aliases=["shutdown", "off"])
async def poweroff(ctx):
    await ctx.send("Turning off...")
    await ctx.send("Goodbye")
    await client.close()

@client.command()
async def xarwin(ctx):
    await ctx.send("My papa")

@client.command(aliases=['whois', 'userinfo'])
async def info(ctx, member:discord.Member=None):
    if member == None:
        member = ctx.message.author
    embed = discord.Embed(title="User Information", description=f"Here is the info of user {member.name}", color = discord.Color.brand_green(), timestamp = ctx.message.created_at)
    embed.set_thumbnail(url = member.avatar)
    embed.add_field(name = "Name", value =f"{member.name}#{member.discriminator}")
    embed.add_field(name = "ID", value = member.id)
    embed.add_field(name = "Server Name", value = member.display_name)
    embed.add_field(name = "Status", value = member.status)
    embed.add_field(name = "Account Created", value = member.created_at.strftime("%B %d, %Y"))
    embed.add_field(name = "Joined Server", value = member.joined_at.strftime("%B %d, %Y"))
    
    await ctx.send(embed = embed)
    



client.run(creds.login_token)
