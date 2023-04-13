import discord
from discord.ext import commands
from discord import FFmpegPCMAudio
import asyncio
import yt_dlp



ytdl_opts = {'format': 'bestaudio/best'}
ytdl = yt_dlp.YoutubeDL(ytdl_opts)

ffmpeg_options = {'options': '-vn'}



class youtube(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.command()
    async def play(self, ctx, client, url):

        
        channel = ctx.message.author.voice.channel
        voice = discord.utils.get(client.voice_clients, guild=ctx.guild)

        loop = asyncio.get_event_loop()
        data = await loop.run_in_executor(None, lambda: ytdl.extract_info(url, download=False))
        song = data['url']
        player = discord.FFmpegPCMAudio(song, **ffmpeg_options)

        voice.play(player)

async def setup(client):
    await client.add_cog(youtube(client))
