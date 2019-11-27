import discord 
from discord.ext import commands 


class nick(commands.Cog, name= "Change nick "):
    def __init__(self , client):
        self.client = client

    @commands.Cog.listener()
    async def on_ready(self):
        print("cogs are loaded for nick")

    
    @commands.Cog.listener()
    async def on_member_update(self , before, after):
        nick = after.nick 
        if nick:
            if nick.lower().count("waturr")> 0:
                last = before.nick
                if last :
                    await after.edit(nick=last)
                else:
                    await after.edit(nick="smh")





def setup(client):
    client.add_cog(nick(client))

