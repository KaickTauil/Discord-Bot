from discord.ext import commands
import discord

class Talk(commands.Cog):
    """Talks with user"""

    def __init__(self, bot):
        self.bot = bot
    
    @commands.command(name='funcionou', help='Informa se o bot está funcionando')
    async def works(self, ctx):
        name = ctx.author.name
        resp = "funcionou paizin " + name

        await ctx.send(resp)
    
    @commands.command(name='inverta', help='Inverte a mensagem enviada')
    async def inverse(self, ctx, message):
        await ctx.send(message[::-1]) 

    @commands.command(name='priv', help='Envia uma mensagem privada')
    async def secret(self, ctx, message):
        message.upper()
        try:
            if message == 'pog':
                await ctx.author.send('poggerrrrrssss')
            elif message == 'nog':
                await ctx.author.send('noggers....')
        except discord.errors.Forbidden:
            await ctx.send('Hablite receber mensagens de qualquer pessoa do servidor')

def setup(bot):
    bot.add_cog(Talk(bot))


    