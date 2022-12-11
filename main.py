# import sqlite3
# from replit import db

# connection = sqlite3.connect("myDatabase.db")
# cursor = connection.cursor()
# nametable1 = "correct"
# nametable2 = "wrong"
# # cursor.execute("CREATE TABLE {} (disID TEXT, Score INTEGER)".format(nametable1))
# # cursor.execute("CREATE TABLE {} (disID TEXT, Score INTEGER)".format(nametable2)) 

# # value1 = db["ทายผิด_id"]
# # value2 = db["ทายผิด_point"]
# # for arr in range(len(value1)):
# #   cursor.execute("INSERT INTO wrong VALUES ('{}',{})".format(str(value1[arr]), int(value2[arr])))

# rows = cursor.execute("SELECT * FROM correct").fetchall()
# print(rows)
# rows1 = cursor.execute("SELECT * FROM wrong").fetchall()
# print(rows1)


# connection.commit()
# connection.close()


  
import sqlite3
import os
import discord
import re
from datetime import datetime
from os import system
from time import sleep
from keepAlive import keep_alive
from discord.ext import commands
from replit import db
from discord.ext.commands import has_permissions, MissingPermissions
from discord.utils import get
from discord import Member, Role


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

def addData(choice:int, id:str, point:int):
  list = db["list"]
  text = list[choice-1]
  sum = 0

  connection = sqlite3.connect("myDatabase.db")
  cursor = connection.cursor()
  result  = cursor.execute("SELECT * from {} WHERE disID = '{}' ".format(text, id)).fetchall();
  print(result)
  arr = len(result)
  # print(arr)
  
  if arr == 0:
    cursor.execute("INSERT INTO {} VALUES ('{}',{})".format(text, id, point))
    # print(cursor)
    sum = point
    connection.commit()
  else:
    score = result[0][1] + point
    # print(score)
    cursor.execute("UPDATE {} SET Score = {} WHERE disID = '{}'".format(text, score, id))
    # print(cursor)
    sum = score
    connection.commit()
    
  connection.close()

  return sum
  
# addData(1, '<@358984660342145025>', 9)

def cutData(choice:int, id:str, point:int):
  list = db["list"]
  text = list[choice-1]
  sum = 0

  connection = sqlite3.connect("myDatabase.db")
  cursor = connection.cursor()
  result  = cursor.execute("SELECT * from {} WHERE disID = '{}' ".format(text, id)).fetchall();
  print(result)
  arr = len(result)
  
  # print(arr)
  sum = 0
  if arr != 0:
    score = result[0][1] - point
    if score < 0:
      return 999
    else:
      cursor.execute("UPDATE {} SET Score = {} WHERE disID = '{}'".format(text, score, id))
      connection.commit()
      connection.close()
  else:
    return 777
  
  
  return score

def idDisSplit(id:str):
  x = id.split("<")
  y = x[1].split("@")
  z = y[1].split(">")

  return z[0]


@client.event
async def on_ready():
    chData()
    showData()
    updateLog('System Starting...')
    print(f'Successfully logged in as {client.user}')
    

@client.command()
async def info(ctx):
  async for message in ctx.channel.history(limit=1):
    await message.delete()
  await ctx.send("❈────────•✦•กระดานคำสั่ง•✦•────────❈\n\n"
                  "─────────────User─────────────\n"
                  "+role   → รับโรล ⚽WolrdCup \n"
                  "+show   → เช็คผลตัวเอง\n"
                  "+s <@name>   → เช็คผลคนอื่น\n"
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
    
    nametable = text
    connection = sqlite3.connect("myDatabase.db")
    cursor = connection.cursor()
    cursor.execute("CREATE TABLE {} (disID TEXT, Score INTEGER)".format(nametable))
    print("Table created successfully........")
    connection.commit()
    connection.close()
    
    await ctx.channel.send('»——————⋆◦★◦⋆——————«\n                 ' + text + ' add to list' + '\n»——————⋆◦★◦⋆——————«')
    
    

@client.command()
@has_permissions(administrator = True)
async def delist(ctx, text: str):
  nameAdmin = str(ctx.author.name)
  list = db["list"]
  if text in list:
    # id = text + '_id'
    # # name = text + '_name'
    # point = text + '_point'
    # del db[id]
    # # del db[name]
    # del db[point]
    list.remove(text)

    connection = sqlite3.connect("myDatabase.db")
    cursor = connection.cursor()
    cursor.execute("DROP TABLE {}".format(text))
    connection.commit()
    connection.close()
  
    await ctx.channel.send('List ' + text + ' was delete')
    log = '{} use method delist for Delete {} out of list'.format(nameAdmin, text)
    updateLog(log)
  else:
    await ctx.channel.send('Not Found')
  
@client.command()
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
  



@client.command(pass_context=True)
async def role(ctx):
  role_object = discord.utils.get(ctx.message.guild.roles, name='worldcup⚽')
  await ctx.author.add_roles(role_object)
  await ctx.channel.send('<@'+str(ctx.author.id) + '>ได้โรล '+str(role_object)+' เรียบร้อย')

  
@client.command()
@has_permissions(administrator = True)
async def wc(ctx, choice: int, *args):
  point = 1
  nameAdmin = str(ctx.author.name)
  list = db["list"]
  if choice <= 0 or choice > len(list) :
    await ctx.channel.send('Number of list is wrong')
  elif point < 1:
    await ctx.channel.send('Number of point is wrong')
  else:
    await ctx.channel.send('น้องบอทขอประมวลผลแปปนึง...')
    for arr in args:
      # print(arr)
      idP = str(arr)
      # nameP = str(player.name)
      sum = addData(choice, idP, point)
      log = '{} use method add {} point to <{}> in {}'.format(nameAdmin, str(point), idP, list[choice-1])
      updateLog(log)
      # realid = idDisSplit(idP)
      # username = ctx.get_user(int(realid))
      # await ctx.channel.send('{} เพิ่มผล{} จำนวน {}คู่, ตอนนี้คุณ{} จำนวน {}คู่'.format(username, list[choice-1], str(point), list[choice-1], str(sum)))
    await ctx.channel.send('อัพเดตผล'+list[choice-1]+'เรียบร้อยแล้ว')

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
    idP = '<@' + str(player.id) + '>'
    # nameP = str(player.name)
    await ctx.channel.send('น้องบอทขอประมวลผลแปปนึง...')
    sum = addData(choice, idP, point)
    log = '{} use method add {} point to <{}> in {}, Now have {}'.format(nameAdmin, str(point), idP, list[choice-1], sum)
    updateLog(log)
    await ctx.channel.send('{} เพิ่มผล{} จำนวน {}คู่, ตอนนี้คุณ{} จำนวน {}คู่'.format(idP, list[choice-1], str(point), list[choice-1], str(sum)))
    

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
    idP = '<@' + str(player.id) + '>'
    # nameP = str(player.name)
    await ctx.channel.send('น้องบอทขอประมวลผลแปปนึง...')
    sum = cutData(choice, idP, point)
    # print(sum)
    if sum == 999:
      await ctx.channel.send('Balance not enough')
    elif sum == 777:
      await ctx.channel.send('User never have point')
    else:
      log = '{} use method cut {} point from <{}> in {}, Now have {}'.format(nameAdmin, str(point), idP, list[choice-1], sum)
      updateLog(log)
      await ctx.channel.send('{} ลดผล{} จำนวน {}คู่, ตอนนี้คุณ{} จำนวน {}คู่'.format(idP, list[choice-1], str(point), list[choice-1], str(sum)))
  
@client.command()
async def show(ctx):
  role_object = discord.utils.get(ctx.message.guild.roles, name='worldcup⚽')
  await ctx.author.add_roles(role_object)
  
  user_id = str(ctx.author)
  id = '<@' + str(ctx.author.id) + '>'
  embed = discord.Embed(title=f"{'----------<Board>----------'}", description=('คะแนนของ ' + user_id),color=discord.Color.red())
  list = db["list"]
  
  for arr in list:
    connection = sqlite3.connect("myDatabase.db")
    cursor = connection.cursor()
    result  = cursor.execute("SELECT * from {} WHERE disID = '{}' ".format(arr, id)).fetchall();
    check = len(result)
    
    if check > 0:
      score = result[0][1]
      embed.add_field(name=arr, value=f"{str(score)}")
    else:
      embed.add_field(name=arr, value=f"{'0'}")
  await ctx.send(embed=embed)

@client.command()
async def s(ctx, player: discord.Member):
  user_id = str(player)
  id = '<@' + str(player.id) + '>'
  embed = discord.Embed(title=f"{'----------<Board>----------'}", description=('คะแนนของ ' + user_id),color=discord.Color.red())
  list = db["list"]
  
  for arr in list:
    connection = sqlite3.connect("myDatabase.db")
    cursor = connection.cursor()
    result  = cursor.execute("SELECT * from {} WHERE disID = '{}' ".format(arr, id)).fetchall();
    check = len(result)
    
    if check > 0:
      score = result[0][1]
      embed.add_field(name=arr, value=f"{str(score)}")
    else:
      embed.add_field(name=arr, value=f"{'0'}")
  await ctx.send(embed=embed)

@client.command()
async def board(ctx, input:int):
  # list = db["list"]
  # connection = sqlite3.connect("myDatabase.db")
  # cursor = connection.cursor()
  # result  = cursor.execute("SELECT * from {} ORDER BY Score DESC ".format(list[input-1])).fetchall();

  # await ctx.channel.send('น้องบอทขอประมวลผลแปปนึง...')
  # text = '```          Point of {}\n'.format(list[input-1])

  # for arr in result:
  #   text += 'คุณ{} มี {} แต้ม \n'.format(arr[0], arr[1])
  # text += '```'
  # await ctx.send(text)
  
  list = db["list"]
  connection = sqlite3.connect("myDatabase.db")
  cursor = connection.cursor()
  result  = cursor.execute("SELECT * from {} ORDER BY Score DESC ".format(list[input-1])).fetchall();

  await ctx.channel.send('น้องบอทขอประมวลผลแปปนึง...')
  text = '```          Point of {}```\n'.format(list[input-1])

  count = 0
  page = 1
  for arr in result:
    if (count%20) == 0:
      embed = discord.Embed(title=f"{'----------< Board of ' + list[input-1] +', Page'+str(page) +' >----------'}", description=('หน้าแสดงคะแนนทายผลบอลโลกในส่วนของ ทาย' + list[input-1]),color=discord.Color.red())
    
    embed.add_field(name=str(arr[1]), value=f"{str(arr[0])}")
    
    if (count%20) == 19:
      await ctx.send(embed=embed)
      page += 1
    count += 1
    
  if (count%20) != 19:
    await ctx.send(embed=embed)

# @client.command()
# @has_permissions(administrator = True)
# async def b(ctx, input:int):
#   list = db["list"]
#   connection = sqlite3.connect("myDatabase.db")
#   cursor = connection.cursor()
#   result  = cursor.execute("SELECT * from {} ORDER BY Score DESC ".format(list[input-1])).fetchall();

#   await ctx.channel.send('น้องบอทขอประมวลผลแปปนึง...')
#   text = '```          Point of {}```\n'.format(list[input-1])

#   count = 0
#   page = 1
#   for arr in result:
#     if (count%20) == 0:
#       embed = discord.Embed(title=f"{'----------< Board of ' + list[input-1] +', Page'+str(page) +' >----------'}", description=('หน้าแสดงคะแนนทายผลบอลโลกในส่วนของ ทาย' + list[input-1]),color=discord.Color.red())
    
#     embed.add_field(name=str(arr[1]), value=f"{str(arr[0])}")
    
#     if (count%20) == 19:
#       await ctx.send(embed=embed)
#       page += 1
#     count += 1
    
#   if (count%20) != 19:
#     await ctx.send(embed=embed)

       
  
# @client.command()
# @has_permissions(administrator = True)
# async def shutdown(ctx):
#   nameAdmin = str(ctx.author.name)
#   delData()
#   chData()
#   showData()
#   await ctx.channel.send('A nuclear bomb destroyed all the data.')
#   log = 'System Restarting...By {} use shutdown method'.format(nameAdmin)
#   updateLog(log)
  
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
  
  
  