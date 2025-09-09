import discord
from discord import app_commands
from discord.ext import commands

class Clear(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @app_commands.command(name="clear", description="Delete a number of messages from the channel")
    @app_commands.default_permissions(manage_messages=True)  # 👈 hides from non-mods
    async def clear(self, interaction: discord.Interaction, amount: int = 5):
        if amount < 1:
            await interaction.response.send_message("⚠️ You must delete at least 1 message.", ephemeral=True)
            return

        # Defer response since purge can take time
        await interaction.response.defer(ephemeral=True)

        deleted = await interaction.channel.purge(limit=amount)
        await interaction.followup.send(f"🧹 Cleared {len(deleted)} messages.", ephemeral=True)

async def setup(bot):
    await bot.add_cog(Clear(bot))
