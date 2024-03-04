import discord
from discord.ext import commands
import keys

intents = discord.Intents.all()
client =  commands.Bot(command_prefix = '!', intents = intents)

@client.event
async def on_ready():
    print("Bot is ready :kek:")

@client.event
async def on_reaction_add(reaction, user):
    if(str(reaction.message.author) in ["victordore", "tassy1262", "thefish123", "Pingrage Bot#1072"] and str(reaction.emoji) in ["<:pingrage:748579412450082837>"]):
        channel = client.get_channel(1214141531905200138)
        await channel.send(user.mention + "<:pingrage:748579412450082837>")

client.run(keys.BOTTOKEN)
