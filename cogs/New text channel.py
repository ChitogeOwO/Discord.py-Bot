import discord
import os
import datetime
import asyncio
import sys
from discord.ext import commands, tasks
from discord.utils import get


class channel(commands.Cog, name="new text channel"):
    def __init__(self, client):
        self.client = client

    @commands.Cog.listener()
    async def on_ready(self):
        print("cogs are laoded for new text channel")

    @commands.command()
    async def newchannel(self, ctx):
        guild = ctx.message.guild
        overwrites= {
            guild.default_role: discord.PermissionOverwrite(read_messages=False),
            guild.me: discord.PermissionOverwrite(read_messages=True),
        }
        await guild.create_text_channel('private room', overwrites=overwrites)
        await ctx.send('new private channel added, now give permission to those members who you wanted to start conversation with "privatly."')
        print('new channel added')

def setup(client):
    client.add_cog(channel(client))