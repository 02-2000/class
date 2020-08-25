from discord.ext import commands
import discord

bot = commands.Bot(command_prefix='d!')

bot.remove_command('help')

class class(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

def setup(bot):
    bot.add_cog(class(bot))
