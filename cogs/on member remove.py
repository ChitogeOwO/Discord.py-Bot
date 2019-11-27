import discord
from discord.ext import commands

class onmemberremove(commands.Cog, name="member remove from the server"):
    def __init__(self, client):
        self.client = client

    @commands.Cog.listener()
    async def on_ready(self):
        print('cogs are loaded for removing members')

    
    @commands.Cog.listener()
    async def on_member_remove(self, member):
        print(f'{member} has left the server.')
    

def setup(client):
    client.add_cog(onmemberremove(client))
