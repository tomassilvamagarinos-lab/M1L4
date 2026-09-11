import discord
from discord.ext import commands
from bot_logic import gen_password
import os
import random

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix='*', intents=intents)

@bot.event
async def on_ready():
    print(f'We have logged in as {bot.user}')

@bot.command()
async def hello(ctx):
    await ctx.send(f'Hola, soy un bot {bot.user}!')

@bot.command()
async def heh(ctx, count_heh = 5):
    await ctx.send("he" * count_heh)

@bot.command()
async def bye(ctx):
    await ctx.send("\U0001f642")
    
@bot.command()
async def password(ctx):
    password = gen_password()
    await ctx.send(f'Tu contraseña es: {password}')
    
@bot.command()
async def mem(ctx):
    with open('images/mem1.png', 'rb') as f:
        picture = discord.File(f)
    await ctx.send(file=picture)
    
@bot.command()
async def meme(ctx):
    
    img_name = random.choice(os.listdir('images'))
    
    with open(f'images/{img_name}', 'rb') as f:
        picture = discord.File(f)
        await ctx.send(file=picture)
   
    await ctx.send(file=picture)

bot.run("key")
