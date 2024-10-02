import discord
from discord.ext import commands
from bot_logic import gen_pass

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix='$', intents=intents)

@bot.event
async def on_ready():
    print(f'We have logged in as {bot.user}')

@bot.command()
async def hello(ctx):
    await ctx.send(f'Hai! Saya adalah bot {bot.user}!') # $hello

@bot.command()
async def pasw(ctx):
    await ctx.send(gen_pass(10)) # $pasw

@bot.command()
async def zakkir(ctx):
    await ctx.send("Hi! nama saya zakkir!!!") # $zakkir

@bot.command()
async def heh(ctx, count_number = 10, nabila=10):
    await ctx.send("he" * count_number + nabila) # $heh 100 60 


bot.run("")
