import discord
import os
import datetime
import asyncio
from discord.ext import commands, tasks

class userinfo(commands.Cog, name="Userinfo"):
    def __init__(self, client):
        self.client = client

    @commands.Cog.listener()
    async def on_ready(self):
        print('cogs loaded for userinfo')

    @commands.command()
    async def userinfo(self , ctx, member: discord.Member = None):
        member = ctx.author if not member else member
        roles = [role for role in member.roles]

        embed = discord.Embed(colour=member.color, timestamp=ctx.message.created_at)

        embed.set_author(name=f"User Info - {member}")
        embed.set_thumbnail(url=member.avatar_url)
        embed.set_footer(text=f"requested by {ctx.author}", icon_url=ctx.author.avatar_url)

        embed.add_field(name="ID:", value=member.id)
        embed.add_field(name="Status:", value = member.status)
        embed.add_field(name="User name:", value=member.display_name, inline=False)

        embed.add_field(name="Created at:", value=member.created_at.strftime("%a, %#d %B %Y, %I:%M %p UTC"),inline=False)
        embed.add_field(name="Joined at:", value=member.joined_at.strftime("%a, %#d %B %Y, %I:%M %p UTC"),inline=False)

        embed.add_field(name="Top Role:", value=member.top_role.mention, inline=False)
        embed.add_field(name=f"Roles ({len(roles)})", value="".join(sorted([role.mention for role in roles])), inline=False)
        
        await ctx.send(embed=embed)

def setup(client):
    client.add_cog(userinfo(client))
