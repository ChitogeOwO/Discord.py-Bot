import discord
from discord.ext import commands
from discord import app_commands
import os

# Enable intents
intents = discord.Intents.default()
intents.message_content = True
intents.members = True

# Create bot (commands.Bot also supports slash commands through tree)
bot = commands.Bot(command_prefix="!", intents=intents)

async def on_app_command_error(interaction: discord.Interaction, error: app_commands.AppCommandError):
    if isinstance(error, app_commands.MissingPermissions):
        await interaction.response.send_message(
            "🚫 You do not have permission to use this command.",
            ephemeral=True
        )
    elif isinstance(error, app_commands.BotMissingPermissions):
        await interaction.response.send_message(
            "❌ I do not have the required permissions to run this command.",
            ephemeral=True
        )
    elif isinstance(error, app_commands.CommandNotFound):
        await interaction.response.send_message(
            "⚠️ That command does not exist.",
            ephemeral=True
        )
    elif isinstance(error, app_commands.CheckFailure):
        await interaction.response.send_message(
            "🚫 You do not meet the requirements to use this command.",
            ephemeral=True
        )
    else:
        await interaction.response.send_message(
            "⚠️ An unexpected error occurred. Please try again later.",
            ephemeral=True
        )
        # Log full error in console for debugging
        raise error

@bot.event
async def on_ready():
    print(f"✅ Logged in as {bot.user} (ID: {bot.user.id})")

    # Load cogs
    for filename in os.listdir("./cogs"):
        if filename.endswith(".py"):
            await bot.load_extension(f"cogs.{filename[:-3]}")

    # Sync slash commands globally
    try:
        synced = await bot.tree.sync()
        print(f"⚡ Synced {len(synced)} slash command(s)")
    except Exception as e:
        print(f"❌ Error syncing commands: {e}")

bot.run("Token") 
