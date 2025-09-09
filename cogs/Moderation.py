import discord
from discord import app_commands
from discord.ext import commands

class Moderation(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    # Kick command
    @app_commands.command(name="kick", description="Kick a member")
    @app_commands.default_permissions(kick_members=True)  # 👈 Only users with kick perms see it
    async def kick(self, interaction: discord.Interaction, member: discord.Member, reason: str = "No reason provided"):
        await member.kick(reason=reason)
        await interaction.response.send_message(f"👢 {member.mention} has been kicked. Reason: {reason}")

    # Ban command
    @app_commands.command(name="ban", description="Ban a member")
    @app_commands.default_permissions(ban_members=True)  # 👈 Only users with ban perms see it
    async def ban(self, interaction: discord.Interaction, member: discord.Member, reason: str = "No reason provided"):
        await member.ban(reason=reason)
        await interaction.response.send_message(f"🔨 {member.mention} has been banned. Reason: {reason}")

    # Unban command
    @app_commands.command(name="unban", description="Unban a member by username#1234")
    @app_commands.default_permissions(ban_members=True)
    async def unban(self, interaction: discord.Interaction, user: str):
        banned_users = await interaction.guild.bans()
        name, discriminator = user.split("#")

        for ban_entry in banned_users:
            if (ban_entry.user.name, ban_entry.user.discriminator) == (name, discriminator):
                await interaction.guild.unban(ban_entry.user)
                await interaction.response.send_message(f"✅ Unbanned {ban_entry.user.mention}")
                return

        await interaction.response.send_message("❌ User not found in banned list.")

    # Clear messages
    @app_commands.command(name="clear", description="Delete a number of messages (default 5)")
    @app_commands.default_permissions(manage_messages=True)
    async def clear(self, interaction: discord.Interaction, amount: int = 5):
        await interaction.channel.purge(limit=amount)
        await interaction.response.send_message(f"🧹 Cleared {amount} messages.", ephemeral=True)

async def setup(bot):
    await bot.add_cog(Moderation(bot))
