import requests
import discord
from discord.ext import commands

class Crypto(commands.Cog):
    """Works with cryptocurrancy"""

    def __init__(self, bot):
        self.bot = bot

    @commands.command(help='Informa o valor de determinada moeda ao informar: "/binance coin base"')
    async def binance(self, ctx, coin, base):
        try:
            response = requests.get(f'https://api.binance.com/api/v3/ticker/price?symbol={coin.upper()}{base.upper()}')
            data = response.json()
            price = data.get('price')

            if price:
                await ctx.send(f'O valor do par {coin}/{base} é {price}')
            else:
                await ctx.send(f'O par {coin}/{base} é inválido')

        except Exception as error:
            await ctx.send('Algo deu errado')
            print(error)

def setup(bot):
    bot.add_cog(Crypto(bot))
