import asyncio
import discord
from discord import member
from discord import channel
from discord.ext import commands
import sys
import time
from datetime import date

intents = discord.Intents.default()
intents.members = True  # Enable the members intent to access member information
intents.presences = True # Enable the presences intent to access user statuses and activities

mat = 1036069001333321728
ann = 1385756951052423198 #current id is a placeholder for testing - replace with actual channel ID 1365866818962718802
serv = 1365865723829682278

bot = commands.Bot(command_prefix="!", intents=intents)


@bot.event
async def on_ready():
    current_date = date.today()
    print(f"Bot is ready. Logged in as {bot.user}")
    member = bot.get_guild(serv).get_member(mat)
    for activity in member.activities:
        if isinstance(activity, discord.CustomActivity):
            custom_status = activity.name
            break
    forum_channel = bot.get_channel(1427062413051691119) # replace this with your forum channel id
    tag_names_to_apply = [" ", ","] # replace with the tag names in your forum channel
    tags_to_apply = []
    for tag_name in tag_names_to_apply:
        for available_tag in forum_channel.available_tags:
            if available_tag.name == tag_name:
                tags_to_apply.append(available_tag)
                break
    await forum_channel.create_thread(
            name=f"{custom_status} - {current_date}",
            content="Rate", # body
            applied_tags=tags_to_apply
        )
    print("c")

    channel = bot.get_channel(ann)


    while True:
        member = bot.get_guild(serv).get_member(mat)
        new_custom_status = None
        
        for activity in member.activities:
            if isinstance(activity, discord.CustomActivity):
                new_custom_status = activity.name
                break
        
        if new_custom_status is None:
            new_custom_status = custom_status # This is because it will recognize no status when offline
            
        if new_custom_status != custom_status:
            custom_status = new_custom_status
            tag_names_to_apply = [" ", ","] # same as beofre
            tags_to_apply = []
            for tag_name in tag_names_to_apply:
                for available_tag in forum_channel.available_tags:
                    if available_tag.name == tag_name:
                        tags_to_apply.append(available_tag)
                        break
                await forum_channel.create_thread(
                        name=f"{custom_status} - {current_date}",
                        content="Rate", # body
                        applied_tags=tags_to_apply
                        )
            print(f"Status updated to: {custom_status}")
        else:
            print(f"No status change detected. Current status: {custom_status}")
            
        await asyncio.sleep(60) 
   





bot.run("Token")
