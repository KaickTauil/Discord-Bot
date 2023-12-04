import discord
from discord.ext import commands

class Image(commands.Cog):
    """Works with images"""

    def __init__(self, bot):
        self.bot = bot

    @commands.command(name='foto', help='Gera um card com uma imagem aleatória')
    async def random_img(ctx):
        url = 'https://picsum.photos/1920/1080'

        embed = discord.Embed(title="Resultado da imagem", description="a busca é totalmente aleatória", color=0x81C3D7)
        
        embed.set_author(name = self.bot.user.name, icon_url = self.bot.user.avatar.url)

        embed.add_field(name = 'API', value = 'usamos a api do picsum')
        embed.add_field(name = 'Parâmetros', value = '{largura}/{altura}')
        embed.add_field(name = 'Exemplo', value = url, inline=False)

        embed.set_image(url = url)

        embed.set_footer(text = f'Feito por {self.bot.user.name}', icon_url = self.bot.user.avatar.url)

        await ctx.send(embed = embed)

def setup(bot):
    bot.add_cog(Image(bot))
