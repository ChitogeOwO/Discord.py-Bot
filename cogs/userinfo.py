import discord
from discord import app_commands
from discord.ext import commands

class UserInfo(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @app_commands.command(name="userinfo", description="Show information about a user")
    async def userinfo(self, interaction: discord.Interaction, user: discord.Member = None):
        user = user or interaction.user  # default to the command user

        embed = discord.Embed(
            title=f"User Info - {user}",
            color=discord.Color.green(),
            timestamp=interaction.created_at
        )

        embed.set_thumbnail(url=user.display_avatar.url)

        embed.add_field(name="👤 Username", value=f"{user.name}", inline=True)
        embed.add_field(name="🆔 User ID", value=user.id, inline=True)
        embed.add_field(name="📅 Account Created", value=user.created_at.strftime("%Y-%m-%d %H:%M:%S"), inline=False)

        if isinstance(user, discord.Member):  # Only if in guild
            embed.add_field(name="📥 Joined Server", value=user.joined_at.strftime("%Y-%m-%d %H:%M:%S"), inline=False)
            roles = [role.mention for role in user.roles if role.name != "@everyone"]
            embed.add_field(name="🎭 Roles", value=", ".join(roles) if roles else "No roles", inline=False)
            embed.add_field(name="💻 Top Role", value=user.top_role.mention, inline=True)

        await interaction.response.send_message(embed=embed)

async def setup(bot):
    await bot.add_cog(UserInfo(bot))
