import os
import discord
from discord.ext import commands
from decouple import config

intents = discord.Intents.all()

#define o prefixo do bot e suas permições
bot = commands.Bot(command_prefix='/', intents=intents)


async def teste_cog():
    await bot.load_extension('cogs.manager')


#conecta o bot com o token
token_bot = config('token')
#executa o bot
bot.run(token_bot)
