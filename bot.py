import discord
from discord.ext import commands
from main import gen_pass
import random
import os
import requests

# Membaca token dari file token.txt
with open("token.txt", "r") as f:
    token = f.read()

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix='$', intents=intents)

@bot.event
async def on_ready():
    print(f'We have logged in as {bot.user}')

@bot.command()
async def hello(ctx):
    await ctx.send(f'Hi! I am a bot {bot.user}!')

@bot.command()
async def repeat(ctx, times: 3, content='repeating...'):
    """Repeats a message multiple times."""
    for i in range(times):
        await ctx.send(content)

@bot.command()
async def heh(ctx, count_heh = 5):
    await ctx.send("he" * count_heh)

@bot.command()
async def passw(ctx, panjang = 5):
    await ctx.send(gen_pass(panjang))

@bot.command()
async def mem(ctx):
    img_name = random.choice(os.listdir('images'))
    with open(f'images/{img_name}', 'rb') as f:
        picture = discord.File(f)
    await ctx.send(file=picture)

animal = {
    'animal1.jpg': 5, #common
    'animal2.jpg': 2, #uncommon
    'animal3.jpg': 1  #rare
}

def get_weighted_random_meme(animal):
    weighted_memes = []
    for animal, rarity in animal.items():
        weighted_memes.extend([animal] * rarity)
    return random.choice(weighted_memes)

@bot.command()
async def anim(ctx):
    anim_name = get_weighted_random_meme(animal)
    with open(f'animals/{anim_name}', 'rb') as f:
        picture = discord.File(f)
    await ctx.send(file=picture)
    
def get_duck_image_url():    
    url = 'https://random-d.uk/api/random'
    res = requests.get(url)
    data = res.json()
    return data['url']

@bot.command('duck')
async def duck(ctx):
    '''Setelah kita memanggil perintah bebek (duck), program akan memanggil fungsi get_duck_image_url'''
    image_url = get_duck_image_url()
    await ctx.send(image_url)

bot.run(token)
