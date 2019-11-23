import discord
from random import randrange
class MyClient(discord.Client):
    scammers = ["sk", "scam", "mcdonalds", "mcds", "pc", "miguk", "dominos",
                "tfmun", "milestone", "scene", "montanas", "movie","discount",
                "free", "cheap", "doksurri", "doksuri"]
    async def on_ready(self):
        print('Logged on as {0}!'.format(self.user))

    async def on_message(self, message):
        print('Message from {0.author}: {0.content}'.format(message))
        channel = message.channel
        print(message.author)
        if message.author != self.user:
            if "apg" in message.content.lower():
                await channel.send('apg')
            for scam in self.scammers:
                if scam in message.content.lower():
                    await channel.send('I HATE SCAMMERS')
                    break
            if "nielan" in message.content.lower():
                await channel.send("no u adny")
            if "aya" in message.content.lower():
                await channel.send("AYAYA")
            if message.mention_everyone = true:
                count = 0
                
                while (count < randrange(100)):
                    count = count + 1


                await channel.send("REEEEEEEEEEEEEEEEE")

client = MyClient()
client.run(process.env.BOT_TOKEN)
