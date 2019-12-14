import discord
import os
import datetime
import asyncio
from discord.ext import commands, tasks

class Sinfo(commands.Cog, name="serverinfo"):
    def __init__(self, client):
        self.client = client

    @commands.Cog.listener()
    async def on_ready(self):
        print('cogs loaded for serverinfo')


    @commands.command(aliases=['guildinfo'], usage='')
    @commands.guild_only()
    async def serverinfo(self, ctx, *, guild_id: int = None):
        if guild_id is not None and await self.client.is_owner(ctx.author):
            guild = self.client.get_guild(guild_id)
            if guild is None:
                return await ctx.send(f'Invalid Guild ID given.')
        else:
            guild = ctx.guild

        roles = [role.name.replace('@', '@\u200b') for role in guild.roles]

        embed = discord.Embed(color = discord.Color.dark_magenta())
        embed.title = guild.name
        embed.add_field(name='ID', value=guild.id,inline=False)
        embed.add_field(name='Owner', value=guild.owner,inline=False)
        if guild.icon:
            embed.set_thumbnail(url=guild.icon_url)

        embed.add_field(name='Created', value=guild.created_at.strftime("%a, %#d %B %Y, %I:%M %p UTC"),inline=False)
        embed.add_field(name='region', value=guild.region,inline=False)
        embed.add_field(name='Categories', value=len(guild.categories))
        embed.add_field(name='Text Channels', value=len(guild.text_channels))
        embed.add_field(name='Voice Channels', value=len(guild.voice_channels))
        
        embed.add_field(name='Roles', value=', '.join(roles) if len(roles) < 10 else f'{len(roles)} roles', inline=False)
        embed.set_footer(text=f"requested by {ctx.author}", icon_url=ctx.author.avatar_url)
        # e.set_footer(text='Created').timestamp = guild.created_at
        await ctx.send(embed=embed)



def setup(client):
    client.add_cog(Sinfo(client))