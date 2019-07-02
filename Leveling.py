import discord
import random
import json
import os
from discord.ext import commands

client = commands.Bot(command_prefix = 'd-')
client.remove_command('help')
#os.chdir(r'C:\Users\edrin\Desktop\test')
@client.event 
async def on_ready():
    print('ready')

@client.event 
async def on_member_join(member): 
    with open('users.json','r') as f: 
        users = json.load(f) 
    
    await update_data(users, member)
    
    with open('users.json', 'w') as f:
        json.dump(users, f)

@client.event 
async def on_message(message):
    with open('users.json', 'r') as f:
        users = json.load(f)

    await update_data(users, message.author)
    await add_experience(users, message.author, 5)
    await level_up(users, message.author, message.channel)

    with open('users.json', 'w') as f:
        json.dump(users, f)
    

async def update_data(users, user):
    try:
        if not user.id in users:
            users[user.id] = {}
            users[user.id]['experience'] = 0
            users[user.id]['level'] = 1
    except Exception:
        pass

async def add_experience(users, user, exp):
    users[user.id]['experience'] += exp

async def level_up(users, user, channel):
    experience = users[user.id]['experience']
    lvl_start = users[user.id]['level']
    lvl_end = int(experience ** (1/4))

    try:
        if lvl_start < lvl_end:
            if user != client.user and user.bot == False:
                embed=discord.Embed(color=0x00a2f6,title="Level up!",description='<:Dartexlevelup:539854740633157672> | {}, you just leveled up to level {}!'.format(user.name,lvl_end))
                await channel.send(embed=embed)
                #await client.add_reaction(lev, emoji="⤴")
                print(f"{user.name} leveled up to level {lvl_end}, user's ID: {user.id}")
                To = client.get_channel('533713132791791624')
                await To.send(f"<@493075860975386646>, {user.name} leveled up to level {lvl_end}, user's ID: {user.id}")
                users[user.id]['level'] = lvl_end
            else:
                pass
    except Exception as e:
        print(e)
client.run(os.getenv('TOKEN'))
#client.run('')
