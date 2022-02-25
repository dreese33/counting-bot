import discord
import os

class Client(discord.Client):
    async def on_message(self, message):
        print(message.content)
        if message.author == self.user:
            return

        if message.content.startswith('hello'):
            await message.channel.send('Hello World!')

    async def on_ready(self):
        print(f'{client.user} has connected to Discord!')


token = os.environ.get('BOT_TOKEN')
client = Client()
client.run(token)
