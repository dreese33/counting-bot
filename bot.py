from curses.ascii import isdigit
import discord
import os

class Client(discord.Client):
    async def on_message(self, message):
        if message.author == self.user:
            return

        if message.content.isnumeric():
            curr_number = int(message.content)
            for i in range(curr_number + 1, curr_number + 51):
                await message.channel.send(i)

    async def on_ready(self):
        print(f'{client.user} has connected to Discord!')


token = os.environ.get('BOT_TOKEN')
client = Client()
client.run(token)
