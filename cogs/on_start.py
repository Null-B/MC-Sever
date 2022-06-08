import disnake
from disnake.ext import commands,tasks
from itertools import cycle

class on_start(commands.Cog):

    def __init__(self, client):
        self.client = client
        print("ready")
        self.status = cycle(['First status', 'Second status', 'Third status']) #Todo add more statuses

    @tasks.loop(hours=1)
    async def change_status(self):
        await self.client.change_presence(activity=disnake.Game(next(self.status)))
    
    @commands.Cog.listener()
    async def on_ready(self):
        self.change_status.start()


def setup(client):
    client.add_cog(on_start(client))