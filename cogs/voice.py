import discord
from discord.ext import commands

class voice(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.command()
    async def join(self, ctx):
        if (ctx.author.voice):
            channel = ctx.message.author.voice.channel
            await channel.connect()
        else:
            await ctx.send("You're not in a voice channel.")
    
    @commands.command()
    async def next(self, ctx):
        voice = ctx.voice_client
        if voice.is_playing() or voice.is_paused():
            voice.stop()
        else:
            await ctx.send("There is no audio to stop")


    @commands.command(aliases=['stop'])
    async def leave(self, ctx):
        if (ctx.voice_client):
            await ctx.guild.voice_client.disconnect()
            await ctx.send("I left the voice channel")
        else:
            await ctx.send("I'm not in the voice channel")


async def setup(client):
    await client.add_cog(voice(client))
