import sqlite3
from replit import db

connection = sqlite3.connect("myDatabase.db")
cursor = connection.cursor()
nametable1 = "correct"
nametable2 = "wrong"
# cursor.execute("CREATE TABLE {} (disID TEXT, Score INTEGER)".format(nametable1))
# cursor.execute("CREATE TABLE {} (disID TEXT, Score INTEGER)".format(nametable2)) 

# value1 = db["ทายผิด_id"]
# value2 = db["ทายผิด_point"]
# for arr in range(len(value1)):
#   cursor.execute("INSERT INTO wrong VALUES ('{}',{})".format(str(value1[arr]), int(value2[arr])))

rows = cursor.execute("SELECT * FROM correct").fetchall()
print(rows)
rows1 = cursor.execute("SELECT * FROM wrong").fetchall()
print(rows1)


connection.commit()
connection.close()


  

# import os
# import discord
# import re
# from datetime import datetime
# from os import system
# from time import sleep
# from keepAlive import keep_alive
# from discord.ext import commands
# from replit import db
# from discord.ext.commands import has_permissions, MissingPermissions
# from discord.utils import get
# from discord import Member, Role

# my_secret = os.environ['Token']
# # my_secret = os.environ['TokenAdmin']

# client = commands.Bot(command_prefix='+')

# def updateLog(text:str):
#   now = datetime.now()
#   date_time = now.strftime("%m/%d/%Y, %H:%M:%S")
#   f = open("Log.txt", "a")
#   f.write(date_time + " | " + text + "\n")
#   f.close()

# def chData():
#   keys = db.keys()
#   tmp = False
#   for row in keys:
#     if row == "list":
#       tmp = True
      
#   if tmp == False:
#     db["list"] = []

# def showData():
#   keys = db.keys()
#   tmp = 'System starting \nShow All Data \n'
#   for row in keys:
#     tmp += row + '\n'
#   print(tmp)

# def delData():
#   keys = db.keys()
#   for row in keys:
#     del db[row]

# #function fo user
# def loopID():
#   valueArr = []
#   tmp = db["idPlayer"]
#   for arr in range(len(tmp)):
#     valueArr.append(tmp[arr])

# def addData(choice:int, id:str, point:int):
#   list = db["list"]
#   tmp = False
#   tmpid = list[choice-1] + '_id'
#   # tmpname = list[choice-1] + '_name'
#   tmppoint = list[choice-1] + '_point'
#   dataID = db[tmpid]
#   # dataName = db[tmpname]
#   dataPoint = db[tmppoint]
#   # print(dataID)
#   # print(dataName)
#   # print(dataPoint)
  
#   sum = 0
#   index = -999
#   if id in dataID:
#     index = dataID.index(id)
#     p = dataPoint[index]
#     sum = (p + point)
#     tmp = True
#   # print(tmp)  
    
#   if tmp == True:
#     # dataName[index] = name
#     dataPoint[index] = sum
#     # print(dataID)
#     # print(dataName)
#     # print(dataPoint)
#     db[tmpid] = dataID
#     # db[tmpname] = dataName
#     db[tmppoint] = dataPoint
#   else:
#     dataID.append(id)
#     # dataName.append(name)
#     dataPoint.append(point)
#     sum = point
#     # print(dataID)
#     # print(dataName)
#     # print(dataPoint)
#     db[tmpid] = dataID
#     # db[tmpname] = dataName
#     db[tmppoint] = dataPoint

#   return sum

# def cutData(choice:int, id:str, point:int):
#   list = db["list"]
#   tmp = False
#   tmpid = list[choice-1] + '_id'
#   # tmpname = list[choice-1] + '_name'
#   tmppoint = list[choice-1] + '_point'
#   dataID = db[tmpid]
#   # dataName = db[tmpname]
#   dataPoint = db[tmppoint]

#   sum = 0
#   index = -999
#   if id in dataID:
#     index = dataID.index(id)
#     p = dataPoint[index]
#     sum = (p - point)
#     tmp = True
#   else:
#     return 777
  
#   if sum < 0:
#     return 999
#   if tmp == True:
#     # dataName[index] = name
#     dataPoint[index] = sum
#     # print(dataID)
#     # print(dataName)
#     # print(dataPoint)
#     db[tmpid] = dataID
#     # db[tmpname] = dataName
#     db[tmppoint] = dataPoint
#   # print(sum)
#   return sum

# def idDisSplit(id:str):
#   x = id.split("<")
#   y = x[1].split("@")
#   z = y[1].split(">")

#   return z[0]


# @client.event
# async def on_ready():
#     chData()
#     showData()
#     updateLog('System Starting...')
#     print(f'Successfully logged in as {client.user}')
    

# @client.command()
# async def info(ctx):
#   async for message in ctx.channel.history(limit=1):
#     await message.delete()
#   await ctx.send("❈────────•✦•กระดานคำสั่ง•✦•────────❈\n\n"
#                   "─────────────User─────────────\n"
#                   "+role   → รับโรล ⚽WolrdCup \n"
#                   "+show   → เช็คผลตัวเอง\n"
#                   "+s <@name>   → เช็คผลคนอื่น\n"
#                   "❈──────────•✦•❅•✦•──────────❈\n")

# @client.command()
# @has_permissions(administrator = True)
# async def make(ctx, text: str):
#   async for message in ctx.channel.history(limit=1):
#     await message.delete()
#   nameAdmin = str(ctx.author.name)
#   list = db["list"]
#   tmp = False
#   for arr in list:
#     if arr == text:
#       tmp = True
#       break
#   if tmp == True:
#     await ctx.channel.send(text + ' have in list already')
#     log = '{} use method add {} to list, But it\'s in list already'.format(nameAdmin, text)
#     updateLog(log)
#   else:
#     list.append(text)
#     db["list"] = list
    
#     log = '{} use method add {} to list, Add to list'.format(nameAdmin, text)
#     updateLog(log)
    
#     id = text + '_id'
#     # name = text + '_name'
#     point = text + '_point'
#     db[id] = []
#     # db[name] = []
#     db[point] = []
#     await ctx.channel.send('»——————⋆◦★◦⋆——————«\n                 ' + text + ' add to list' + '\n»——————⋆◦★◦⋆——————«')
    
#     log = 'Create db of {}, it has {}, {} and {}'.format(text, id, point)
#     updateLog(log)

# @client.command()
# @has_permissions(administrator = True)
# async def delist(ctx, text: str):
#   nameAdmin = str(ctx.author.name)
#   list = db["list"]
#   if text in list:
#     id = text + '_id'
#     # name = text + '_name'
#     point = text + '_point'
#     del db[id]
#     # del db[name]
#     del db[point]
#     list.remove(text)
#     await ctx.channel.send('List ' + text + ' was delete')
#     log = '{} use method delist for Delete {} out of list'.format(nameAdmin, text)
#     updateLog(log)
#   else:
#     await ctx.channel.send('Not Found')
  
# @client.command()
# async def list(ctx):
#   async for message in ctx.channel.history(limit=1):
#     await message.delete()
#   nameAdmin = str(ctx.author.name)
#   list = db["list"]
#   num = 1
#   output = '----------<In List have >----------\n'
#   for arr in list:
#     output += str(num) + '  is ' + arr + '\n'
#     num += 1
#   await ctx.channel.send(output)
#   log = '{} use method list'.format(nameAdmin)
#   updateLog(log)
  



# @client.command(pass_context=True)
# async def role(ctx):
#   role_object = discord.utils.get(ctx.message.guild.roles, name='worldcup⚽')
#   await ctx.author.add_roles(role_object)
#   await ctx.channel.send('<@'+str(ctx.author.id) + '>ได้โรล '+str(role_object)+' เรียบร้อย')

# @client.command()
# async def check(ctx, iddis: str):
#   realid = idDisSplit(iddis)
#   print(realid)
#   username = client.get_user(int(realid))
#   await ctx.channel.send(username)
  
# @client.command()
# @has_permissions(administrator = True)
# async def wc(ctx, choice: int, *args):
#   point = 1
#   nameAdmin = str(ctx.author.name)
#   list = db["list"]
#   if choice <= 0 or choice > len(list) :
#     await ctx.channel.send('Number of list is wrong')
#   elif point < 1:
#     await ctx.channel.send('Number of point is wrong')
#   else:
#     await ctx.channel.send('น้องบอทขอประมวลผลแปปนึง...')
#     for arr in args:
#       # print(arr)
#       idP = str(arr)
#       # nameP = str(player.name)
#       sum = addData(choice, idP, point)
#       log = '{} use method add {} point to <{}> in {}'.format(nameAdmin, str(point), idP, list[choice-1])
#       updateLog(log)
#       # realid = idDisSplit(idP)
#       # username = ctx.get_user(int(realid))
#       # await ctx.channel.send('{} เพิ่มผล{} จำนวน {}คู่, ตอนนี้คุณ{} จำนวน {}คู่'.format(username, list[choice-1], str(point), list[choice-1], str(sum)))
#     await ctx.channel.send('อัพเดตผล'+list[choice-1]+'เรียบร้อยแล้ว')

# def addR8(choice: int, id:str, answer: str):
#   list = db["list"]
#   tmp = False
#   tmpid = list[choice-1] + '_id'
#   # tmpname = list[choice-1] + '_name'
#   tmppoint = list[choice-1] + '_point'
#   dataID = db[tmpid]
#   # dataName = db[tmpname]
#   dataPoint = db[tmppoint]
#   # print(dataID)
#   # print(dataName)
#   # print(dataPoint)
  
#   sum = 0
#   index = -999
#   if id in dataID:
#     index = dataID.index(id)
#     p = dataPoint[index]
#     sum = (p + point)
#     tmp = True
#   # print(tmp)  
    
#   if tmp == True:
#     # dataName[index] = name
#     dataPoint[index] = sum
#     # print(dataID)
#     # print(dataName)
#     # print(dataPoint)
#     db[tmpid] = dataID
#     # db[tmpname] = dataName
#     db[tmppoint] = dataPoint
#   else:
#     dataID.append(id)
#     # dataName.append(name)
#     dataPoint.append(point)
#     sum = point
#     # print(dataID)
#     # print(dataName)
#     # print(dataPoint)
#     db[tmpid] = dataID
#     # db[tmpname] = dataName
#     db[tmppoint] = dataPoint

#   return sum

# @client.command()
# @has_permissions(administrator = True)
# async def summit(ctx, choice: int, *args):
#   nameAdmin = str(ctx.author.name)
#   list = db["list"]
#   if choice <= 0 or choice > len(list) :
#     await ctx.channel.send('Number of list is wrong')
#   elif point < 1:
#     await ctx.channel.send('Number of point is wrong')
#   else:
#     await ctx.channel.send('น้องบอทขอประมวลผลแปปนึง...')
#     for arr in args:
#       # print(arr)
#       idP = str(arr)
#       # nameP = str(player.name)
#       sum = addData(choice, idP, point)
#       log = '{} use method add {} point to <{}> in {}'.format(nameAdmin, str(point), idP, list[choice-1])
#       updateLog(log)
#       # realid = idDisSplit(idP)
#       # username = ctx.get_user(int(realid))
#       # await ctx.channel.send('{} เพิ่มผล{} จำนวน {}คู่, ตอนนี้คุณ{} จำนวน {}คู่'.format(username, list[choice-1], str(point), list[choice-1], str(sum)))
#     await ctx.channel.send('อัพเดตผล'+list[choice-1]+'เรียบร้อยแล้ว')

# @client.command()
# @has_permissions(administrator = True)
# async def add(ctx, choice: int, player: discord.Member, point: int):
#   nameAdmin = str(ctx.author.name)
#   list = db["list"]
#   if choice <= 0 or choice > len(list) :
#     await ctx.channel.send('Number of list is wrong')
#   elif point < 1:
#     await ctx.channel.send('Number of point is wrong')
#   else:
#     idP = '<@' + str(player.id) + '>'
#     # nameP = str(player.name)
#     await ctx.channel.send('น้องบอทขอประมวลผลแปปนึง...')
#     sum = addData(choice, idP, point)
#     log = '{} use method add {} point to <{}> in {}'.format(nameAdmin, str(point), idP, list[choice-1])
#     updateLog(log)
#     # username = client.get_user(int(player.id))
#     # await ctx.channel.send('{} เพิ่มผล{} จำนวน {}คู่, ตอนนี้คุณ{} จำนวน {}คู่'.format(username, list[choice-1], str(point), list[choice-1], str(sum)))

# @client.command()
# @has_permissions(administrator = True)
# async def cut(ctx, choice: int, player: discord.Member, point: int):
#   nameAdmin = str(ctx.author.name)
#   list = db["list"]
#   if choice <= 0 or choice > len(list) :
#     await ctx.channel.send('Number of list is wrong')
#   elif point < 1:
#     await ctx.channel.send('Number of point is wrong')
#   else:
#     idP = '<@' + str(player.id) + '>'
#     # nameP = str(player.name)
#     await ctx.channel.send('น้องบอทขอประมวลผลแปปนึง...')
#     sum = cutData(choice, idP, point)
#     # print(sum)
#     if sum == 999:
#       await ctx.channel.send('Balance not enough')
#     elif sum == 777:
#       await ctx.channel.send('User never have point')
#     else:
#       log = '{} use method cut {} point from <{}> in {}'.format(nameAdmin, str(point), idP, list[choice-1])
#       updateLog(log)
#       # username = client.get_user(int(player.id))
#       # await ctx.channel.send('{} ลดผล{} จำนวน {}คู่, ตอนนี้คุณ{} จำนวน {}คู่'.format(username, list[choice-1], str(point), list[choice-1], str(sum)))
  
# @client.command()
# async def show(ctx):
#   role_object = discord.utils.get(ctx.message.guild.roles, name='worldcup⚽')
#   await ctx.author.add_roles(role_object)
  
#   user_id = str(ctx.author)
#   id = '<@' + str(ctx.author.id) + '>'
#   embed = discord.Embed(title=f"{'----------<Board>----------'}", description=('คะแนนของ ' + user_id),color=discord.Color.red())
#   list = db["list"]
#   for arr in list:
#     tmpid = arr + '_id'
#     tmppoint = arr + '_point'
    
#     dataID = db[tmpid]
#     # print(str(ctx))
#     # print(dataID)
#     dataPoint = db[tmppoint]

#     index = 0
    
#     if id in dataID:
#       index = dataID.index(id)
#       embed.add_field(name=arr, value=f"{str(dataPoint[index])}")
#     else:
#       embed.add_field(name=arr, value=f"{'0'}")
#   await ctx.send(embed=embed)

# @client.command()
# async def s(ctx, player: discord.Member):
#   user_id = str(player)
#   id = '<@' + str(player.id) + '>'
#   embed = discord.Embed(title=f"{'----------<Board>----------'}", description=('คะแนนของ ' + user_id),color=discord.Color.red())
#   list = db["list"]
#   for arr in list:
#     tmpid = arr + '_id'
#     tmppoint = arr + '_point'
    
#     dataID = db[tmpid]
#     dataPoint = db[tmppoint]

#     index = 0
    
#     if id in dataID:
#       index = dataID.index(id)
#       embed.add_field(name=arr, value=f"{str(dataPoint[index])}")
#     else:
#       embed.add_field(name=arr, value=f"{'0'}")
#   await ctx.send(embed=embed)

# @client.command()
# async def board(ctx, input:int):
#   list = db["list"]
#   i = 0
#   tmp = ''
#   for arr in list:
#     if i == (input-1):
#       tmp = arr
#       # print(tmp)
#       break
#     i += 1

#   if tmp == '':
#     await ctx.send('Number of list is wrong')
#   else:
#     await ctx.send('Found it')
#     id = db[tmp + "_id"]
#     point = db[tmp + "_point"]

#     text = '```          Point of {}\n'.format(tmp)
#     for arr in range(len(id)):
#       text += 'คุณ{} มี {} แต้ม \n'.format(id[arr], point[arr])
#     text += '```'
#     await ctx.send(text)
    
# # @client.command()
# # @has_permissions(administrator = True)
# # async def shutdown(ctx):
# #   nameAdmin = str(ctx.author.name)
# #   delData()
# #   chData()
# #   showData()
# #   await ctx.channel.send('A nuclear bomb destroyed all the data.')
# #   log = 'System Restarting...By {} use shutdown method'.format(nameAdmin)
# #   updateLog(log)
  
# @add.error
# async def add_error(ctx, error):
#   if isinstance(error, MissingPermissions):
#     text = "Sorry {}, you do not have permissions to do that!".format(ctx.message.author)
#     await ctx.send(text)
# @cut.error
# async def cut_error(ctx, error):
#   if isinstance(error, MissingPermissions):
#     text = "Sorry {}, you do not have permissions to do that!".format(ctx.message.author)
#     await ctx.send(text)
# @make.error
# async def make_error(ctx, error):
#   if isinstance(error, MissingPermissions):
#     text = "Sorry {}, you do not have permissions to do that!".format(ctx.message.author)
#     await ctx.send(text)

# @client.command(pass_context = True)
# @has_permissions(administrator = True)
# async def whoami(ctx):
#   await ctx.send('คุณเป็น administrator')

# @whoami.error
# async def whoami_error(ctx, error):
#   if isinstance(error, MissingPermissions):
#     text = "Sorry {}, you do not have permissions to do that!".format(ctx.message.author)
#     await ctx.send(text)



# @client.command()
# async def restart(ctx): 
#   await ctx.channel.send('Test Restart')
#   print("\n\nRESTARTING NOW\n\n\n")
#   await ctx.channel.send('kill process')
#   print('kill')
#   system('kill 1')
#   await ctx.channel.send('sleep')
#   print('sleep')
#   sleep(7)
#   await ctx.channel.send('restart')
#   print('restart')
#   system("python main.py")

# keep_alive()
# try:
#     client.run(my_secret)
# except discord.errors.HTTPException:
#   print("\n\n\nBLOCKED BY RATE LIMITS\nRESTARTING NOW\n\n\n")
#   system("python restarter.py")
  
  
  