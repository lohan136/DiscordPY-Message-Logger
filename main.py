import discord
import time
import datetime
import discord.ext.commands as commands

client = discord.Client()

@client.event
async def on_ready():
    print('Logged in as')
    print(client.user.name)
    print(client.user.id)
    print('------')

@client.event
async def on_message(message):
    ts = time.time()
    st = datetime.datetime.fromtimestamp(ts).strftime('%Y-%m-%d %H:%M:%S')
    with open("logs.txt", "a") as text_file:
        print(f"[{st}] [{message.author.id}] {message.author} {message.content}", file=text_file)

# Made By YesYes#5346 Please Don't Steal My Code Or Claim It As Your Own

client.run('changeme')