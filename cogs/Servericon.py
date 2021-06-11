import discord
import os
import datetime
import asyncio
from discord.ext import commands, tasks

class Sicon(commands.Cog, name="serverinfo"):
    def __init__(self, client):
        self.client = client

    @commands.Cog.listener()
    async def on_ready(self):
        print('cogs loaded for serverinfo')



    @commands.command(aliases=['guildicon'], usage='')
    @commands.guild_only()
    async def servericon(self, ctx, *, guild_id: int = None):
        if guild_id is not None and await self.client.is_owner(ctx.author):
            guild = self.client.get_guild(guild_id)
            if guild is None:
                return await ctx.send(f'Invalid Guild ID given.')
        else:
            guild = ctx.guild
        embed = discord.Embed(color = discord.Color.dark_magenta())
        embed.title = guild.name
        if guild.icon:
            embed.set_image(url=guild.icon_url)
            

        embed.set_footer(text=f"requested by {ctx.author}", icon_url=ctx.author.avatar_url)
        await ctx.send(embed=embed)

def setup(client):
    client.add_cog(Sicon(client))