import discord
from discord.ext import commands
import urllib.parse
from revChatGPT.ChatGPT import Chatbot


client = commands.Bot(command_prefix='/', intents=discord.Intents.all())    # bot prefix is "/" but that can change

@client.event
async def on_ready():
    print(f'{client.user.name} has connected to Discord!')  # prints something when the bot successfully initialized


maps = {    # links a tarkov map name with the link leading to its image
    'customs': 'https://static.wikia.nocookie.net/escapefromtarkov_gamepedia/images/5/55/CustomsLargeExpansionGloryMonki.png/revision/latest?cb=20221117130235',
    'customs_3D': 'https://static.wikia.nocookie.net/escapefromtarkov_gamepedia/images/0/0b/CustomsMapRealNorthColour_Reemr.png/revision/latest?cb=20211215150401',
    'dorms': 'https://static.wikia.nocookie.net/escapefromtarkov_gamepedia/images/9/96/DormRoomsMap.jpg/revision/latest?cb=20200328162326',
    'factory': 'https://static.wikia.nocookie.net/escapefromtarkov_gamepedia/images/9/94/Factory_loot.png/revision/latest?cb=20221130011116',
    'factory_3D': 'https://static.wikia.nocookie.net/escapefromtarkov_gamepedia/images/c/cd/Factory_3D_b_Johnny_Tushonka.jpg/revision/latest?cb=20210704215141',
    'interchange': 'https://static.wikia.nocookie.net/escapefromtarkov_gamepedia/images/2/27/Interchange2DMapLorathor.jpg/revision/latest?cb=20220409224052',
    'interchange_3D': 'https://static.wikia.nocookie.net/escapefromtarkov_gamepedia/images/8/8e/Interchange3DMapMrYundaz.jpg/revision/latest?cb=20220409223309',
    'lighthouse': 'https://static.wikia.nocookie.net/escapefromtarkov_gamepedia/images/1/13/Jindouz_Lighthouse_Map_V1.png/revision/latest?cb=20230108073256',
    'lighthouse_3D': 'https://static.wikia.nocookie.net/escapefromtarkov_gamepedia/images/a/ab/Re3mrLighthouseIsometricDay-min.jpg/revision/latest?cb=20221230133844',
    'reserve_3D': 'https://static.wikia.nocookie.net/escapefromtarkov_gamepedia/images/3/38/Re3mrReserveCardinalNorthWikiVer.jpg/revision/latest?cb=20220127204615',
    'reserve': 'https://static.wikia.nocookie.net/escapefromtarkov_gamepedia/images/7/7c/JindouzReserve_v1_2dmap.png/revision/latest?cb=20221230141022',
    'reserve_3D': 'https://static.wikia.nocookie.net/escapefromtarkov_gamepedia/images/7/7c/JindouzReserve_v1_2dmap.png/revision/latest?cb=20221230141022',
    'shoreline': 'https://static.wikia.nocookie.net/escapefromtarkov_gamepedia/images/a/ac/Shoreline_Map_-_12.7.png/revision/latest?cb=20220910181732',
    'shoreline_3D': 'https://static.wikia.nocookie.net/escapefromtarkov_gamepedia/images/a/a1/ShorelineQuestsRe3mr.jpg/revision/latest?cb=20220829212546',
    'health': 'https://static.wikia.nocookie.net/escapefromtarkov_gamepedia/images/b/b1/ShorelineResortRoomsByreemr.png/revision/latest?cb=20220416155253',
    'streets': 'https://static.wikia.nocookie.net/escapefromtarkov_gamepedia/images/7/71/StreetsOfTarkov2DMapByJindouz.png/revision/latest?cb=20230118135014',
    'streets_3D': 'https://static.wikia.nocookie.net/escapefromtarkov_gamepedia/images/1/17/StreetsOfTarkov3DMapByRE3MR.jpg/revision/latest?cb=20230118100543',
    'woods': 'https://static.wikia.nocookie.net/escapefromtarkov_gamepedia/images/0/05/Glory4lyfeWoods_map_v4_marked.png/revision/latest?cb=20221203082625',
    'woods_3D': 'https://static.wikia.nocookie.net/escapefromtarkov_gamepedia/images/d/de/WikiWoodsRe3mr.jpg/revision/latest?cb=20220824190832'
    }

chatbot = Chatbot({     # initializing the ChatGPT instance that will be used to generate answers using Microsoft Login
  "email": "EMAIL",
  "password": "PASSWORD",
  "isMicrosoftLogin": True
})

''' Displays Escape from Tarkov maps
Input : name of the map required
Output : URL leading to the map asked for
'''
@client.command()
async def tarkovmap(ctx, map_name):
    if map_name in maps:
        await ctx.send(maps[map_name])
    else:
        await ctx.send("Invalid map name. Use the `listmaps` command to see all available maps.")


''' Image generation
Input : user prompt
Output : URL with the user prompt and some additions, that turns into a generated image
'''
@client.command()
async def imagine(ctx, *prompt):
    prompt = " ".join(prompt) + ", by Greg Rutkowski, masterpiece, trending on Artstation, 8K"  # usually produces better results, can be tuned
    prompt = urllib.parse.quote(prompt)
    await ctx.send(f"https://image.pollinations.ai/prompt/{prompt}")


''' ChatGPT answer
Input : user prompt
Output : ChatGPT answer, sent as a text message
'''
@client.command()
async def ask(ctx, *, prompt):
    response = chatbot.ask(prompt)
    await ctx.send(response["message"])


client.run("DISCORD_BOT_TOKEN")  # starts the bot
