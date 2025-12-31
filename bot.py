import os
import discord
from discord.ext import commands

# Bot token
TOKEN = os.environ.get("DISCORD_TOKEN")  # Render e environment variable hisebe thakbe

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix="!", intents=intents)

@bot.event
async def on_ready():
    print(f'Logged in as {bot.user}')

@bot.command()
async def hello(ctx):
    await ctx.send(f"Hello {ctx.author.mention}!")

bot.run(TOKEN)
