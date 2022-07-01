from concurrent.futures.thread import _shutdown
from errno import EEXIST
from logging import shutdown
from pyexpat.errors import messages
from re import A, X 
from typing import Awaitable
from unittest import async_case
#from func31 import *
import discord
from discord.ext import commands
import os
from time import sleep
import random
import asyncio
import json
import aiohttp
import giphy_client
from giphy_client.rest import ApiException
from googletrans import Translator




#                                                             DEĞİŞKENLER
intents = discord.Intents(messages=True, guilds=True, reactions=True, members=True, presences=True)
Bot = commands.Bot(command_prefix='#', intents=intents)
Bot.remove_command("help")
roles = []
messages = []
urwelcome = ["sağol","Sağol","SAĞOL","SAGOL","Teşekkürler","TEŞK","teşk","teşekkürler","tesekkürler","tesk","Tesekkürler","Tesekkurler","tesekkurler","eyw","Eyvallah","eyvallah","eyv"]
selam = ["sa","Sa","SA","sA","selamın aleyküm","Selamın Aleyküm","Selamın aleyküm","selamın Aleyküm","SELAMIN ALEYKÜM"]
pgifs = ["https://c.tenor.com/szPtb6lqakIAAAAS/beating-up-beating-up-lilo.gif","https://c.tenor.com/FFYqOVVbrJAAAAAC/markiplier-punch.gif","https://c.tenor.com/qKTBsktfhSgAAAAS/punch-blue-hoodie.gif","https://c.tenor.com/-dK24mwTyKwAAAAS/tv-shows-supernatural.gif","https://c.tenor.com/ZwjudWL5JxYAAAAC/kirby-punch.gif"]
#-------------------------------------------------------------------------------------------------------------------#
#                                                       BOT AÇILIŞI ONAYI VE DURUM
@Bot.event
async def on_ready():
    await Bot.change_presence(activity=discord.Game(name='#help//Abdullahogus'))
    print("||=--+------------+--/Discord botu baslatilmistir.Iyi kullanimlar :)\--+------------+--=||")

@Bot.event
async def on_message(message):
    user = message.author
    if message.author.id == Bot.user.id:
        return
    if message.content in selam:
        await message.channel.send(f"{user.mention} As Kardeşim Hg :wink:")
    if message.content in urwelcome:
        await message.channel.send(f"{user.mention} bir şey değil Her zaman kullanıma hazırım.")
    await Bot.process_commands(message)
    
@Bot.event
async def on_command_error(ctx, error):
	if isinstance(error, commands.CommandOnCooldown):
		await ctx.send(f"sakin ol tekrar komut kullanman için {round(error.retry_after, 2)} saniyen var.")


async def ch_pr():
    await Bot.wait_until_ready()

    statuses = ["//Abdullahogus", "Selam ben Apot", "#help//Abdullahogus","#help","Cemi Götten Sikiyor"]

    while not Bot.is_closed():
        status = random.choice(statuses)

        await Bot.change_presence(activity=discord.Game(name=status))

        await asyncio.sleep(10)

Bot.loop.create_task(ch_pr())


#-------------------------------------------------------------------------------------------------------------------#
#                                                             ROL ALMA [1]
@Bot.event
async def on_reaction_add(reaction, user):
    if user.bot:
        return
    if reaction.message in messages:
        for rs in roles:
            if rs[1] == str(reaction):
                await user.add_roles(rs[0])
#-------------------------------------------------------------------------------------------------------------------#
#                                                               MUTE


@Bot.command(case_insenstive=True)
@commands.has_role("amdin")
@commands.cooldown(1, 5, commands.BucketType.user)
async def mute(ctx, member: discord.Member, *, reason=None):
    if reason == None:
        await ctx.send("Lütfen bir sebep yazın!")
        return
    guild = ctx.guild
    muteRole = discord.utils.get(guild.roles, name = "Muted")
    testrole1 = discord.utils.get(guild.roles, name = "SLOT")
    

    await member.add_roles(muteRole, reason=reason)
    await ctx.send(f"{member.mention} susturuldu sebebi: {reason}")
    await member.remove_roles(testrole1)
#-------------------------------------------------------------------------------------------------------------------#    
#                                                             UNMUTE
@Bot.command(case_insensitive=True)
@commands.has_role("amdin")
@commands.cooldown(1, 5, commands.BucketType.user)
async def unmute(ctx, member: discord.Member, *, reason=None):
    guild = ctx.guild
    muteRole = discord.utils.get(guild.roles, name = "Muted")
    testrole1 = discord.utils.get(guild.roles, name = "SLOT")
    

    if not muteRole:
        await ctx.send("Rol bulunamadı lütfen rolü kontrol ediniz")
        return

    await member.remove_roles(muteRole, reason=reason)
    await ctx.send(f"{member.mention} Susturması kaldırıldı")
    await member.add_roles(testrole1)

#-------------------------------------------------------------------------------------------------------------------#
#                                                         ÜYE GİRİŞ İNFOSU
@Bot.event
async def on_member_join(member):
    channel = discord.utils.get(member.guild.text_channels, name="🚪・hoşgeldin•baybay")
    await channel.send(f"{member.mention} Aramıza katıldı. Hoş geldin")
#-------------------------------------------------------------------------------------------------------------------#    
#                                                         ÜYE ÇIKIŞ İNFOSU
@Bot.event
async def on_member_remove(member):
    channel = discord.utils.get(member.guild.text_channels, name="🚪・hoşgeldin•baybay")
    await channel.send(f"{member.mention} Aramızdan ayrıldı :(")
#-------------------------------------------------------------------------------------------------------------------#    
#                                                         BOT KOMUTLARI
@Bot.command()
@commands.cooldown(1, 5, commands.BucketType.user)
async def sSupreme(ctx, *args):
    await ctx.send("En iyi Yasuo <@775305718143778836>")

@Bot.command()
@commands.cooldown(1, 5, commands.BucketType.user)
async def lua(ctx, *args):
    await ctx.send("En Lua <@589193582473117699>")
@Bot.command()
@commands.cooldown(1, 5, commands.BucketType.user)
async def hileci(ctx, *args):
    await ctx.send("Hileci Orospu Çocugu <@905532694627246150>")
@Bot.command()
@commands.cooldown(1, 5, commands.BucketType.user)
async def feeder(ctx, *args):
    await ctx.send("2-22 Singed Feeder <@533275339728617473> :flushed:")
@Bot.command()
@commands.cooldown(1, 5, commands.BucketType.user)
async def floppa(ctx, *args):
    await ctx.send("Floppa şey değilmi <@533278005368324102>")
@Bot.command()
@commands.cooldown(1, 5, commands.BucketType.user)
async def hentai(ctx, *args):
    await ctx.send("Yürüyen cinsellik <@918845035729027103>")
@Bot.command()
@commands.cooldown(1, 5, commands.BucketType.user)
async def developer(ctx, *args):
    await ctx.send("En developer <@934177779061239859>")
#---------------------------------------------------------------------------------------------------------------------#
#                                                            PUNCH
@Bot.command()
@commands.cooldown(1, 5, commands.BucketType.user)
async def punch(ctx,member: discord.Member = None,*args):
    if member == None:
        await ctx.send("Bir etiket gir kendini yumruklayamassın.")
        return
    user = ctx.message.author
    pemb = discord.Embed(
        colour=(discord.Colour.random()),
        description =f"{user.name} Kişisi {member.name} Kişisine yumruk attı"
        )
    pemb.set_image(url=(random.choice(pgifs)))

    await ctx.send(embed = pemb)
#--------------------------------------------------------------------------------------------------------------------#
#                                                            RENAME
@Bot.command(pass_context=True)
@commands.cooldown(1, 5, commands.BucketType.user)
@commands.has_role("amdin")
async def rename(ctx, member: discord.Member, nick):
    await member.edit(nick=nick)
    await ctx.send(f'Takma adı şunun ile değiştirildi {member.mention} ')

#-------------------------------------------------------------------------------------------------------------------#
#                                                            CLEAR
@Bot.command()
@commands.cooldown(1, 5, commands.BucketType.user)
async def clear(ctx, amount=5):
    await ctx.channel.purge(limit=amount)
#-------------------------------------------------------------------------------------------------------------------#    
#                                                            KİCK
@Bot.command()
@commands.cooldown(1, 5, commands.BucketType.user)
@commands.has_role("amdin")
async def kick(ctx, member:discord.Member, *args, reason="yok"):
    await member.kick(reason=reason)
#-------------------------------------------------------------------------------------------------------------------#    
#                                                            BAN
@Bot.command()
@commands.cooldown(1, 5, commands.BucketType.user)
@commands.has_role("amdin")
async def ban(ctx, member:discord.Member, *args, reason="yok"):
    await member.ban(reason=reason)
#-------------------------------------------------------------------------------------------------------------------#    
#                                                           UNBAN
@Bot.command()
@commands.cooldown(1, 5, commands.BucketType.user)
@commands.has_role("amdin")
async def unban(ctx, *, member):
    banned_users = await ctx.guild.bans()
    member_name, member_discriminator = member.split('#')

    for bans in banned_users:
        user = bans.user

        if (user.name, user.discriminator) == (member_name, member_discriminator):
            await ctx.guild.unban(user)
            await ctx.send(f'Banı kaldırıldı {user.mention}')
            return
#-------------------------------------------------------------------------------------------------------------------#
#                                                     LOAD UNLOAD 
#@Bot.command()
#@commands.has_role("ADMINTEST")
#async def load(ctx, extension):
 #   Bot.load_extension(f'cogs.{extension}')

#@Bot.command()
#@commands.has_role("ADMINTEST")
#async def unload(ctx, extension):
#    Bot.load_extension(f'cogs.{extension}')

#for filename in os.listdir("./cogs"):
 #   if filename.endswith('.py'):
  #      Bot.load_extension(f'cogs.{filename[:-3]}')
#-------------------------------------------------------------------------------------------------------------------#
#                                                      ROL ALMA [2]
@Bot.command()
async def add_role(ctx, role: discord.Role, emoji: str, message_channel: str):
    channel_id, message_id = message_channel.split("/")[-2:]
    msg = await Bot.get_channel(int(channel_id)).fetch_message(int(message_id))
    await msg.add_reaction(emoji)
    messages.append(msg)

    for saved_roles in roles:
        if (role in saved_roles) or (emoji in saved_roles):
            await ctx.send("Bu rol ve emoji kullanılmış, Lütfen başka rol ve emoji kullanın.")
            return

    add_new_role(role, emoji)

def add_new_role(role, emoji):
    roles.append([role, emoji])
    print(roles)

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

#-------------------------------------------------------------------------------------------------------------#
#                                                         CM
@Bot.command()
@commands.cooldown(1, 5, commands.BucketType.user)
async def cm(ctx,member: discord.Member=None):
    cm_list = ["8=D","8==D","8===D","8======D","8========D","8===============D","8===========================D","8=D","8==D","8===D","8=D","8==D","8===D"]
    if(member == None):
        user = ctx.message.author
        embed = discord.Embed(title="DİCKRATE",description=f"{user.mention} Senin Alet {random.choice(cm_list)}")
        await ctx.send(embed = embed)
    else:
        embed = discord.Embed(title="DİCKRATE",description=f"{member.mention} Senin Alet {random.choice(cm_list)}")
        await ctx.send(embed = embed)

#--------------------------------------------------------------------------------------------------------------#
#                                                          GAY
@Bot.command(case_insenstive=True)
@commands.cooldown(1, 5, commands.BucketType.user)
async def gay(ctx,member: discord.Member=None,*args):
    gayC = random.randint(1,100)
    if(member == None):
        user = ctx.message.author
        await ctx.send(f'{user.mention} %{gayC} Gay')
    if(gayC == 100):
        await ctx.send(f'{member.mention} Hakiki :rainbow_flag: LGBTQ+ üyesi.')
    else:   
        await ctx.send(f'{member.mention} %{gayC} Gay')
#---------------------------------------------------------------------------------------------------------------#
#                                                         UNGAY
@Bot.command()
@commands.cooldown(1, 5, commands.BucketType.user)
async def ungay(ctx,member: discord.Member=None,*args):
    await ctx.send(f"{member.mention} Gay olmadığını #ungay kullanarak kanıtladı. Artık Straight.")
#---------------------------------------------------------------------------------------------------------------#
#                                                        SHUTDOWN
@Bot.command()
@commands.cooldown(1, 5, commands.BucketType.user)
#@commands.has_role("amdin")
async def shutdown(message):
    id = message.author.id
    if id == 775305718143778836: 
       print("Bot kapatıldı Görüşmek üzere patron")
       await message.send("Bot kapatıldı görüşmek üzere patron...")
       await Bot.logout()
    elif id == 918845035729027103:
        print("Bot kapatıldı görüşmek üzere patron")
        await Bot.logout()
        
    else:
        await message.send("Botu patron dışında kimse kapatamaz")
        return
#---------------------------------------------------------------------------------------------------------------#
#                                                      CUSTOM HELP
@Bot.group(invoke_without_command=True)
@commands.cooldown(1, 5, commands.BucketType.user)
async def help(ctx):
    em = discord.Embed(title = "Help", description = "Komutların başına # koyarak aşşağıdaki komutları kullanabilirsin.")

    em.add_field(name ="Moderasyon", value= "//kick • ban • unban • mute • unmute • clear • rename// ")
    em.add_field(name ="Eğlence", value="//cm • gay • ungay • pp • punch • gif • cevir//")

    await ctx.send(embed = em)
#---------------------------------------------------------------------------------------------------------------#
#                                                         AVATAR
@Bot.command()
@commands.cooldown(1, 5, commands.BucketType.user)
async def pp(ctx, member: discord.Member = None):
    if member == None:
        member = ctx.author
    
    memberAvtar = member.avatar_url
    avaEmbed = discord.Embed(title = f"{member.name} // Profil Fotoğrafı" )
    avaEmbed.set_image(url = memberAvtar)
    await ctx.send(embed = avaEmbed)
#---------------------------------------------------------------------------------------------------------------#
#                                                           GİF
@Bot.command()
@commands.cooldown(1, 5, commands.BucketType.user)
async def gif(ctx, *,q="Smile"):

    api_key = "qtC2GU1CezSTlPOrOMBdby6IFjB5IEIy"
    api_instance = giphy_client.DefaultApi()

    try:

        api_responce = api_instance.gifs_search_get(api_key, q, limit=10, rating="g",lang = "tr")
        lst = list(api_responce.data)
        giff = random.choice(lst)

        await ctx.channel.send(giff.embed_url)

    except ApiException as e:
        print("Exception when calling Api")
#--------------------------------------------------------------------------------------------------------------#
#                                                          ÇEVİRİ
@Bot.command()
async def cevir(ctx, lang, *, thing):
    translator = Translator()
    translation = translator.translate(thing, dest=lang)
    await ctx.send(translation.text)
#--------------------------------------------------------------------------------------------------------------#
#                                                          SNİPE
snipe_message_author = {}
snipe_message_content = {}

@Bot.event
async def on_message_delete(message):
     snipe_message_author[message.channel.id] = message.author
     snipe_message_content[message.channel.id] = message.content
     await sleep(3)
     del snipe_message_author[message.channel.id]
     del snipe_message_content[message.channel.id]

@Bot.command(name = 'snipe')
@commands.cooldown(1, 5, commands.BucketType.user)
async def snipe(ctx):
    channel = ctx.channel
    try:
        em = discord.Embed(name = f"Son silinen mesaj #{channel.name}", description = snipe_message_content[channel.id])
        em.set_footer(text = f"Bu mesaj şu kişi tarafından gönderildi {snipe_message_author[channel.id]}")
        await ctx.send(embed = em)
    except KeyError: 
        await ctx.send(f"Burada hiç silinen mesaj yok #{channel.name}")
#------------------------------------------------------------------------------------------------------------#
#                                                      ROL EKLE AL
@Bot.command()
@commands.cooldown(1, 5, commands.BucketType.user)
@commands.has_role("amdin")
async def ar(ctx, role: discord.Role, user: discord.Member):
    await user.add_roles(role)
    await ctx.send(f"{role.mention} Rolü {user.mention} Kişisine verildi.")

@Bot.command()
@commands.cooldown(1, 5, commands.BucketType.user)
@commands.has_role("amdin")
async def rr(ctx, role: discord.Role, user: discord.Member):
    await user.remove_roles(role)
    await ctx.send(f"{role.mention} Rolü {user.mention} Kişisinden alındı.")

#------------------------------------------------------------------------------------------------------------#





Bot.run('OTgwNTI1Mzc0NzE2OTM2Mjgy.Gupqv-.8MFeO6H7-QomMuGJwim5tUDTzW8udkgB363Kl4')
