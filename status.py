import discord
from discord.ext import tasks
import time

token = ''

client = discord.Client()

@tasks.loop(seconds=5)
async def lie_status():
    await client.change_presence(
        status=discord.Status.dnd,
        afk=False,
        activity=discord.Activity(
            type=discord.ActivityType.streaming,
            name='L ',
            url='https://twitch.tv/LIE'
        )
    )
    time.sleep(2)
    await client.change_presence(
        status=discord.Status.dnd,
        afk=False,
        activity=discord.Activity(
            type=discord.ActivityType.streaming,
            name='L I ',
            url='https://twitch.tv/LIE'
        )
    )
    time.sleep(2)
    await client.change_presence(
        status=discord.Status.dnd,
        afk=False,
        activity=discord.Activity(
            type=discord.ActivityType.streaming,
            name='L I E',
            url='https://twitch.tv/LIE'
        )
    )
    await client.change_presence(
        status=discord.Status.dnd,
        afk=False,
        activity=discord.Activity(
            type=discord.ActivityType.streaming,
            name='L I ',
            url='https://twitch.tv/LIE'
        )
    )
    time.sleep(2)
    await client.change_presence(
        status=discord.Status.dnd,
        afk=False,
        activity=discord.Activity(
            type=discord.ActivityType.streaming,
            name='L ',
            url='https://twitch.tv/LIE'
        )
    )
    time.sleep(2)

@client.event
async def on_connect():
    lie_status.start()
    print("Connected -> {}#{}".format(client.user.name, client.user.discriminator))

if __name__ == '__main__':
    try:
        client.run(token, bot=False, reconnect=True)
    except discord.errors.HTTPException:
        print("Error -> Improper Token Has Been Passed")
