import disnake, requests
from disnake.ext import commands
import datetime


class ServerInfo(commands.Cog):
            
        def __init__(self, client):
            self.client = client
    
        @commands.command()
        async def server_info(self, ctx):
            prams ={'Content-Type': 'yes'}
            result = requests.get('https://api.minehut.com/server/Theleaksmp?byName=true', prams)
            if result.status_code == 200:

                r = result.json()
                a= r.get('server')

                name= a.get('name')
                last_online= a.get('last_online') # convert form unix to normal time
                online= a.get('online')
                playerCount= a.get('player_count')

                # ls=(datetime.utcfromtimestamp(last_online))

                embed = disnake.Embed(title=name, description=f'Last Online: {last_online} not yet done bc of unix time', color=0x00ff00)
                embed.add_field(name='playerCount', value=playerCount, inline=True)
                embed.add_field(name='Online', value=online, inline=False)
                await ctx.send(embed=embed)

            else:
                await ctx.send("Server not found")

         


def setup(client):
   client.add_cog(ServerInfo(client))