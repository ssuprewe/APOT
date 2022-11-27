from errno import EEXIST
from pyexpat.errors import messages
from typing import Awaitable
from unittest import async_case
#from func31 import *
import discord
from discord.ext import commands
from discord.ext.commands import has_permissions
import os
from time import sleep
import random
import asyncio
import json
import aiohttp
import giphy_client
from giphy_client.rest import ApiException
from googletrans import Translator




#                                                                Variables
intents = discord.Intents(messages=True, guilds=True, reactions=True, members=True, presences=True)
Bot = commands.Bot(command_prefix='#', intents=intents) #you can change the prefix 
Bot.remove_command("help")
roles = []
messages = []
pgifs = ["https://c.tenor.com/szPtb6lqakIAAAAS/beating-up-beating-up-lilo.gif","https://c.tenor.com/FFYqOVVbrJAAAAAC/markiplier-punch.gif","https://c.tenor.com/qKTBsktfhSgAAAAS/punch-blue-hoodie.gif","https://c.tenor.com/-dK24mwTyKwAAAAS/tv-shows-supernatural.gif","https://c.tenor.com/ZwjudWL5JxYAAAAC/kirby-punch.gif"]
#-------------------------------------------------------------------------------------------------------------------#
#                                                                Startup
@Bot.event
async def on_ready():
    await Bot.change_presence(activity=discord.Game(name='#help'))
    print("||=--+------------+--/Bot is ready!\--+------------+--=||")
    
@Bot.event
async def on_command_error(ctx, error):
	if isinstance(error, commands.CommandOnCooldown):
		await ctx.send(f"calm down dude try again{round(error.retry_after, 2)} seconds.")


async def ch_pr():
    await Bot.wait_until_ready()

    statuses = ["#help"] #you can change statuses

    while not Bot.is_closed():
        status = random.choice(statuses)

        await Bot.change_presence(activity=discord.Game(name=status))

        await asyncio.sleep(10)

Bot.loop.create_task(ch_pr())


#-------------------------------------------------------------------------------------------------------------------#
#                                                               MUTE


@Bot.command(case_insenstive=True)
@has_permissions(administrator=True)
@commands.cooldown(1, 5, commands.BucketType.user)
async def mute(ctx, member: discord.Member, *, reason=None):
    if reason == None:
        await ctx.send("please write a reason!")
        return
    guild = ctx.guild
    muteRole = discord.utils.get(guild.roles, name = "Muted") #write mute role name
    

    await member.add_roles(muteRole, reason=reason)
    await ctx.send(f"{member.mention} muted. reason: {reason}")
    await member.remove_roles(testrole1)
#-------------------------------------------------------------------------------------------------------------------#    
#                                                             UNMUTE
@Bot.command(case_insensitive=True)
@has_permissions(administrator=True)
@commands.cooldown(1, 5, commands.BucketType.user)
async def unmute(ctx, member: discord.Member, *, reason=None):
    guild = ctx.guild
    muteRole = discord.utils.get(guild.roles, name = "Muted") #write mute role name
    

    if not muteRole:
        await ctx.send("role not found")
        return

    await member.remove_roles(muteRole, reason=reason)
    await ctx.send(f"{member.mention} unmuted")
    await member.add_roles(testrole1)

#-------------------------------------------------------------------------------------------------------------------#
#                                                         MEMBER JOIN
@Bot.event
async def on_member_join(member):
    channel = discord.utils.get(member.guild.text_channels, name="") #our enter exit channelname
    await channel.send(f"{member.mention} welcome") #ur welcome message
#-------------------------------------------------------------------------------------------------------------------#    
#                                                         MEMBER REMOVE
@Bot.event
async def on_member_remove(member):
    channel = discord.utils.get(member.guild.text_channels, name="")#our enter exit channelname
    await channel.send(f"{member.mention} ")#ur message
#-------------------------------------------------------------------------------------------------------------------#    
#                                                         BOT KOMUTLARI

#---------------------------------------------------------------------------------------------------------------------#
#                                                            PUNCH
@Bot.command()
@commands.cooldown(1, 5, commands.BucketType.user)
async def punch(ctx,member: discord.Member = None,*args):
    if member == None:
        await ctx.send("write a person. cant punch yourself.")
        return
    user = ctx.message.author
    pemb = discord.Embed(
        colour=(discord.Colour.random()),
        description =f"{user.name} {member.name} " #our message
        )
    pemb.set_image(url=(random.choice(pgifs)))

    await ctx.send(embed = pemb)
#--------------------------------------------------------------------------------------------------------------------#
#                                                            RENAME
@Bot.command(pass_context=True)
@commands.cooldown(1, 5, commands.BucketType.user)
@has_permissions(administrator=True)
async def rename(ctx, member: discord.Member, nick):
    await member.edit(nick=nick)
    await ctx.send(f'nickname changed {member.mention} ')

#-------------------------------------------------------------------------------------------------------------------#
#                                                            CLEAR
@Bot.command()
@commands.cooldown(1, 5, commands.BucketType.user)
async def clear(ctx, amount=5):
    await ctx.channel.purge(limit=amount)
#-------------------------------------------------------------------------------------------------------------------#    
#                                                            KİCK
@Bot.command()
@has_permissions(kick_members = True)
@commands.cooldown(1, 5, commands.BucketType.user)
async def kick(ctx, member:discord.Member, *args, reason="yok"):
    await member.kick(reason=reason)
#-------------------------------------------------------------------------------------------------------------------#    
#                                                            BAN
@Bot.command()
@has_permissions(ban_members = True)
@commands.cooldown(1, 5, commands.BucketType.user)
async def ban(ctx, member:discord.Member, *args, reason="yok"):
    await member.ban(reason=reason)

@Bot.command()
async def banned(ctx, member:discord.Member, *args, reason="yok"):
    id = message.author.id
    if id == 775305718143778836:
        await member.ban(reason=reason)
    else:
        ctx.send("olmas")
	

#-------------------------------------------------------------------------------------------------------------------#    
#                                                           UNBAN
@Bot.command()
@has_permissions(ban_members = True)
@commands.cooldown(1, 5, commands.BucketType.user)
async def unban(ctx, *, member):
    banned_users = await ctx.guild.bans()
    member_name, member_discriminator = member.split('#')

    for bans in banned_users:
        user = bans.user

        if (user.name, user.discriminator) == (member_name, member_discriminator):
            await ctx.guild.unban(user)
            await ctx.send(f'Unbanned {user.mention}')
            return
#-------------------------------------------------------------------------------------------------------------#
#                                                         PİNG
@Bot.command()
@commands.cooldown(1, 5, commands.BucketType.user)
async def ping(ctx):
    ms1=f'Pong! {round(Bot.latency * 1000)}ms'
    pig = discord.Embed(
        colour=(discord.Colour.random()),
        title="Discord ping",
        description=ms1
    )
    await ctx.send(embed=pig)

#---------------------------------------------------------------------------------------------------------------#
#                                                        SHUTDOWN
@Bot.command()
@commands.cooldown(1, 5, commands.BucketType.user)
async def shutdown(message):
    id = message.author.id
    if id == : #ur discord id
       print("bot closed")
       await message.send("") #your message
       await Bot.logout()
    else:
        await message.send("")
        return
#---------------------------------------------------------------------------------------------------------------#
#                                                      CUSTOM HELP
@Bot.group(invoke_without_command=True)
@commands.cooldown(1, 5, commands.BucketType.user)
async def help(ctx):
    em = discord.Embed(title = "Help", description = "")

    em.add_field(name ="Moderation", value= "//kick • ban • unban • mute • unmute • clear • rename// ")
    em.add_field(name ="Fun", value="//pp • punch • gif • translate//")

    await ctx.send(embed = em)
#---------------------------------------------------------------------------------------------------------------#
#                                                         AVATAR
@Bot.command()
@commands.cooldown(1, 5, commands.BucketType.user)
async def pp(ctx, member: discord.Member = None):
    if member == None:
        member = ctx.author
    
    memberAvtar = member.avatar_url
    avaEmbed = discord.Embed(title = f"{member.name} // Profile Picture" )
    avaEmbed.set_image(url = memberAvtar)
    await ctx.send(embed = avaEmbed)
#---------------------------------------------------------------------------------------------------------------#
#                                                           GİF
@Bot.command()
@commands.cooldown(1, 5, commands.BucketType.user)
async def gif(ctx, *,q="Smile"):

    api_key = "" #your giphy api key
    api_instance = giphy_client.DefaultApi()

    try:

        api_responce = api_instance.gifs_search_get(api_key, q, limit=10, rating="g",lang = "tr")
        lst = list(api_responce.data)
        giff = random.choice(lst)

        await ctx.channel.send(giff.embed_url)

    except ApiException as e:
        print("Exception when calling Api")
#--------------------------------------------------------------------------------------------------------------#
#                                                          TRANSLATE
@Bot.command()
async def cevir(ctx, lang, *, thing):
    translator = Translator()
    translation = translator.translate(thing, dest=lang)
    await ctx.send(translation.text)








Bot.run('') #your bot token 
