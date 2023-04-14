import discord
from discord.ext import commands
from discord import FFmpegPCMAudio
import asyncio
import yt_dlp



ytdl_opts = {'format': 'bestaudio/best'}
ytdl = yt_dlp.YoutubeDL(ytdl_opts)

ffmpeg_options = {'before_options': '-reconnect 1 -reconnect_streamed 1 -reconnect_delay_max 5', 'options' : '-vn'}



class youtube(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.command()
    async def play(self, ctx, url):

        
        
        channel = ctx.message.author.voice.channel
        voice = discord.utils.get(self.client.voice_clients, guild=ctx.guild)

        loop = asyncio.get_event_loop()
        data = await loop.run_in_executor(None, lambda: ytdl.extract_info(url, download=False))
        song = data['url']
        player = discord.FFmpegPCMAudio(song, **ffmpeg_options)

        if voice is None or not voice.is_connected():
            voice = await channel.connect()
        voice.play(player)
            
        




async def setup(client):
    await client.add_cog(youtube(client))
