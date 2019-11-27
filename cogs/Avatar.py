import discord
from discord.ext import commands

class avatar(commands.Cog, name = "Avatar"):

    def __init__(self, client):
        self.client = client

    @commands.Cog.listener()
    async def on_ready(self):
        print('Cogs are loaded for avatar')

    @commands.command()
    async def avatar(self, ctx, member: discord.Member):
        Savatar = discord.Embed(color = discord.Color.default())
        Savatar = embed = discord.Embed(colour=member.color)
        Savatar = embed.set_author(name=f"Avatar - {member}")
        Savatar = embed.set_footer(text=f"requested by {ctx.author}", icon_url=ctx.author.avatar_url)
        Savatar.set_image(url='{}'.format(member.avatar_url))
        """embed = discord.Embed(colour=member.color)
        embed.set_author(name=f"Avatar - {member}")
        embed.set_footer(text=f"requested by {ctx.author}", icon_url=ctx.author.avatar_url)"""

        await ctx.send(embed= Savatar)



def setup(client):
    client.add_cog(avatar(client))

