# bot.py
import os
import random
import discord

from discord.ext import commands
from dotenv import load_dotenv

load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')

bot = commands.Bot(command_prefix='!')
client = discord.Client()

@bot.event
async def on_ready():
    print(f'{bot.user.name} has connected to Discord!')


@bot.command(name='bot', help='Call bot')
async def test(ctx):
    bot_chui = [
        'Gọi cc',
        'Gọi clgt?',
        'Gọi cái giè?',
        'Bố mày đây, gọi cc',

    ]

    response = random.choice(bot_chui)
    await ctx.send(response)


@bot.command(name='roll_dice', help='Simulates rolling dice.')
async def roll(ctx, number_of_dice: int, number_of_sides: int):
    dice = [
        str(random.choice(range(1, number_of_sides + 1)))
        for _ in range(number_of_dice)
    ]
    await ctx.send(', '.join(dice))



@bot.command(name='roll', help = 'Roll a random picked number')
async def random_number(ctx, number: int):
    rnumber = [
        str(random.choice(range(1, number+1)))
    ]
    await ctx.send(', '.join(rnumber))

bot.run(TOKEN)