import discord

class Smart(commands.Cog):
    """Smart commands"""

    def __init__(self, bot):
        self.bot = bot

def setup(bot):
    bot.add_cog(Smart(bot))
 