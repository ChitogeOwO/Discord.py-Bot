import discord
from discord.ext import commands

class help(commands.Cog , name ="help"):
    def __init__(self , client):
        self.client = client

    @commands.Cog.listener()
    async def on_ready(self):
        print('cogs loaded for help command')

    @commands.command()
    async def help(self , ctx, *, command = None):
        if command==None:
            embed = discord.Embed(color=discord.Color.red(),title="Incorrect command")
            embed.add_field(name = "Correct Command", value="help mod\n help info \n help ai \n help fact")
            await ctx.send(embed=embed)

        elif command=="mod":
            embed = discord.Embed(color=discord.Color.green(), title= "Mod Commands")
            embed.add_field(name="Available Commands", value="clear[number] \n kick[@user] \n ban[@user] \n unban[@user] \n role[@user]role name \n derole[user]role name")
            await ctx.send(embed = embed)

        elif command=="info":
            embed = discord.Embed(color=discord.Color.green(), title= "info Commands")
            embed.add_field(name="Available Commands", value="userinfo[@user] \n serverinfo \n avatar[@user]")
            await ctx.send(embed=embed)

        elif command=="ai":
            embed = discord.Embed(color=discord.Color.green(), title= "ai Commands")
            embed.add_field(name="Available Commands You dont need to use prefix", value="loli \n ques")
            await ctx.send(embed=embed)

        elif command=="fact":
            embed = discord.Embed(color=discord.Color.green(),title = "fact commands")
            embed.add_field(name="Available Commands", value="fact dog \n fact cats \n fact panda \n fact fox \n fact bird \n fact koala")
            await ctx.send(embed = embed)

        else:
            pass

def setup(client):
    client.add_cog(help(client))