import discord
import config
import random
import asyncio
import basics

from discord.ext import commands

bot = commands.Bot(command_prefix=config.command_prefix)
bot.remove_command("help") # Heck the normal help command

async def status():
    await bot.wait_until_ready()
    while True:
        await bot.change_presence(activity=discord.Activity(name=f"{random.choice(config.status_q)} | {config.command_prefix}help", type=2), status=discord.Status.dnd)
        await asyncio.sleep(1800)

@bot.event
async def on_command_error(ctx, error):
    print(f"Error: \"{str(error)}\" when someone typed \"{ctx.message.content}\"")

@bot.event
async def on_ready():
    members = 0
    
    for guild in bot.guilds:
        members += guild.member_count
        
    print(f"Started {bot.user.name} on {len(bot.guilds)} servers with {members} members!")

bot.loop.create_task(status())
bot.add_cog(basics.Basics(bot))
bot.run(config.token)