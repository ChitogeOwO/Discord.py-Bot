import discord
from discord.ext import commands

class error(commands.Cog, name="error handler"):
    def __init__(self, client):
        self.client = client

    

    @commands.Cog.listener()
    async def on_ready(self):
        print('cogs are loaded for error handling')

    @commands.Cog.listener()
    async def on_command_error(self , ctx, error):
        if isinstance(error, commands.CommandNotFound):
            await ctx.send('Command not found')

def setup(client):
    client.add_cog(error(client))
