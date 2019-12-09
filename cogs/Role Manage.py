import discord 
from discord.ext import commands 
import discord.utils

class role(commands.Cog, name= "Roles Manage"):
    def __init__(self , client):
        self.client = client

    @commands.Cog.listener()
    async def on_ready(self):
        print("cogs are loaded for roles")


    @commands.command()
    @commands.has_permissions(manage_roles=True)
    async def role(self, ctx, user: discord.Member , role: discord.Role=None):
        if role not in user.roles:
            await user.add_roles(role)
            await ctx.send(f"{user.mention}, {ctx.author.name} has gave you a role called {role.name}")
            print(f"{role.name} role added to {user}")
        else:
            await ctx.send("Member already has the role")


    @commands.command()
    @commands.has_permissions(manage_roles=True)
    async def derole(self, ctx, user: discord.Member , role: discord.Role):
        await user.remove_roles(role)
        await ctx.send(f"{user.mention}, {ctx.author.name} has removed your role called {role.name}")
        print(f"{role.name} role removed from {user}")
        

def setup(client):
    client.add_cog(role(client))

