import discord
from discord.ext import commands
from bot_logic import *

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix='$', intents=intents)

@bot.event
async def on_ready():
    print(f'We have logged in as {bot.user}')

@bot.command()
async def hello(ctx):
    await ctx.send(f'Hai! Saya adalah bot {bot.user}!')
@bot.command()
async def senyum(ctx):
    await ctx.send(gen_emoji())

@bot.command()
async def pasw(ctx):
    await ctx.send(gen_pass(10))

bot.run("MTM2ODIwNzMxNTQyOTQ5NDc5NA.GtI75A.poGXjyl8YBRs4H2qBYv4Uy41bokEjIiqNMwRIg")