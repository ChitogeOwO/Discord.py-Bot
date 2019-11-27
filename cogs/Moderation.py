import discord
from discord.ext import commands

class mods(commands.Cog, name = "Moderation"):

    def __init__(self, client):
        self.client = client

    @commands.Cog.listener()
    async def on_ready(self):
        print('Cogs are loaded for moderation')


    @commands.command()
    @commands.has_permissions(manage_messages=True)
    async def clear(self , ctx, amount : int):
        await ctx.channel.purge(limit=amount)
    

    
    @clear.error
    async def clear_error(self, ctx, error):
        if isinstance(error, commands.MissingRequiredArgument):
            await ctx.send('please specify an amount of messages to delete.')




    @commands.command()
    @commands.has_permissions(kick_members=True)
    async def kick(self, ctx, member : discord.Member, *,reason=None):
        await member.kick(reason=reason)
        await ctx.send(f'{member.name} has been kicked from the server')


    @commands.command()
    @commands.has_permissions(ban_members=True)
    async def ban(self ,ctx, member : discord.Member, *,reason=None):
        await member.ban(reason=reason)
        await ctx.send(f'Banned {member.memtion}')
#       await ctx.send('A member has been banned from the group')


    @commands.command()
    @commands.has_permissions(ban_members=True)
    async def unban(self , ctx, *,member):
        banned_users = await ctx.guild.bans()
        member_name, member_discriminator = member.split('#')

        for ban_entry in banned_users:
            user = ban_entry.user

            if (user.name, user.discriminator) == (member_name, member_discriminator):
                await ctx.guild.unban(user)
                await ctx.send(f'unbanned {user.memtion}')
                return




def setup(client):
    client.add_cog(mods(client))

    