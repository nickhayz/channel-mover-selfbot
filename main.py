
import discord
from discord.ext import commands
from dotenv import load_dotenv 
import os

load_dotenv()
#get env variable from .env in current directory
TOKEN = os.getenv('TOKEN')

bot = commands.Bot(command_prefix='>', self_bot=True)

@bot.command()
async def move(ctx, member: discord.Member, channel, times : int):
    #delete command message
    await ctx.message.delete()
    print(ctx)
    #if channel is id instead of name
    if channel.isdigit():
        channel = discord.utils.get(ctx.guild.channels, id=int(channel))
    else:
        # get channel id from channel name from current server
        channel = discord.utils.get(ctx.guild.channels, name=channel)
    #get id from current voice channel
    currentChan = discord.utils.get(ctx.guild.channels, id=member.voice.channel.id)
    for _ in range(times):
        await member.move_to(channel)
        #await asyncio.sleep(0.5)
        await member.move_to(currentChan)

bot.run(TOKEN)


