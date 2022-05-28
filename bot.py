import os
import discord
from discord.ext import commands
from decouple import config

bot = commands.Bot("!")

bot.load_extension("commands.commands_conditions")
bot.load_extension("commands.messages_eng")
bot.load_extension("commands.messages_ptbr")


TOKEN = config("TOKEN")
bot.run(TOKEN)
