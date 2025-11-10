import asyncio
import discord
from discord import member
from discord import channel
from discord.ext import commands
import sys
import time

intents = discord.Intents.default()
intents.members = True  # Enable the members intent to access member information
intents.presences = True # Enable the presences intent to access user statuses and activities

mat = 1036069001333321728
ann = 1385756951052423198 # current id is a placeholder for testing - replace with actual channel ID 1365866818962718802
serv = 1365865723829682278

bot = commands.Bot(command_prefix="!", intents=intents)

@bot.event
async def on_ready():
    print(f"Bot is ready. Logged in as {bot.user}")
    member = bot.get_guild(serv).get_member(mat)
    for activity in member.activities:
        if isinstance(activity, discord.CustomActivity):
            custom_status = activity.name
            break
    embed = discord.Embed(
        title=f"{member.display_name}'s Status",
        description=f"**Status:** {custom_status}",
        color=discord.Color.blue()
    )
    channel = bot.get_channel(ann)

    await channel.send(embed=embed)
    await channel.send("Computer is now on - all code is running")

    while True:
        member = bot.get_guild(serv).get_member(mat)
        new_custom_status = None
        
        for activity in member.activities:
            if isinstance(activity, discord.CustomActivity):
                new_custom_status = activity.name
                break
        
        if new_custom_status is None:
            new_custom_status = "No custom status"
            
        if new_custom_status != custom_status:
            custom_status = new_custom_status
            embed = discord.Embed(
                title=f"{member.display_name}'s Status was updated!",
                description=f"**Status:** {custom_status}",
                color=discord.Color.blue()
            )
            await channel.send(embed=embed)
            print(f"Status updated to: {custom_status}")
        else:
            print(f"No status change detected. Current status: {custom_status}")
            
        await asyncio.sleep(60) 


bot.run("Tokeh") # replace with your bottoken
