import discord
from discord.ext import commands
from discord import client
import random



client = commands.Bot(command_prefix="!", case_insensitive=True)

########Start########
@client.event
async def on_ready():
    print("###-LitheKong Is Online-###")


#######PING#######

@client.command(name='ping')
async def ping(ctx):
    await ctx.send(f'**BUM!** Latencia: {round(client.latency * 1000)}ms')

#######STREAMERS#######

@client.command(name='streamers')
async def stremers(ctx):
    embed = discord.Embed(title='Stremer#1', color=discord.Colour.blue())
    embed.set_image(
        url='https://static-cdn.jtvnw.net/jtv_user_pictures/cfd5e66a-f247-4158-be16-5aa5068f13a0-profile_image-70x70.png')
    embed.add_field(name='ID:', value='@Dux')
    embed.add_field(name='URL:', value='https://www.twitch.tv/igdux')

    await ctx.send(embed=embed)

    embed = discord.Embed(title='Streamer#2', color=discord.Colour.blue())
    embed.set_image(
        url='https://static-cdn.jtvnw.net/jtv_user_pictures/6b4441ff-a6bf-4609-bc1d-32cba5b51c61-profile_image-70x70.png')
    embed.add_field(name='ID:', value='@F4')
    embed.add_field(name='URL:', value='https://www.twitch.tv/f4_zzz')

    await ctx.send(embed=embed)
    embed = discord.Embed(title='Streamer#3', color=discord.Colour.blue())
    embed.set_image(
        url='https://static-cdn.jtvnw.net/jtv_user_pictures/d05c03ad-4e70-4734-9159-51fc1477d564-profile_image-70x70.png')
    embed.add_field(name='ID:', value='@Héset')
    embed.add_field(name='URL:', value='https://www.twitch.tv/1heset')

    await ctx.send(embed=embed)
    embed = discord.Embed(title='Streamer#4', color=discord.Colour.blue())
    embed.set_image(
        url='https://static-cdn.jtvnw.net/jtv_user_pictures/216fb513-c711-4d1e-abd6-0503b9744c18-profile_image-70x70.png')
    embed.add_field(name='ID:', value='@Japoleca')
    embed.add_field(name='URL:', value='https://www.twitch.tv/japoleca')

    await ctx.send(embed=embed)


#########-Campeonato-HaxBoll-#############

def log(text):
    with open('jogadorescamp.txt', 'a') as file_log:
        file_log.write(text)

@client.command(name='inscrever')
async def insrever(ctx):
    user = ctx.message.author.name
    log(user+'\n')
    print(user)
    embed = discord.Embed(title='Campeonato Oficial de HAXBALL da Gorilândia', color=discord.Colour.blue())
    embed.set_image(
        url='https://cdn.titotu.io/images/games/haxball-com-839x472.jpg')
    embed.add_field(name='ID:', value=f'{user}')
    embed.add_field(name='Situação:', value='Inscrição Confirmada!')

    await ctx.send(embed=embed)


@client.command(name='hbcamp')
async def camp(ctx, modor):
    jogadores = []
    txt = open("jogadorescamp.txt", 'r')
    await ctx.send(f'Jogadores Inscritos:')
    for word in txt:
        print(word)
        jogadores.append(word[:-1])

    embed = discord.Embed(title='Jogadores Inscritos', color=discord.Colour.blue())
    for i in range(0, len(jogadores)):
        embed.add_field(name='- - -', inline=True, value=f'{jogadores[i]}')
    await ctx.send(embed=embed)

    times = []
    time1 = []
    time2 = []
    time3 = []
    time4 = []
    time5 = []
    time6 = []
    time7 = []
    modo = modor
        #input('Qual é o modo? (SOLO / DUO / TRIO) ')

    # MODOS  ---------------------------------------------------------------------------------
    if modo == 'TRIO':
        for i in range(0, len(jogadores)):
            x = random.choice(jogadores)
            jogadores.remove(x)
            if len(time1) < 3:
                time1.insert(0, x)
            elif len(time2) < 3:
                time2.insert(0, x)
            elif len(time3) < 3:
                time3.insert(0, x)
            elif len(time4) < 3:
                time4.insert(0, x)
            elif len(time5) < 3:
                time5.insert(0, x)
            elif len(time6) < 3:
                time6.insert(0, x)
            elif len(time7) < 3:
                time7.insert(0, x)
            else:
                jogadores.insert(0, x)

        # print's
        embed = discord.Embed(title='TIMES', color=discord.Colour.blue())
        if len(time1) == 3:
            embed.add_field(name='Time 1:', value=f'{str(time1[0])} + {time1[1]} + {time1[2]}')
            times.insert(0, 'time1')
        if len(time2) == 3:
            embed.add_field(name='Time 2:', value=f'{str(time2[0])} + {time2[1]} + {time2[2]}')
            times.insert(0, 'time2')
        if len(time3) == 3:
            embed.add_field(name='Time 3:', value=f'{str(time3[0])} + {time3[1]} + {time3[2]}')
            times.insert(0, 'time3')
        if len(time4) == 3:
            embed.add_field(name='Time 4:', value=f'{str(time4[0])} + {time4[1]} + {time4[2]}')
            times.insert(0, 'time4')
        if len(time5) == 3:
            embed.add_field(name='Time 5:', value=f'{str(time5[0])} + {time5[1]} + {time5[2]}')
            times.insert(0, 'time5')
        if len(time6) == 3:
            embed.add_field(name='Time 6:', value=f'{str(time6[0])} + {time6[1]} + {time6[2]}')
            times.insert(0, 'time6')
        if len(time7) == 3:
            embed.add_field(name='Time 7:', value=f'{str(time7[0])} + {time7[1]} + {time7[2]}')
            times.insert(0, 'time7')

        await ctx.send(embed=embed)




    if modo == 'DUO':
        for i in range(0, len(jogadores)):
            x = random.choice(jogadores)
            jogadores.remove(x)
            if len(time1) < 2:
                time1.insert(0, x)
            elif len(time2) < 2:
                time2.insert(0, x)
            elif len(time3) < 2:
                time3.insert(0, x)
            elif len(time4) < 2:
                time4.insert(0, x)
            elif len(time5) < 2:
                time5.insert(0, x)
            elif len(time6) < 2:
                time6.insert(0, x)
            elif len(time7) < 2:
                time7.insert(0, x)
            else:
                jogadores.insert(0, x)

        # print's
        embed = discord.Embed(title='TIMES', color=discord.Colour.blue())
        if len(time1) == 3:
            embed.add_field(name='Time 1:', value=f'{str(time1[0])} + {time1[1]}')
            times.insert(0, 'time1')
        if len(time2) == 3:
            embed.add_field(name='Time 2:', value=f'{str(time2[0])} + {time2[1]}')
            times.insert(0, 'time2')
        if len(time3) == 3:
            embed.add_field(name='Time 3:', value=f'{str(time3[0])} + {time3[1]}')
            times.insert(0, 'time3')
        if len(time4) == 3:
            embed.add_field(name='Time 4:', value=f'{str(time4[0])} + {time4[1]}')
            times.insert(0, 'time4')
        if len(time5) == 3:
            embed.add_field(name='Time 5:', value=f'{str(time5[0])} + {time5[1]}')
            times.insert(0, 'time5')
        if len(time6) == 3:
            embed.add_field(name='Time 6:', value=f'{str(time6[0])} + {time6[1]}')
            times.insert(0, 'time6')
        if len(time7) == 3:
            embed.add_field(name='Time 7:', value=f'{str(time7[0])} + {time7[1]}')
            times.insert(0, 'time7')

        await ctx.send(embed=embed)

    if modo == 'SOLO':
        for i in range(0, len(jogadores)):
            x = random.choice(jogadores)
            jogadores.remove(x)
            if len(time1) < 1:
                time1.insert(0, x)
            elif len(time2) < 1:
                time2.insert(0, x)
            elif len(time3) < 1:
                time3.insert(0, x)
            elif len(time4) < 1:
                time4.insert(0, x)
            elif len(time5) < 1:
                time5.insert(0, x)
            elif len(time6) < 1:
                time6.insert(0, x)
            elif len(time7) < 1:
                time7.insert(0, x)
            else:
                jogadores.insert(0, x)

        # print's
        embed = discord.Embed(title='TIMES', color=discord.Colour.blue())
        if len(time1) == 3:
            embed.add_field(name='Time 1:', value=f'{str(time1[0])}')
            times.insert(0, 'time1')
        if len(time2) == 3:
            embed.add_field(name='Time 2:', value=f'{str(time2[0])}')
            times.insert(0, 'time2')
        if len(time3) == 3:
            embed.add_field(name='Time 3:', value=f'{str(time3[0])}')
            times.insert(0, 'time3')
        if len(time4) == 3:
            embed.add_field(name='Time 4:', value=f'{str(time4[0])}')
            times.insert(0, 'time4')
        if len(time5) == 3:
            embed.add_field(name='Time 5:', value=f'{str(time5[0])}')
            times.insert(0, 'time5')
        if len(time6) == 3:
            embed.add_field(name='Time 6:', value=f'{str(time6[0])}')
            times.insert(0, 'time6')
        if len(time7) == 3:
            embed.add_field(name='Time 7:', value=f'{str(time7[0])}')
            times.insert(0, 'time7')

        await ctx.send(embed=embed)

    # ---------------------------------------------------------------------------------

    print(times)

    # para calcular o numero de jogos totais:
    t = len(times)
    t2 = len(times)
    while t != 1:
        t -= 1
        t2 *= t
    # print(t2)
    t3 = len(times) - 2
    t4 = t3
    while t3 != 1:
        t3 -= 1
        t4 *= t3
    # print(t4)
    t5 = t2 / (t4 * 2)
    print('Número de partidas: ', t5)
    numdejogos = int(t5 + 1)
    # ------------------------------------

    embed = discord.Embed(title='Partidas Definidas:', color=discord.Colour.blue())
    if len(times) == 3:
        embed.add_field(name='Partida 1 ✔', value='Time 1 x Time 2')
        embed.add_field(name='Partida 2 ✔', value='Time 1 x Time 3')
        embed.add_field(name='Partida 3 ✔', value='Time 2 x Time 2')
    if len(times) == 4:
        embed.add_field(name='Partida 1 ✔', value='Time 1 x Time 2')
        embed.add_field(name='Partida 2 ✔', value='Time 3 x Time 4')
        embed.add_field(name='Partida 3 ✔', value='Time 1 x Time 3')
        embed.add_field(name='Partida 4 ✔', value='Time 3 x Time 2')
        embed.add_field(name='Partida 5 ✔', value='Time 1 x Time 4')
        embed.add_field(name='Partida 6 ✔', value='Time 4 x Time 2')
    if len(times) == 5:
        embed.add_field(name='Partida 1 ✔', value='Time 1 x Time 2')
        embed.add_field(name='Partida 2 ✔', value='Time 3 x Time 4')
        embed.add_field(name='Partida 3 ✔', value='Time 1 x Time 5')
        embed.add_field(name='Partida 4 ✔', value='Time 3 x Time 2')
        embed.add_field(name='Partida 5 ✔', value='Time 4 x Time 5')
        embed.add_field(name='Partida 6 ✔', value='Time 1 x Time 3')
        embed.add_field(name='Partida 7 ✔', value='Time 2 x Time 4')
        embed.add_field(name='Partida 8 ✔', value='Time 3 x Time 5')
        embed.add_field(name='Partida 9 ✔', value='Time 1 x Time 4')
        embed.add_field(name='Partida 10 ✔', value='Time 2 x Time 5')
    if len(times) == 6:
        embed.add_field(name='Partida 1 ✔', value='Time 1 x Time 2')
        embed.add_field(name='Partida 2 ✔', value='Time 3 x Time 4')
        embed.add_field(name='Partida 3 ✔', value='Time 6 x Time 1')
        embed.add_field(name='Partida 4 ✔', value='Time 1 x Time 5')
        embed.add_field(name='Partida 5 ✔', value='Time 3 x Time 2')
        embed.add_field(name='Partida 6 ✔', value='Time 6 x Time 5')
        embed.add_field(name='Partida 7 ✔', value='Time 4 x Time 5')
        embed.add_field(name='Partida 8 ✔', value='Time 2 x Time 6')
        embed.add_field(name='Partida 9 ✔', value='Time 1 x Time 3')
        embed.add_field(name='Partida 10 ✔', value='Time 2 x Time 4')
        embed.add_field(name='Partida 11 ✔', value='Time 6 x Time 3')
        embed.add_field(name='Partida 12 ✔', value='Time 3 x Time 5')
        embed.add_field(name='Partida 13 ✔', value='Time 1 x Time 4')
        embed.add_field(name='Partida 14 ✔', value='Time 2 x Time 5')
        embed.add_field(name='Partida 15 ✔', value='Time 4 x Time 6')
    await ctx.send(embed=embed)



client.run("")

