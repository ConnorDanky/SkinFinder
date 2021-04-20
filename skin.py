import discord
import json

from discord.ext import commands

# mcuuid-1.0.1 - in requirements.txt
from mcuuid import MCUUID
from mcuuid.tools import is_valid_minecraft_username

#Akoots cool helper tool
import util.io_util as io_util


intents = discord.Intents().all()
skin = commands.Bot(command_prefix = "/", intents = intents)

@skin.event
async def on_ready():
    print("SkinBot is online.")
    await skin.change_presence(activity=discord.Game(name = "Looking up Skins!"))

@skin.event
async def on_message(msg):


    await skin.process_commands(msg)


@skin.command()
async def image(ctx,*,entry):

    switch = is_valid_minecraft_username(entry)

    if (switch == True):
        Player = MCUUID(name = entry)
        id_ = Player.uuid


        skin_Embed = discord.Embed(
            colour = (discord.Colour.green()),
            title = entry,
            description = id_
        )
        
        
        skin_Embed.set_footer(icon_url = ctx.author.avatar_url,text = f"Requested by {ctx.author}")
        skin_Embed.set_image(url = f'https://visage.surgeplay.com/full/512/{id_}.png')
        await ctx.send(embed = skin_Embed)

token = io_util.load_json('auth.json')['token']

skin.run(token)
