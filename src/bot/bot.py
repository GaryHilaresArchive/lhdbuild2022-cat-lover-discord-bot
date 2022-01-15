from discord.ext import commands
from bot.commands import cat

discord_client = commands.Bot(command_prefix="cats!")
discord_client.add_command(cat)