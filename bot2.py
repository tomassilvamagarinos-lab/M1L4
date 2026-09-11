import discord
from discord.ext import commands
from bot_logic import gen_password


intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix='$', intents=intents)

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
async def no(ctx):
   await ctx.send("si")

@bot.command()
async def todo_bien?(ctx)
 await ctx.send("bien, y tu?")

@client.tree.command()
@app_commands.describe(member='The member you want to get the joined date from; defaults to the user who uses the command')
async def joined(interaction: discord.Interaction, member: Optional[discord.Member] = None):
    """Says when a member joined."""
     member = member or interaction.user
 await interaction.response.send_message(f'{member} joined {discord.utils.format_dt(member.joined_at)}')

@bot.command()
async def password(ctx):
    password = gen_password()
    await ctx.send(f'La contraseña generada es: {password}')

bot.run("key")
