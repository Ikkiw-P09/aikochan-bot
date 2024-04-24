import os
from dotenv import load_dotenv
import discord
from discord.ext import commands  
load_dotenv()

# Retrieve Discord bot token and channel ID from environment variables
TOKEN = os.getenv('DISCORD_TOKEN')
CHANNEL_ID = os.getenv('ANNOUNCEMENT_CHANNEL_ID')

# Specify Intents (events your bot wants to listen to)
intents = discord.Intents.default()
intents.members = True  # Required for handling message content

# Create a Bot instance with the command prefix and intents
client = commands.Bot(command_prefix='/', intents=intents)

#@client.command()  # Keep for traditional slash commands

async def hello(ctx):
    await ctx.channel.send("hi")  

async def paymenow(ctx):
    await ctx.send("Please enter the title of your announcement:")
    title = await client.wait_for('message', check=lambda m: m.author == ctx.author)
    
    await ctx.channel.send(title)
    
client.run(TOKEN)
