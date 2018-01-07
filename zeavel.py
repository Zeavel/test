import discord # импорт библиотеки discord.py
from urllib.request import urlopen 
from urllib.parse import quote

client = discord.Client() # клиент

@client.event 
async def on_ready(): # объявление ивента on_ready: триггерится, когда запущен бот
    print('We have logged in as {0.user}'.format(client)) # инфа о юзере в консоль

@client.event
async def on_message(message): # ивент on_message: триггерится на каждое сообщение
    if message.author == client.user: # если сообщение от клиента - игнорим
        return

    if message.content.startswith('#test'): # если сообщение начинается с "$hello"
        await message.channel.send('Привет! Я теперь на питоне)') # пишем в этот же канал "Hello!"

    if message.content.startswith('inf'): # если сообщение начинается с "$hello"
        await message.channel.send('!z my info') # пишем в этот же канал "Hello!"

    if message.content.startswith('tes'): # если сообщение начинается с "$hello"
        def test(x, y):
              return x + y
        await message.channel.send(test(5, 7)) # пишем в этот же канал "Hello!"
    if message.content.startswith('chel'): 
     
        def SearchUser(SearchTerm):
           url = "http://boomlings.com/database/getGJUsers20.php"
           p = f"gameVersion=20&binaryVersion=29&str={quote(str(SearchTerm), safe='')}&total=0&page=0&secret=Wmfd2893gb7".encode()
           data = urlopen(url, p).read().decode()
           return data
        await message.channel.send(SearchUser(p))     
        

client.run('Mzc2MDI5NjMwMTY1MDI0NzY5.DN416Q.SJ7yUmoGXlk8sahg1W3R7ah403A') 
