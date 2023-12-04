from discord.ext import commands
import datetime
import discord

class Datetime(commands.Cog):
    """Works with datetime"""

    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_ready(self):
        self.current_time.start()

    @tasks.loop(minutes=20)
    async def current_time(self):
        now = datetime.datetime.now()
        now = now.strftime('atualmente %H:%M:%S em Itarapucaiba-BA')

        channel = self.bot.get_channel(1174704174601097258)

        await channel.send(now)

def setup(bot):
    bot.add_cog(Datetime(bot))
 