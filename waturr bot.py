import discord
import os
import datetime
import asyncio
import sys
from discord.ext import commands, tasks
from discord.utils import get

client = commands.Bot(command_prefix='any')



@client.event
async def on_ready():
    await client.change_presence(status=discord.Status.online, activity=discord.Activity(type=1, name='Whatever', url='CAN PUT YOUR WEBSITE OR WHATEVER'))
    print('Bot is ready')


@client.command()
async def ping(ctx):
    await ctx.send(f'waturr! {round(client.latency * 1000)}ms')




# for welcome
@client.event
async def on_member_join(member):
    print(f'{member} has joined the server.')
    embed = discord.Embed(description=f"welcome to the server! waturr!!!!")
    embed.set_thumbnail(url=f"{member.avatar_url}")
    embed.set_author(name=f"{member.name}", icon_url=f"{member.avatar_url}")
    embed.set_footer(text=f"{member.guild}", icon_url=f"{member.guild.icon_url}")
    embed.timestamp=datetime.datetime.utcnow()
    channel = client.get_channel(id=id)
    await channel.send(embed=embed)



# for moderations avatar and stuff
for filename in os.listdir('./cogs'):
    if filename.endswith('.py'):
        client.load_extension(f'cogs.{filename[:-3]}')


# if you wanted to use emote reaction role giving thingy smh
"""
@client.event
async def on_raw_reaction_add(payload):
    message_id = payload.message_id
    if message_id == use message id:
        guild_id = payload.guild_id
        guild = discord.utils.find(lambda  g: g.id == guild_id, client.guilds)

        if payload.emoji.name == "emote":
            role = discord.utils.get(guild.roles, name='role name')
        elif payload.emoji.name == "emote":
            role = discord.utils.get(guild.roles, name='role name')
        else:
            role = discord.utils.get(guild.roles, name=payload.emoji.name)

        if role is not None:
            member = discord.utils.find(lambda m: m.id == payload.user_id, guild.members)
            if member is not None:
                await member.add_roles(role)
                print("done")
            else:
                print("member not found")
        else:
            print("role not found")



@client.event
async def on_raw_reaction_remove(payload):
    pass

"""



client.run("TOKEN")

