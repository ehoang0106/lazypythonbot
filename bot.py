# bot.py
import os
import random
import discord
import bj


from discord.ext import commands
from dotenv import load_dotenv

load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')

bot = commands.Bot(command_prefix='!')
client = discord.Client()

@bot.event
async def on_ready():
    print(f'{bot.user.name} has connected to Discord!')

#call bot
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

#call khoa
@bot.command(name='khoa', help='Khoa đẹp trai siêu cấp vũ trụ')
async def test(ctx):
    bot_chui = [
        'Khoa đẹp trai siu cấp dũ trụ',
        'gọi clg? Khoa đi chơi rồi',
        'Khoa đi rồi, !bot để gọi bot',
        'Gọi Khoa làm clgt, ãnh đi chơi rồi, tí quay lại',

    ]

    response = random.choice(bot_chui)
    await ctx.send(response)
#call nhat
@bot.command(name='nhat', help='Nhật xấu trai')
async def test(ctx):
    bot_chui = [
        'Nhật xấu trai, đánh dota sida',
        'Nhật đi hút cần với Khoa rồi, tí quay lại',
        'Nhật trả bài rồi, mai quay lại nha'

    ]

    response = random.choice(bot_chui)
    await ctx.send(response)

#call anh Tam
@bot.command(name='tam', help='anh Tâm gánh kèo')
async def test(ctx):
    bot_chui = [
        'Anh Tâm ơi cứu em',
        'Anh Tâm ơi cái này làm sao',
        'Tâm gánh tạ'

    ]

    response = random.choice(bot_chui)
    await ctx.send(response)


#roll dice with input number of dice and number of side
@bot.command(name='roll_dice', help='Simulates rolling dice. Must pick number of dice')
async def roll(ctx, number_of_dice: int):
    number_of_sides = 6
    dice = [
        str(random.choice(range(1, number_of_sides + 1)))
        for _ in range(number_of_dice)
    ]
    await ctx.send('Here is your dice :game_die: :')
    await ctx.send(', '.join(dice))

#create channel
@bot.command(name='create-channel')
@commands.has_role('Admin')
async def create_channel(ctx, channel_name='new-channel'):
    guild = ctx.guild
    existing_channel = discord.utils.get(guild.channels, name=channel_name)
    if not existing_channel:
        print(f'Creating a new channel: {channel_name}')
        await guild.create_text_channel(channel_name)

@bot.event
async def on_command_error(ctx, error):
    if isinstance(error, commands.errors.CheckFailure):
        await ctx.send('You do not have the correct role for this command.')

#roll number from 1 to picked number
@bot.command(name='roll', help = 'Roll a random picked number start from 1')
async def random_number(ctx, number: int):
    rnumber = [
        str(random.choice(range(1, number+1)))
    ]
    number_emoji =[':zero:,:one:,:two:,:three:,:four:,:five:,:six:']
    final_number = []
    
    
    await ctx.send(' '.join(rnumber))


@bot.command(name='chuibot', help = 'Toxic with bot')
async def test(ctx, *, arg):
    list_chui = [
        'dmm',
        'con cho bot',
         'bot ngu', 
         'fuck you', 
         'fuck u', 
         'stupid bot',
         'idiot',
         'fuck',
         'cho dien',
         'cho',
         'moron',
         'fucking stupid',
         'ga',
         'noob'
        ]
    for _ in list_chui:
        arg = [
            'chửi cái dmm',
            'mày thích chửi bố mày không, bố mày gọi cả hội giờ?',
            'solo không? chửi cc',
            'Shut the fuck up noob!',
            'Á à, con chó này dám chửi bố mày à?',
            'Anh em ơi, có thằng chó nó chửi em kìa',
            ]

    bot_reply = random.choice(arg)
    await ctx.send(bot_reply)

bot.run(TOKEN)