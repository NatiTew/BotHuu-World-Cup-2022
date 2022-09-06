# from replit import db
# keys = db.keys()
# for row in keys:
#   del db[row]

import os
import discord
from datetime import datetime
from os import system
from time import sleep
from keepAlive import keep_alive
from discord.ext import commands
from replit import db
from discord.ext.commands import has_permissions, MissingPermissions

my_secret = os.environ['Token']
# my_secret = os.environ['TokenAdmin']

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
  dataID = db[tmpid]
  dataName = db[tmpname]
  dataPoint = db[tmppoint]
  # print(dataID)
  # print(dataName)
  # print(dataPoint)
  
  sum = 0
  index = -999
  if id in dataID:
    index = dataID.index(id)
    p = dataPoint[index]
    sum = (p + point)
    tmp = True
  # print(tmp)  
    
  if tmp == True:
    dataName[index] = name
    dataPoint[index] = sum
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
    sum = point
    # print(dataID)
    # print(dataName)
    # print(dataPoint)
    db[tmpid] = dataID
    db[tmpname] = dataName
    db[tmppoint] = dataPoint

  return sum

def cutData(choice:int, id:str, name:str, point:int):
  list = db["list"]
  tmp = False
  tmpid = list[choice-1] + '_id'
  tmpname = list[choice-1] + '_name'
  tmppoint = list[choice-1] + '_point'
  dataID = db[tmpid]
  dataName = db[tmpname]
  dataPoint = db[tmppoint]

  sum = 0
  index = -999
  if id in dataID:
    index = dataID.index(id)
    p = dataPoint[index]
    sum = (p - point)
    tmp = True
  else:
    return 777
  
  if sum < 0:
    return 999
  if tmp == True:
    dataName[index] = name
    dataPoint[index] = sum
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
  await ctx.send("❈────────•✦•กระดานคำสั่ง•✦•────────❈\n\n"
                  "─────────────Admin────────────\n"
                  "+make <ชื่อ>   → สร้างlist ที่ใช้เก็บคะแนน เช่น เกลือ\n"
                  "+list   → แสดงเลข list\n"
                  "+add <เลขlist> <@name> <แต้ม>    → เพิ่มแต้ม\n"
                  "+cut <เลขlist> <@name> <แต้ม>    → ลดแต้ม\n\n"
                  "─────────────User─────────────\n"
                  "+show   → เช็ค point ตัวเอง\n"
                  "+s <@name>   → เช็ค point คนอื่น\n"
                  "❈──────────•✦•❅•✦•──────────❈\n")

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
async def cut(ctx, choice: int, player: discord.Member, point: int):
  nameAdmin = str(ctx.author.name)
  list = db["list"]
  if choice <= 0 or choice > len(list) :
    await ctx.channel.send('Number of list is wrong')
  elif point < 1:
    await ctx.channel.send('Number of point is wrong')
  else:
    idP = str(player.id)
    nameP = str(player.name)
    sum = cutData(choice, idP, nameP, point)
    if sum == 999:
      await ctx.channel.send('Balance not enough')
    elif sum == 777:
      await ctx.channel.send('User never have point')
    else:
      log = '{} use method cut {} point to <{}>{} in {}'.format(nameAdmin, str(point), idP, nameP, list[choice-1])
      updateLog(log)
      await ctx.channel.send('<@{}> cut {} Point to {} , now you have {}'.format(idP, str(point), list[choice-1], str(sum)))
  
@client.command()
async def show(ctx):
  user_id = str(ctx.author)
  id = str(ctx.author.id)
  embed = discord.Embed(title=f"{'----------<Board>----------'}", description=('คะแนนของ ' + user_id),color=discord.Color.red())
  list = db["list"]
  for arr in list:
    tmpid = arr + '_id'
    tmppoint = arr + '_point'
    
    dataID = db[tmpid]
    dataPoint = db[tmppoint]

    index = 0
    
    if id in dataID:
      index = dataID.index(id)
      embed.add_field(name=arr, value=f"{str(dataPoint[index])}")
    else:
      embed.add_field(name=arr, value=f"{'0'}")
  await ctx.send(embed=embed)

@client.command()
async def s(ctx, player: discord.Member):
  user_id = str(player)
  id = str(player.id)
  embed = discord.Embed(title=f"{'----------<Board>----------'}", description=('คะแนนของ ' + user_id),color=discord.Color.red())
  list = db["list"]
  for arr in list:
    tmpid = arr + '_id'
    tmppoint = arr + '_point'
    
    dataID = db[tmpid]
    dataPoint = db[tmppoint]

    index = 0
    
    if id in dataID:
      index = dataID.index(id)
      embed.add_field(name=arr, value=f"{str(dataPoint[index])}")
    else:
      embed.add_field(name=arr, value=f"{'0'}")
  await ctx.send(embed=embed)
  
@add.error
async def add_error(ctx, error):
  if isinstance(error, MissingPermissions):
    text = "Sorry {}, you do not have permissions to do that!".format(ctx.message.author)
    await ctx.send(text)
@cut.error
async def cut_error(ctx, error):
  if isinstance(error, MissingPermissions):
    text = "Sorry {}, you do not have permissions to do that!".format(ctx.message.author)
    await ctx.send(text)
@make.error
async def make_error(ctx, error):
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
  
  
  