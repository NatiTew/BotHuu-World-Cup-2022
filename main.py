# from replit import db
# keys = db.keys()
# for row in keys:
#   del db[row]

import os
import numpy as np
import random
import discord
import collections
import time
import logging
import datetime
from datetime import datetime
from os import system
from itertools import repeat
from time import sleep
from keepAlive import keep_alive
from discord.ext import commands
from replit import db
from discord.ext.commands import has_permissions, MissingPermissions

#my_secret = os.environ['Token']
my_secret = os.environ['TokenAdmin']

client = commands.Bot(command_prefix='+')

def updateLog(text:str):
  now = datetime.now()
  date_time = now.strftime("%m/%d/%Y, %H:%M:%S")
  f = open("Log.txt", "a")
  f.write(date_time + " | " + text + "\n")
  f.close()

def chData():
  keys = db.keys()
  tmp = False
  for row in keys:
    if row == "list":
      tmp = True
      
  if tmp == False:
    db["list"] = []

def showData():
  keys = db.keys()
  tmp = 'System starting \nShow All Data \n'
  for row in keys:
    tmp += row + '\n'
  print(tmp)

def delData():
  keys = db.keys()
  for row in keys:
    del db[row]

#function fo user
def loopID():
  valueArr = []
  tmp = db["idPlayer"]
  for arr in range(len(tmp)):
    valueArr.append(tmp[arr])

def addData(choice:int, id:str, name:str, point:int):
  list = db["list"]
  tmp = False
  tmpid = list[choice-1] + '_id'
  tmpname = list[choice-1] + '_name'
  tmppoint = list[choice-1] + '_point'
  dataID = []
  dataName = db[tmpname]
  dataPoint = db[tmppoint]
  for arr in db[tmpid]:
    dataID.append(arr)
  
  p = 0
  num = 0
  while num < len(dataID):
    if dataID[num] == id:
      p = dataPoint[num]
      tmp = True
      break
    num += 1
  sum = (p + point)
  if tmp == True:
    dataName[num] = name
    dataPoint[num] = sum
    # print(dataID)
    # print(dataName)
    # print(dataPoint)
    db[tmpid] = dataID
    db[tmpname] = dataName
    db[tmppoint] = dataPoint
  else:
    dataID.append(id)
    dataName.append(name)
    dataPoint.append(point)
    # print(dataID)
    # print(dataName)
    # print(dataPoint)
    db[tmpid] = dataID
    db[tmpname] = dataName
    db[tmppoint] = dataPoint

  return sum

@client.event
async def on_ready():
    # delData()
    chData()
    showData()
    updateLog('System Starting...')
    print(f'Successfully logged in as {client.user}')
    

@client.command()
async def info(ctx):
  async for message in ctx.channel.history(limit=1):
    await message.delete()
  await ctx.send("❈────────•✦•กระดานคำสั่ง•✦•────────❈\n"
                  "(ทุกคนสามารถใช้ได้ทุกคน)\n\n"
                  "+show   → เช็ค point ตัวเอง\n"
                  "+s <@name>   → เช็ค point คนอื่น\n"
                  "+salt   → เปิด LeaderBoard 25 อันดับแรก\n\n"
                  "+gacha   → เปิด LeaderBoard 25 อันดับแรก\n\n"
                  "❈────────•✦•❅•✦•────────❈\n")

@client.command()
@has_permissions(administrator = True)
async def make(ctx, text: str):
  async for message in ctx.channel.history(limit=1):
    await message.delete()
  nameAdmin = str(ctx.author.name)
  list = db["list"]
  tmp = False
  for arr in list:
    if arr == text:
      tmp = True
      break
  if tmp == True:
    await ctx.channel.send(text + ' have in list already')
    log = '{} use method add {} to list, But it\'s in list already'.format(nameAdmin, text)
    updateLog(log)
  else:
    list.append(text)
    db["list"] = list
    
    log = '{} use method add {} to list, Add to list'.format(nameAdmin, text)
    updateLog(log)
    
    id = text + '_id'
    name = text + '_name'
    point = text + '_point'
    db[id] = []
    db[name] = []
    db[point] = []
    await ctx.channel.send(text + ' add to list')
    
    log = 'Create db of {}, it has {}, {} and {}'.format(text, id, name, point)
    updateLog(log)

@client.command()
@has_permissions(administrator = True)
async def list(ctx):
  async for message in ctx.channel.history(limit=1):
    await message.delete()
  nameAdmin = str(ctx.author.name)
  list = db["list"]
  num = 1
  output = '----------<In List have >----------\n'
  for arr in list:
    output += str(num) + '  is ' + arr + '\n'
    num += 1
  await ctx.channel.send(output)
  log = '{} use method list'.format(nameAdmin)
  updateLog(log)
  
@client.command()
@has_permissions(administrator = True)
async def add(ctx, choice: int, player: discord.Member, point: int):
  nameAdmin = str(ctx.author.name)
  list = db["list"]
  if choice <= 0 or choice > len(list) :
    await ctx.channel.send('Number of list is wrong')
  elif point < 1:
    await ctx.channel.send('Number of point is wrong')
  else:
    idP = str(player.id)
    nameP = str(player.name)
    sum = addData(choice, idP, nameP, point)
    log = '{} use method add {} point to <{}>{} in {}'.format(nameAdmin, str(point), idP, nameP, list[choice-1])
    updateLog(log)
    await ctx.channel.send('<@{}> add {} Point to {} , now you have {}'.format(idP, str(point), list[choice-1], str(sum)))
  
@client.command()
@has_permissions(administrator = True)
async def add1(ctx, player: discord.Member, input: int):
  sPlayer = str(player.id)
  np = 'n' + str(player.id)
  nPlayer = str(player.name)
  check = False
  keys = db.keys()
  for row in keys:
    if row == sPlayer:
      check = True
      # print(check)
      break
  if check == True:
    value = db[sPlayer]
    value[1] = (value[1] + input)
    # print(value[0])
    db[sPlayer] = value
    db[np] = nPlayer
  else:
    db[np] = nPlayer
    arr = ['player',0,0]
    arr[1] = input
    # print(arr[0])
    db[sPlayer] = arr
  # print('<@'+ sPlayer +'> add '+ str(input) +'♚DouCoin')
  await ctx.channel.send('<@'+ sPlayer +'> add '+ str(input) +'♚Salt')


@add1.error
async def add1_error(ctx, error):
  if isinstance(error, MissingPermissions):
    text = "Sorry {}, you do not have permissions to do that!".format(ctx.message.author)
    await ctx.send(text)

@client.command(pass_context = True)
@has_permissions(administrator = True)
async def whoami(ctx):
  await ctx.send('คุณเป็น administrator')

@whoami.error
async def whoami_error(ctx, error):
  if isinstance(error, MissingPermissions):
    text = "Sorry {}, you do not have permissions to do that!".format(ctx.message.author)
    await ctx.send(text)



@client.command()
async def restart(ctx): 
  await ctx.channel.send('Test Restart')
  print("\n\nRESTARTING NOW\n\n\n")
  await ctx.channel.send('kill process')
  print('kill')
  system('kill 1')
  await ctx.channel.send('sleep')
  print('sleep')
  sleep(7)
  await ctx.channel.send('restart')
  print('restart')
  system("python main.py")

keep_alive()
try:
    client.run(my_secret)
except discord.errors.HTTPException:
  print("\n\n\nBLOCKED BY RATE LIMITS\nRESTARTING NOW\n\n\n")
  system("python restarter.py")
  
  
  