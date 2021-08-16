# bot.py
import os
import random
import discord
from discord import message
import requests
import json
from quotes import list_quotes, cat_images

from discord.ext import commands
from dotenv import load_dotenv
from discord.utils import get
from discord_components import DiscordComponents, Button, ButtonStyle, InteractionType
from discord.ext import commands
from discord.ext.commands import Bot


load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')

bot = commands.Bot(command_prefix='$')
client = discord.Client()



@bot.event
async def on_ready():
    print(f'{bot.user.name} has connected to Discord!')
    print('Connected to bot: {}'.format(bot.user.name))
    print('Bot ID: {}'.format(bot.user.id))

    await bot.change_presence(status=discord.Status.online, activity=discord.Game('$command'))




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
    print('Code run successful!')
    await ctx.send('Here is your dice :game_die: :')
    await ctx.send(', '.join(dice))

#create channel
@bot.command(name='create-channel', help = 'Create channel + {channel_name}')
@commands.has_role('Admin')
async def create_channel(ctx, *, channel_name):
    guild = ctx.guild
    existing_channel = discord.utils.get(guild.channels, name=channel_name)
    if not existing_channel:
        print(f'Created a new channel: {channel_name}')
        await guild.create_text_channel(channel_name)

@bot.event
async def on_command_error(ctx, error):
    if isinstance(error, commands.errors.CheckFailure):
        await ctx.send('You do not have the correct role for this command.')



#roll number from 1 to picked number

@bot.command(name='roll', help = 'Roll a random picked number start from 1')
async def random_number(ctx, number: int):
    rnumber = random.randint(1,number)
    print('Code run successful!')

    number_emoji =[':zero:',':one:',':two:',':three:',':four:',':five:',':six:',':seven:',':eight:',':nine:']
    emoji = []
    while rnumber  !=0:
        nnumber = rnumber % 10
        rnumber = int(rnumber / 10)
        emoji.insert(0,number_emoji[nnumber])
    await ctx.send(' '.join(emoji))


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
    emoji = ':like:'
    bot_reply = random.choice(arg)
    await ctx.send(bot_reply)
    

# weather


# api_key = '17f479c11d7d372baa39d9a5e3de5f1a'
# command_prefix = '$weather'


# color = 0xFF6500
# key_features = {
#     'temp' : 'Nhiệt độ °F',
#     'feels_like' : 'Feels Like',
#     'temp_min' : 'Nhiệt độ thấp nhất',
#     'temp_max' : 'Nhiệt độ cao nhất'
# }

# def parse_data(data):
#     del data['humidity']
#     del data['pressure']
#     return data

# def weather_message(data, location):
#     location = location.title()
#     message = discord.Embed(
#         title=f'{location} weather',
#         description=f'Thời tiết hôm nay tại {location}.',
#         color=color
#     )
#     for key in data:
#         message.add_field(
#             name=key_features[key],
#             value=str(data[key]),
#             inline=False
#         )
#     return message

# def error_message(location):
#     location = location.title()
#     return discord.Embed(
#         title='Error',
#         description=f'Không thể tìm thấy thời tiết tại {location}.',
#         color=color
#     )



# @bot.event
# async def on_message(message):
#     if message.author != bot.user and message.content.startswith(command_prefix):
#         location = message.content.replace(command_prefix, '').lower()
#         url = f'http://api.openweathermap.org/data/2.5/weather?q={location}&appid={api_key}&units=imperial'
#         try:
#             data = parse_data(json.loads(requests.get(url).content)['main'])
#             await message.channel.send(embed=weather_message(data, location))
#         except KeyError:
#             await message.channel.send(embed=error_message(location))


#test embed



@bot.command(name='quotes', help='show embed')
async def embed(ctx):
    #discription
    embed=discord.Embed(title="Quote Of The Day :love_letter: ", description=random.choice(list_quotes), color=discord.Color.random())

    #set author
    embed.set_author(name=ctx.author.display_name, url="https://khoahoang.net", icon_url=ctx.author.avatar_url)
    
    #set thumbnail
    embed.set_thumbnail(url=random.choice(cat_images))

    #set field

    #field 1
    embed.add_field(name="Random quote ", value="From LazyPythonBot with love :heart_on_fire: ")
    #field 2

    #field 3
    #embed.add_field(name="Field 3 Title", value="It is inline with Field 2", inline=True)
    #
    


    await ctx.send(embed=embed)


@bot.command(name='command', help='show list command')
async def help(ctx):
    embed=discord.Embed(title='Help Command')

    embed.set_author(name=ctx.author.display_name, url="https://khoahoang.net", icon_url=ctx.author.avatar_url)

    embed.add_field(name="Danh sách lệnh của bot: ", value="`command\n` `bot\n` `chuibot\n` `quotes\n` `create-channel\n` `roll\n` `roll_dice\n` `khoa\n` `nhat\n` `tam\n`", inline=False)
    embed.set_footer(text="Sử dụng $command {lệnh} để xem chi tiết.")

    await ctx.send(embed=embed)



bot.run(TOKEN)
