import discord

from discord.ext import commands

class Basics(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.guild_only()
    @commands.command()
    async def membercount(self, ctx):
        await ctx.send(f"{ctx.guild.name} has {ctx.guide.member_count} users!")
    
    @commmands.command()
    async def about(self, ctx):
        message = "Asteroid is a bot programmed by <@!141532589725974528> and can be found at https://github.com/AtlasNX/Asteroid \n"
        embed = discord.Embed(title="Informations about the bot!", url="https://github.com/AtlasNX/Asteroid", description=message)

        await ctx.send(embed=embed)