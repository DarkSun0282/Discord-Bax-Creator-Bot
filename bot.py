import discord
import random
from discord.ext import commands
from asyncio import *
from discord.ext.commands import Bot
from discord import Member
from discord.ext.commands import has_permissions, MissingPermissions

# PREFIX
# پیشوند
prefix = "!" 
client = commands.Bot(command_prefix = prefix)

TOKEN = "ADD YOUR TOKEN HERE"
randcolor = random.randint(0x000000, 0xFFFFFF)

@client.event
async def on_ready():
    print(f'{client.user} Has Been Runned')    


# CREATE BAX
# ساخت بکس

@client.command()
# PERMISSION | NEED TO MANAGE ROLES & MANAGE CHANNELS TO CREATE BAX OTHERWISE USER GETS AN ERROR
# پرمیشن ها | نیازمند پرمیشن منیج رول و منیج چنل میباشد در غیر این صورت یوزر ارور دریافت میکند
@has_permissions(manage_channels=True, manage_roles=True)
async def bax(ctx, *, arg):
    # CONSOLE MESSAGE
    # پیام کنسول
    print("{} Has Used !bax Command".format(ctx.author))
    
    # CREATE LEVEL EMBED MESSAGE
    # پیام لول های ساخت
    startembed=discord.Embed(description="Setting Up __**{}**__ Bax 🔃".format(arg), color=randcolor)
    roleembed=discord.Embed(description="Create __**{}**__ Role 🔃".format(arg), color=randcolor)
    catembed=discord.Embed(description="Create __**{}**__ Category 🔃".format(arg), color=randcolor)
    chatembed=discord.Embed(description="Create __**{}**__ Text Channel 🔃".format(arg), color=randcolor)
    vcembed=discord.Embed(description="Crate __**{}**__ Voice Channels 🔃".format(arg), color=randcolor)
    confembed=discord.Embed(description="Configure __**{}**__ Channels Permission 🔃".format(arg), color=randcolor)
    endembed=discord.Embed(description="__**{}**__ Bax Has Been Created Successfully ✅".format(arg), color=randcolor)
        
    startembed.set_footer(text="Requested By {}".format(ctx.author.name), icon_url="{}".format(ctx.author.avatar_url))
    roleembed.set_footer(text="Requested By {}".format(ctx.author.name), icon_url="{}".format(ctx.author.avatar_url))
    catembed.set_footer(text="Requested By {}".format(ctx.author.name), icon_url="{}".format(ctx.author.avatar_url))
    chatembed.set_footer(text="Requested By {}".format(ctx.author.name), icon_url="{}".format(ctx.author.avatar_url))
    vcembed.set_footer(text="Requested By {}".format(ctx.author.name), icon_url="{}".format(ctx.author.avatar_url))
    confembed.set_footer(text="Requested By {}".format(ctx.author.name), icon_url="{}".format(ctx.author.avatar_url))
    endembed.set_footer(text="Requested By {}".format(ctx.author.name), icon_url="{}".format(ctx.author.avatar_url))
    
    startembed.set_thumbnail(url="{}".format(ctx.guild.icon_url))
    roleembed.set_thumbnail(url="{}".format(ctx.guild.icon_url))
    catembed.set_thumbnail(url="{}".format(ctx.guild.icon_url))
    chatembed.set_thumbnail(url="{}".format(ctx.guild.icon_url))
    vcembed.set_thumbnail(url="{}".format(ctx.guild.icon_url))
    confembed.set_thumbnail(url="{}".format(ctx.guild.icon_url))
    endembed.set_thumbnail(url="{}".format(ctx.guild.icon_url))
    
    guild = ctx.message.guild
    baxmsg = await ctx.reply(embed=startembed)
    
    # CREATE ROLE
    # ساخت رول
    await baxmsg.edit(embed=roleembed)
    baxrole = await guild.create_role(name = "🪓〢{}™️".format(arg), reason="Requested By {}".format(ctx.author))
    lbaxrole = await guild.create_role(name = "🪓〢{}ˡᵉᵃᵈᵉʳ".format(arg), reason="Requested By {}".format(ctx.author))
    
    # CREATE CATEGORY
    # ساخت کتگوری
    await baxmsg.edit(embed=catembed)
    category = await guild.create_category("✎𓐘𓐘𓐘{}𓐘𓐘𓐘".format(arg), reason="Requsted By {}".format(ctx.author))
    
    # CREATE TEXT_CHANNELS
    # ساخت چنل تکست
    await baxmsg.edit(embed=chatembed)
    baxchat = await guild.create_text_channel("•⊰⟅💬⟆{} 𝐶ℎ𝑎𝑡".format(arg), category=category, reason="Requsted By {}".format(ctx.author), sync_permissions=True)
    baxmusic = await guild.create_text_channel("•⊰⟅🗨⟆{} 𝑀𝑢𝑠𝑖𝑐".format(arg), category=category, reason="Requsted By {}".format(ctx.author), sync_permissions=True)
    
    # CREATE VOICE_CHANNELS
    # ساخت چنل ویس
    await baxmsg.edit(embed=vcembed)
    baxpubvc = await guild.create_voice_channel("•➺🔊⎱{} 𝐏𝐮𝐛𝐥𝐢𝐜".format(arg), category=category, reason="Requsted By {}".format(ctx.author), sync_permissions=True)
    baxvc1 = await guild.create_voice_channel("•➺🔊⎱{} 𝐕𝐨𝐢𝐜𝐞¹".format(arg), category=category, reason="Requsted By {}".format(ctx.author), sync_permissions=True)
    baxvc2 = await guild.create_voice_channel("•➺🔊⎱{} 𝐕𝐨𝐢𝐜𝐞²".format(arg), category=category, reason="Requsted By {}".format(ctx.author), sync_permissions=True)
    
    # CONFIG CHANNELS PERMISSIONS
    # کانفیگ و پرمیشن چنل ها
    await baxmsg.edit(embed=confembed)
    await category.set_permissions(baxrole, read_messages=True, send_messages=True, connect=True, speak=True)
    await category.set_permissions(lbaxrole, read_messages=True, send_messages=True, manage_messages=True, connect=True, speak=True, mute_members=True, deafen_members=True, move_members=True)
    await category.set_permissions(ctx.guild.default_role, connect=False, mute_members=False, deafen_members=False, move_members=False)
    await baxchat.set_permissions(ctx.guild.default_role, read_messages=False)
    await baxmusic.set_permissions(ctx.guild.default_role, read_messages=False)
    await baxpubvc.set_permissions(ctx.guild.default_role, connect=True)
    
    # END MESSAGE
    # پیام آخر 
    endembed.add_field(name=":part_alternation_mark: Roles", value="Leader Role <@&{}>\nBax Role <@&{}>".format(lbaxrole.id, baxrole.id), inline=False)
    endembed.add_field(name=":speech_left: Text Channels", value="Bax Chat <#{}>\nMusic Channel <#{}>".format(baxchat.id, baxmusic.id), inline=False)
    endembed.add_field(name=":loud_sound: Voice Channels", value="Public Voice <#{}>\nBax Voice 1 <#{}>\nBax Voice 2 <#{}>".format(baxpubvc.id, baxvc1.id, baxvc2.id))
    await baxmsg.edit(embed=endembed)



# ERROR
# ارور
@bax.error
async def bax_error(ctx, error):
    errembed=discord.Embed(description="Sorry **{}**, You Don't Have Permission To Create Bax ❌".format(ctx.author))
    errembed.set_thumbnail(url="{}".format(ctx.guild.icon_url))
    errembed.set_footer(text="Requested By {}".format(ctx.author.name), icon_url="{}".format(ctx.author.avatar_url))
    if isinstance(error, MissingPermissions):
        await ctx.reply(embed=errembed)

#####
client.run(TOKEN)
