import discord
from discord.ext import commands


class userinfo(commands.Cog):
    def __init__(self, client):
        self.client = client


    
    @commands.command(aliases=['whois', 'userinfo'])
    async def info(self, ctx, member: discord.Member = None):
        if member == None:
            member = ctx.message.author
        embed = discord.Embed(title="User Information", description=f"Here is the info of user {member.name}", color=discord.Color.brand_green(
        ), timestamp=ctx.message.created_at)
        embed.set_thumbnail(url=member.avatar)
        embed.add_field(name="Name", value=f"{member.name}#{member.discriminator}")
        embed.add_field(name="ID", value=member.id)
        embed.add_field(name="Server Name", value=member.display_name)
        embed.add_field(name="Status", value=member.status)
        embed.add_field(name="Account Created",
                        value=member.created_at.strftime("%B %d, %Y"))
        embed.add_field(name="Joined Server",
                        value=member.joined_at.strftime("%B %d, %Y"))

        await ctx.send(embed=embed)


async def setup(client):
    await client.add_cog(userinfo(client))
