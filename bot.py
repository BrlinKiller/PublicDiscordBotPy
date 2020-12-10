import discord
from discord.ext import commands
import random

TOKEN = '****I CAN NOT SHOW THIS ****'

Client = commands.Bot(command_prefix="B+", intents = discord.Intents.all())

@Client.event
async def on_ready():
    await Client.change_presence(activity=discord.Activity(type=discord.ActivityType.listening, name="B+help"))
    print("Bot is ready")

Client.remove_command("help")

@Client.command()
async def help(ctx):
    emh = discord.Embed(title="brlinbot2", description = "**B+** *<command>*",color = discord.Color.dark_blue())
    emh.set_thumbnail(url='https://cdn.discordapp.com/attachments/702124631414276228/783080761641009182/chup4.png')
    emh.add_field(name="**moderation**",value="```remove``` ```send``` ```notsend``` ```removerole``` ```addrole```")
    emh.add_field(name="**other**",value="```count``` ```ping``` ```gulu``` ```infos``` ```rules```")
    emh.add_field(name="**fun**",value="```say``` ```rat``` ```Star```")
    await ctx.author.send(embed=emh)
    await ctx.send("command list sent to DMs.")

@Client.event
async def on_message(msgr):
    if msgr.channel == msgr.guild.get_channel(783118420492943360):
        if not msgr.content=='Rat.':
            await msgr.delete()
                     
    await Client.process_commands(msgr)


@Client.event
async def on_member_join(meberjoin):
    embjoin = discord.Embed(title =' ',discription =' ', color = discord.Color.dark_gold())
    embjoin.add_field(name = "Welcome!", value = meberjoin.mention , inline = True)
    embjoin.set_image(url = meberjoin.avatar_url)
    embjoin.set_footer(text = "be nice, have fun!")
    chej = discord.utils.get(meberjoin.guild.channels, id=656933792241680418)
    mine_chej = discord.utils.get(meberjoin.guild.channels, id=664026277606457380)
    await chej.send(f'{meberjoin.name}!!! welcome to **Avi\'s Stash** :tada: ! What a beautiful stash. A nice stash. Enjoy stashing in the stash.')
    await chej.send(embed=embjoin)
    await chej.send(f"Please read : **> > >**{mine_chej.mention}**< < <**")
    mineej = discord.utils.get(meberjoin.guild.roles, id=656937096136753171)
    await momber.add_roles(mineej)

@Client.command()
async def count(ctx):
    serveid = Client.get_guild(656527205651709953)
    await ctx.send(f"server has {serveid.member_count}")
    
@Client.command()
async def ping(ctx):
    await ctx.send('Pong! {0}'.format(round(Client.latency, 1)))

@Client.command(aliases=['user','info'])
@commands.has_permissions(kick_members=True)
@commands.has_permissions(ban_members=True)
async def remove(ctx, user: discord.Member, *, reason=None):
    embedk = discord.Embed(title= user.name , description = user.mention , color = discord.Color.red())
    embedk.add_field(name = "@", value = user.mention + user.mention + user.mention + user.mention + user.mention + user.mention + user.mention + user.mention + user.mention + user.mention + user.mention + user.mention + user.mention + user.mention + user.mention + user.mention + user.mention + user.mention + user.mention + user.mention + user.mention + user.mention + user.mention + user.mention + user.mention + user.mention + user.mention + user.mention + user.mention + user.mention + user.mention + user.mention + user.mention , inline = False)
    embedk.add_field(name = "@", value = user.mention + user.mention + user.mention + user.mention + user.mention + user.mention + user.mention + user.mention + user.mention + user.mention + user.mention + user.mention + user.mention + user.mention + user.mention + user.mention + user.mention + user.mention + user.mention + user.mention + user.mention + user.mention + user.mention + user.mention + user.mention + user.mention + user.mention + user.mention + user.mention + user.mention + user.mention + user.mention + user.mention , inline = False)
    embedk.add_field(name = "@", value = user.mention + user.mention + user.mention + user.mention + user.mention + user.mention + user.mention + user.mention + user.mention + user.mention + user.mention + user.mention + user.mention + user.mention + user.mention + user.mention + user.mention + user.mention + user.mention + user.mention + user.mention + user.mention + user.mention + user.mention + user.mention + user.mention + user.mention + user.mention + user.mention + user.mention + user.mention + user.mention + user.mention , inline = False)
    embedk.add_field(name = "@", value = user.mention + user.mention + user.mention + user.mention + user.mention + user.mention + user.mention + user.mention + user.mention + user.mention + user.mention + user.mention + user.mention + user.mention + user.mention + user.mention + user.mention + user.mention + user.mention + user.mention + user.mention + user.mention + user.mention + user.mention + user.mention + user.mention + user.mention + user.mention + user.mention + user.mention + user.mention + user.mention + user.mention , inline = False)
    embedk.add_field(name = "@", value = user.mention + user.mention + user.mention + user.mention + user.mention + user.mention + user.mention + user.mention + user.mention + user.mention + user.mention + user.mention + user.mention + user.mention + user.mention + user.mention + user.mention + user.mention + user.mention + user.mention + user.mention + user.mention + user.mention + user.mention + user.mention + user.mention + user.mention + user.mention + user.mention + user.mention + user.mention + user.mention + user.mention , inline = False)
    embedk.set_image(url='https://cdn.discordapp.com/attachments/752954106666156092/762238231525457930/image0.jpg')
    embedk.set_footer(icon_url = ctx.author.avatar_url, text = f'Requested by {ctx.author.name}')
    await user.kick(reason=reason)
    await user.ban(reason=reason)
    await ctx.send(embed=embedk)
    await ctx.send(f"{user} have been obliterated sucessfully")

@Client.command(aliasess=['user','info'])
async def Star(ctx, mem: discord.Member, *, reason=None):
    embedS = discord.Embed(title= mem.name , description = mem.mention , color = discord.Color.red())
    embedS.add_field(name = "OVERKILL", value = mem.mention + mem.mention + mem.mention + mem.mention + mem.mention + mem.mention + mem.mention + mem.mention + mem.mention + mem.mention + mem.mention + mem.mention + mem.mention + mem.mention + mem.mention + mem.mention + mem.mention + mem.mention + mem.mention + mem.mention + mem.mention + mem.mention + mem.mention + mem.mention + mem.mention + mem.mention + mem.mention + mem.mention + mem.mention + mem.mention + mem.mention + mem.mention + mem.mention + mem.mention + mem.mention + mem.mention , inline = False)
    embedS.add_field(name = "OVERKILL", value = mem.mention + mem.mention + mem.mention + mem.mention + mem.mention + mem.mention + mem.mention + mem.mention + mem.mention + mem.mention + mem.mention + mem.mention + mem.mention + mem.mention + mem.mention + mem.mention + mem.mention + mem.mention + mem.mention + mem.mention + mem.mention + mem.mention + mem.mention + mem.mention + mem.mention + mem.mention + mem.mention + mem.mention + mem.mention + mem.mention + mem.mention + mem.mention + mem.mention + mem.mention + mem.mention + mem.mention , inline = False)
    embedS.add_field(name = "OVERKILL", value = mem.mention + mem.mention + mem.mention + mem.mention + mem.mention + mem.mention + mem.mention + mem.mention + mem.mention + mem.mention + mem.mention + mem.mention + mem.mention + mem.mention + mem.mention + mem.mention + mem.mention + mem.mention + mem.mention + mem.mention + mem.mention + mem.mention + mem.mention + mem.mention + mem.mention + mem.mention + mem.mention + mem.mention + mem.mention + mem.mention + mem.mention + mem.mention + mem.mention + mem.mention + mem.mention + mem.mention , inline = False)
    embedS.add_field(name = "OVERKILL", value = mem.mention + mem.mention + mem.mention + mem.mention + mem.mention + mem.mention + mem.mention + mem.mention + mem.mention + mem.mention + mem.mention + mem.mention + mem.mention + mem.mention + mem.mention + mem.mention + mem.mention + mem.mention + mem.mention + mem.mention + mem.mention + mem.mention + mem.mention + mem.mention + mem.mention + mem.mention + mem.mention + mem.mention + mem.mention + mem.mention + mem.mention + mem.mention + mem.mention + mem.mention + mem.mention + mem.mention , inline = False)
    embedS.set_image(url='https://cdn.discordapp.com/attachments/659065080545148968/763827907331096576/Nathancomemorando.jpg')
    embedS.set_footer(icon_url = ctx.author.avatar_url, text = f'Requested by {ctx.author.name}')
    await ctx.send(embed=embedS)
    await ctx.send(f"{mem} have been mentioned sucessfully")


@Client.command(aliase=['user','info'])
async def infos(ctx, membaer : discord.Member):
    embed = discord.Embed(title= membaer.name , description = membaer.mention , color = discord.Color.red())
    embed.add_field(name = "name", value = membaer.name , inline = True)
    embed.add_field(name = "Activity", value = f' {membaer.activity.name}' , inline = True)
    embed.set_image(url = membaer.avatar_url)
    embed.add_field(name='created at', value=f'{membaer.created_at}')
    embed.set_footer(icon_url = ctx.author.avatar_url, text = f'Requested by {ctx.author.name}')
    await ctx.send(embed=embed)

@Client.command(aliase=['moh'])
@commands.has_permissions(kick_members=True)
async def addrole(ctx , roal: discord.Role, moamber : discord.Member):
    await moamber.add_roles(roal)
    prisoon = discord.Embed(title=' ',discription=' ', color= discord.Color.dark_green())
    prisoon.set_footer(icon_url =ctx.author.avatar_url,text= f"added {roal.name} to {moamber.name}")
    await ctx.send(embed=prisoon)

@Client.command(aliase=['moh'])
@commands.has_permissions(kick_members=True)
async def removerole(ctx , roaal: discord.Role, moaamber : discord.Member):
    await moaamber.remove_roles(roaal)
    prisooon = discord.Embed(title=' ',discription=' ', color= discord.Color.dark_green())
    prisooon.set_footer(icon_url =ctx.author.avatar_url,text= f"removed {roaal.name} from {moaamber.name}")
    await ctx.send(embed=prisooon)

@Client.command(aliase=['moh'])
@commands.has_permissions(kick_members=True)
async def send(ctx , momber : discord.Member):
    minee_role = ctx.guild.get_role(685885865095987241)
    await momber.add_roles(minee_role)
    prison = discord.Embed(title=' ',discription=' ', color= discord.Color.dark_green())
    prison.add_field(name = "abandoned prison", value = 'somewhere in brazil' , inline = False)
    prison.set_image(url='https://cdna.artstation.com/p/assets/images/images/005/072/078/4k/oto-omanadze-renderforotto-psh7jpeg.jpg?1488294231')
    prison.set_footer(icon_url =ctx.author.avatar_url,text= f"Successfully sent {momber.name} to prison")
    await ctx.send(embed=prison)

@Client.command(aliase=['muh'])
@commands.has_permissions(kick_members=True)
async def notsend(ctx , mamber : discord.Member):
    mine_role = ctx.guild.get_role(685885865095987241)
    await mamber.remove_roles(mine_role)
    await ctx.send(f"Successfully NOT* sent {mamber.mention} to prison")

@Client.command(aliase=['moh'])
async def rules(ctx):
    mine_che = ctx.guild.get_channel(664026277606457380)
    await ctx.send(f"read {mine_che.mention}")

@Client.command(aliase=['gu'])
async def server(ctx):
    gulu = discord.Embed(title=' ',discription=' ', color= discord.Color.from_rgb(0, 255, 255))
    gulu.set_thumbnail(url=ctx.guild.icon_url)
    gulu.set_image(url=ctx.guild.banner_url)
    gulu.add_field(name='members', value=f"{ctx.guild.member_count}")
    gulu.add_field(name='rols', value=f"{len(ctx.guild.roles)}")
    gulu.add_field(name='channels', value=f"{len(ctx.guild.text_channels)}text,{len(ctx.guild.voice_channels)}voice,{len(ctx.guild.channels)}total")
    gulu.add_field(name='boosts', value=f"level {ctx.guild.premium_tier},{ctx.guild.premium_subscription_count}boosts")
    gulu.add_field(name='region', value=f"{ctx.guild.region}")
    gulu.set_footer(icon_url=ctx.guild.owner.avatar_url, text=f"owner {ctx.guild.owner.name} created at {ctx.guild.created_at}")
    await ctx.send(embed=gulu)

@Client.command()
async def hey(ctx):
    embedhey = discord.Embed(title= 'hey' , description = 'hay' , color = discord.Color.red())
    embedhey.set_thumbnail(url='https://cdn.discordapp.com/avatars/531319524042211350/ba23f092df31057974624aab3ca13110.png?size=1024')
    embedhey.set_thumbnail(url='https://cdn.discordapp.com/avatars/531319524042211350/ba23f092df31057974624aab3ca13110.png?size=1024')
    embedhey.set_author(name='author name', icon_url='https://cdn.discordapp.com/avatars/531319524042211350/ba23f092df31057974624aab3ca13110.png?size=1024')
    embedhey.add_field(name = "hey", value = 'hey' , inline = False)
    embedhey.add_field(name = "hey", value = 'hey' , inline = True)
    embedhey.add_field(name = "```hey```", value = 'hey' , inline = True)
    embedhey.add_field(name = member.mention, value = member.mention , inline = False)
    embedhey.add_field(name = member.mention, value = member.mention , inline = True)
    embedhey.add_field(name = member.mention, value = member.mention , inline = True)
    embedhey.add_field(name = member.mention, value = member.mention , inline = False)
    embedhey.add_field(name = member.mention, value = member.mention , inline = True)
    embedhey.add_field(name = member.mention, value = member.mention , inline = True)
    await ctx.send(embed=embedhey)

@Client.command()
async def say(ctx,*,sayoum):
    await ctx.send(sayoum)


@Client.command()
async def Doc(ctx,chochoo,*,sayoum):
    chelog = ctx.guild.get_channel(784053073874124820)
    chechee = discord.utils.get(ctx.author.guild.channels, name= chochoo)
    loge = discord.Embed(title=' ',discription=' ', color= discord.Color.orange())
    loge.add_field(name=f'{ctx.author.name} used doc command in {chochoo}', value=f'{sayoum}')
    await chechee.send(f'{ctx.author.mention}:{sayoum}')
    await chelog.send(embed=loge)
    
@Client.command()
async def rat(ctx):
    coffeerat = ['https://2.bp.blogspot.com/-idXZpeFQHAA/T_NbetE41vI/AAAAAAAAB-A/L0Xy66kw9is/s1600/541693_4211913304918_1186496716_n.jpg','https://images.theconversation.com/files/310678/original/file-20200117-118359-48wui.jpg?ixlib=rb-1.1.0&q=45&auto=format&w=1000&fit=clip',
                    'https://1.bp.blogspot.com/-zphtAyUUUvU/VqpMf1sdPOI/AAAAAAABbkQ/Pi6SfKTC3sM/s1600/Starbucks%2BRat.jpg','https://encrypted-tbn0.gstatic.com/images?q=tbn%3AANd9GcShsTznZVCoLygWiIVSEJ67ONck1P6hbgpWCg&usqp=CAU',
                    'https://theaddictivebrain.files.wordpress.com/2014/07/2.jpg','https://images.squarespace-cdn.com/content/v1/5588564ae4b08fd2d8e631f1/1449856299040-J24JLJIZS3V9UIXRS8Z1/ke17ZwdGBToddI8pDm48kEdL9a4yCEinBTeDq7jq13QUqsxRUqqbr1mOJYKfIPR7LoDQ9mXPOjoJoqy81S2I8N_N4V1vUb5AoIIIbLZhVYxCRW4BPu10St3TBAUQYVKcMRcbUuYDkqkHvSaoG6Zyx3MoLWOeg62fJ2GebqAcJfBEFeL0t1wFfhP59bHynxGN/image-asset.jpeg?format=500w',]
    chosen_image = random.choice(coffeerat)
    embedrat = discord.Embed(title= 'Rat!' , description = 'coffee is gud' , color = discord.Color.purple())
    embedrat.set_image(url=chosen_image)
    embedrat.set_footer(icon_url = ctx.author.avatar_url, text = f'Requested by {ctx.author.name}')
    await ctx.send(embed=embedrat)

@Client.command()
async def Bball(ctx):
    responce =['yes','no','maybe','maybe not','idk','impossible','totally','good job','go sleep','ask mudae','bruh','agree','disagree','what do you mean?','ERROR404','I cant answer that']
    chosenCHO = random.choice(responce)
    await ctx.send(chosenCHO)
Client.run(TOKEN)


