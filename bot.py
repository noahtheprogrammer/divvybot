import os
from datetime import datetime
from dotenv import load_dotenv

import discord
from discord.ext import commands

from commands import token_balance, sol_balance

load_dotenv()
token = os.getenv('DISCORD_TOKEN')

intents = discord.Intents()
intents.messages = True
intents.message_content = True

bot = commands.Bot("!", intents=intents)

@bot.command()
async def update(ctx):
    embed = discord.Embed(title="Divvy Accrual",
                          url="https://solscan.io/account/3D3whwTbRYzr2b6yY8hXE6EVGRJVGYyGC7jFrTxHVhbK",
                          description="The current balance of Divvy's accrual wallet can be viewed below. This information is pulled directly from Solscan.",
                          timestamp=datetime.now())
    embed.add_field(name="SOL", value=sol_balance(), inline=True)
    embed.add_field(name="USDC", value=f"${token_balance('EPjFWdd5AufqSSqeM2qN1xzybapC8G4wEGGkZwyTDt1v')}", inline=True)
    embed.add_field(name="Tether", value=f"${token_balance('Es9vMFrzaCERmJfrF4H2FYD4KCoNkY11McCe8BenwNYB')}", inline=True)
    embed.set_footer(text="Powered by bigweavers")
    await ctx.send(embed=embed)

@bot.command()
async def support(ctx):
    embed = discord.Embed(title="Divvybot Support",
                          description="Currently supported commands and their actions can be viewed below.",
                          timestamp=datetime.now())
    embed.add_field(name="!update", value="Displays the $SOL, $USDC, and $USDT balance of the accrual wallet.", inline=False)
    embed.add_field(name="!support", value="Displays more information on the available commands.", inline=False)
    embed.set_footer(text="Powered by bigweavers")
    await ctx.send(embed=embed)

bot.run(token)