from discord.ext import commands
import discord

class React(commands.Cog):
    """Work with reactions"""

    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_reaction_add(self, reaction, user):
        if reaction.emoji == '🤯':
            role = user.guild.get_role(1177009534666014824)
        elif reaction.emoji == '😪':
            role = user.guild.get_role(1177009609433677934)

        await user.add_roles(role)

def setup(bot):
    bot.add_cog(React(bot))