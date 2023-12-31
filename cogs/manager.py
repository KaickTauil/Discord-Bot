import discord
from discord.ext import commands
from discord.ext.commands.errors import MissingRequiredArgument, CommandNotFound

class Manager(commands.Cog):
    """Bot manager's events"""

    def __init__(self, bot):
        self.bot = bot
    
    @commands.Cog.listener()
    async def on_ready(self):
        print('funcionou paizin')   

    @commands.Cog.listener()
    async def on_message(self, message):
        if message.author == self.bot.user:
            return
        if "merda" in message.content:
            await message.channel.send(f'eeeee rapaz, se acalme {message.author.name}')

        await bot.process_commands(message)

    @commands.Cog.listener()
    async def on_command_error(self, ctx, error):
        if isinstance(error, MissingRequiredArgument):
            await ctx.send('Favor enviar todos os argumentos, digite /help para conferir os comandos')
        elif isinstance(error, CommandNotFound):
            await ctx.send('O comando não existe, digite /help para conferir os comandos')
        else:
            raise error

async def setup(bot):
    await bot.add_cog(Manager(bot))
 