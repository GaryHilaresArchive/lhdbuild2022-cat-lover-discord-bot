import requests
import discord
from discord.ext import commands

@commands.command(name='forever', brief='Gets a random cat fact and an image.')
async def cat(ctx, *args):
    cat_fact = requests.get('https://meowfacts.herokuapp.com/').json()['data'][0]
    cat_image_link = requests.get('https://api.thecatapi.com/v1/images/search').json()[0]['url']
    img = discord.Embed()
    img.set_image(url=cat_image_link)
    await ctx.channel.send(cat_fact, embed=img)