import discord
from discord import app_commands
from discord.ext import commands

class ServerIcon(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @app_commands.command(name="servericon", description="Show the server's icon")
    async def servericon(self, interaction: discord.Interaction):
        guild = interaction.guild

        if guild.icon:
            embed = discord.Embed(
                title=f"{guild.name}'s Icon",
                color=discord.Color.blurple(),
                timestamp=interaction.created_at
            )
            embed.set_image(url=guild.icon.url)
            await interaction.response.send_message(embed=embed)
        else:
            await interaction.response.send_message("❌ This server has no icon.", ephemeral=True)

async def setup(bot):
    await bot.add_cog(ServerIcon(bot))
