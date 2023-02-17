import discord
import requests
import asyncio

client = discord.Client()

@client.event
async def on_ready():
    print(f'Logged in as {client.user.name} (ID: {client.user.id})')
    # Set a task to send a random cat picture every 24 hours
    await asyncio.create_task(send_cat_picture())

async def send_cat_picture():
    channel = client.get_channel(CHANNEL_ID) # Replace CHANNEL_ID with the actual ID of the channel you want to send the pictures to
    while True:
        # Get a random cat picture from the Cat API
        response = requests.get('https://api.thecatapi.com/v1/images/search')
        if response.status_code == 200:
            # Send the picture to the channel
            await channel.send(response.json()[0]['url'])
        # Wait for 24 hours before sending the next picture
        await asyncio.sleep(24 * 60)

client.run('YOUR_DISCORD_BOT_TOKEN') # Replace YOUR_DISCORD_BOT_TOKEN with the actual token of your Discord bot
