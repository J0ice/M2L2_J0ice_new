import discord
from discord.ext import commands
from bot_logic import *
import random
import requests
import os


intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix='$', intents=intents)

@bot.event
async def on_ready():
    print(f'We have logged in as {bot.user}, type $cmd to interact.')

@bot.command()
async def hello(ctx):
    await ctx.send(f'Sup Im {bot.user}')

@bot.command()
async def brainrot_mode(ctx):
    await ctx.send(f'ngl imo ts pmo fr🥀')

@bot.command()
async def my_password(ctx):
    await ctx.send(gen_pass(10))

@bot.command()
async def send_a_random_emoji(ctx):
    await ctx.send(gen_emodji())

@bot.command()
async def flip_a_coin(ctx):
    await ctx.send(f"you get... {flip_coin()}")

@bot.command('cmd')
async def cmd(ctx):
    with open('help.txt', 'r', encoding='utf-8') as f:
        await ctx.send(f.read())

@bot.command()
async def meme(ctx):
    # with open('images/meme1.jpg', 'rb') as f:
    #     picture = discord.File(f)
    img_name = random.choice(os.listdir('images'))
    with open(f'images/{img_name}', 'rb') as f:
        picture = discord.File(f)
    await ctx.send(file=picture)

@bot.command()
async def animal_memes(ctx):
    # with open('images/meme1.jpg', 'rb') as f:
    #     picture = discord.File(f)
    img_name = random.choice(os.listdir('animals'))
    with open(f'animals/{img_name}', 'rb') as f:
        picture = discord.File(f)
    await ctx.send(file=picture)

@bot.command()
async def random_memes(ctx):
    # with open('images/meme1.jpg', 'rb') as f:
    #     picture = discord.File(f)
    img_name = random.choice(os.listdir('random_meme'))
    with open(f'random_meme/{img_name}', 'rb') as f:
        picture = discord.File(f)
    await ctx.send(file=picture)


def get_duck_image_url():    
    url = 'https://random-d.uk/api/random'
    res = requests.get(url)
    data = res.json()
    return data['url']

@bot.command('solution')
async def solution(ctx):
    with open('Solution2.txt', 'r', encoding='utf-8') as f:
        await ctx.send(f.read())

@bot.command('i_want_to_know')
async def i_want_to_know(ctx):
    with open('Solution3.txt', 'r', encoding='utf-8') as f:
        await ctx.send(f.read())
    with open('Instructions/instructionss.png', 'rb') as f:
        picture = discord.File(f)
    await ctx.send(file=picture)

@bot.command()
async def final(ctx):
    with open('Instructions/finalphoto.png', 'rb') as f:
        picture = discord.File(f)
    await ctx.send(file=picture)

@bot.command('duck')
async def duck(ctx):
    '''Setelah kita memanggil perintah bebek (duck), program akan memanggil fungsi get_duck_image_url'''
    image_url = get_duck_image_url()
    await ctx.send(image_url)

bot.run("")