import os
import requests
from datetime import datetime
from dotenv import load_dotenv

import discord
from discord.ext import commands

from connection import *

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
    embed.add_field(name="SOL", value=sol_balance(accrual), inline=True)
    embed.add_field(name="USDC", value=f"${token_balance(accrual, usdc[1]):,}", inline=True)
    embed.add_field(name="Tether", value=f"${token_balance(accrual, usdt[1]):,}", inline=True)
    embed.set_footer(text="Powered by bigweavers")
    await ctx.send(embed=embed)

@bot.command()
async def support(ctx):
    embed = discord.Embed(title="Divvybot Support",
                          description="Currently supported commands and their actions can be viewed below.",
                          timestamp=datetime.now())
    embed.add_field(name="!update", value="Displays the $SOL, $USDC, and $USDT balance of the accrual wallet.", inline=False)
    embed.add_field(name="!house", value="Displays the $SOL, $USDC, and $USDT balance of the house pool.", inline=False)
    embed.add_field(name="!market", value="Displays the floor price, average sale, and total volume of the Divvy collection.", inline=False)
    embed.add_field(name="!staking `address`", value="Displays staking information and estimated revenue for the given wallet address.", inline=False)
    embed.add_field(name="!donate", value="Displays the donation address of the creator.", inline=False)
    embed.set_footer(text="Powered by bigweavers")
    await ctx.send(embed=embed)

@bot.command()
async def donate(ctx):
    embed = discord.Embed(title="Donations",
                          description="Below is the donation address for the creator of Divvybot. Buy him a coffee please!",
                          timestamp=datetime.now())
    embed.add_field(name="Wallet Address", value="9P8zVyaaA1rgqWjZ7hCG5w1BxL94Q248ozqyy88HQpCn", inline=False)
    embed.set_footer(text="Powered by bigweavers")
    await ctx.send(embed=embed)

@bot.command()
async def house(ctx):
    embed = discord.Embed(title="Divvy House",
                        url="https://app.divvy.bet/housepool/",
                        description="The current balances of Divvy's House Pool can be viewed below. This information is pulled directly from Solscan.",
                        timestamp=datetime.now())
    embed.add_field(name="SOL", value=sol_balance(sol[0]), inline=True)
    embed.add_field(name="USDC", value=f"${token_balance(usdc[0], usdc[1]):,}", inline=True)
    embed.add_field(name="Tether", value=f"${token_balance(usdt[0], usdt[1]):,}", inline=True)
    embed.set_footer(text="Powered by bigweavers")
    await ctx.send(embed=embed)

@bot.command()
async def staking(ctx, args):
    counters = find_pass_count(args)
    revenue = token_balance(accrual, usdc[1])
    revenue = revenue + token_balance(accrual, usdt[1])
    embed = discord.Embed(title="Divvy Staking",
                          url="https://app.divvy.bet/staking/",
                          description="Divvy staking information and estimated wallet revenue can be viewed below. This information is pulled directly from Solscan.",
                          timestamp=datetime.now())
    embed.add_field(name="Owned Passes", value=counters[0], inline=True)
    embed.add_field(name="Staked Passes", value=counters[1], inline=True)
    embed.add_field(name="Estimated Revenue", value=f"${revenue/2500 * counters[1]}", inline=False)
    embed.set_footer(text="Powered by bigweavers")
    await ctx.send(embed=embed)

@bot.command()
async def market(ctx):
    data = requests.get("https://api-mainnet.magiceden.dev/v2/collections/dvypass/stats")
    collection = data.json()
    embed = discord.Embed(title="Divvy Market",
                    url="https://magiceden.io/marketplace/dvypass",
                    description="Divvy's current market statistics can be viewed below. This information is pulled directly from Magic Eden.",
                    timestamp=datetime.now())
    embed.add_field(name="Floor Price", value=f"{collection['floorPrice']/(10**9)} SOL", inline=True)
    embed.add_field(name="Average Sale", value=f"{round(collection['avgPrice24hr']/(10**9), 2)} SOL", inline=True)
    embed.add_field(name="Total Volume", value=f"{round(collection['volumeAll']/(10**9), 2)} SOL", inline=True)
    embed.set_footer(text="Powered by bigweavers")
    await ctx.send(embed=embed)

bot.run(token)