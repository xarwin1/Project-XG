import discord
from discord.ext import commands
from discord import FFmpegPCMAudio
import glob
import asyncio

class music(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.command()
    async def alex(self, ctx):

        channel = ctx.message.author.voice.channel
        voice = await channel.connect()
        songs = glob.glob(
            "/home/xarwin/projects/Project-XG/resources/audio/Lex/*.mp3")

        for song in songs:
            voice.play(discord.FFmpegPCMAudio(song))
            noprefix = song.removeprefix(
                "/home/xarwin/projects/Project-XG/resources/audio/Lex/")
            nosuffix = noprefix.removesuffix(".mp3")
            embed = discord.Embed(title="Now playing", description=nosuffix,
                                color=discord.Color.brand_green(), timestamp=ctx.message.created_at)
            await ctx.send(embed=embed)
            while voice.is_playing():
                await asyncio.sleep(1)


    @commands.command()
    async def dwight(self, ctx):

        channel = ctx.message.author.voice.channel
        voice = await channel.connect()
        songs = glob.glob(
            "/home/xarwin/projects/Project-XG/resources/audio/chills/*.mp3")

        for song in songs:
            voice.play(discord.FFmpegPCMAudio(song))
            noprefix = song.removeprefix(
                "/home/xarwin/projects/Project-XG/resources/audio/chills/")
            nosuffix = noprefix.removesuffix(".mp3")
            embed = discord.Embed(title="Now playing", description=nosuffix,
                                color=discord.Color.brand_green(), timestamp=ctx.message.created_at)
            await ctx.send(embed=embed)
            while voice.is_playing():
                await asyncio.sleep(1)


    @commands.command(aliases=['ethan'])
    async def etthan(self, ctx):

        channel = ctx.message.author.voice.channel
        voice = await channel.connect()
        songs = glob.glob(
            "/home/xarwin/projects/Project-XG/resources/audio/ugabuga/*.mp3")

        for song in songs:
            voice.play(discord.FFmpegPCMAudio(song))
            noprefix = song.removeprefix(
                "/home/xarwin/projects/Project-XG/resources/audio/ugabuga/")
            nosuffix = noprefix.removesuffix(".mp3")
            embed = discord.Embed(title="Now playing", description=nosuffix,
                                color=discord.Color.brand_green(), timestamp=ctx.message.created_at)
            await ctx.send(embed=embed)
            while voice.is_playing():
                await asyncio.sleep(1)


    

async def setup(client):
    await client.add_cog(music(client))