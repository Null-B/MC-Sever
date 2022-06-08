import disnake, requests
from disnake.ext import commands

class Server_boot(commands.Cog):
            
        def __init__(self, client):
            self.client = client
        
        @commands.command(pass_context = True , aliases=['start', 'serverst', 'serverstart'])
        async def server_start(self, ctx):
            await ctx.send('Server is starting', delete_after=2)
            await ctx.send('https://cdn.discordapp.com/emojis/715599179744804965.gif?size=64', delete_after=1)
            prams ={'Authorization':'96fe2546-ab98-4488-ac1f-23c6a9ad0636', 'x-session-id':'828f005f-d5c6-4a50-b4e8-d88b30a3addf'}
            r = requests.post('https://api.minehut.com/server/Theleaksmp/start_service', {'Authorization':'96fe2546-ab98-4488-ac1f-23c6a9ad0636', 'x-session-id':'828f005f-d5c6-4a50-b4e8-d88b30a3addf'})
            await ctx.send(r)

        # got to discord chat to check how to refresh the sesion id 
        @commands.command()
        async def server_shutdown(self, ctx):
            await ctx.send('Server is shutting down')
            await ctx.send('https://cdn.discordapp.com/emojis/715599179744804965.gif?size=64', delete_after=1)
            prams ={'Authorization':'96fe2546-ab98-4488-ac1f-23c6a9ad0636', 'x-session-id':'828f005f-d5c6-4a50-b4e8-d88b30a3addf'}
            r = requests.post('https://api.minehut.com/server/Theleaksmp/destroy_service', {'Authorization':'96fe2546-ab98-4488-ac1f-23c6a9ad0636', 'x-session-id':'828f005f-d5c6-4a50-b4e8-d88b30a3addf'})
            await ctx.send(r)


def setup(client):
   client.add_cog(Server_boot(client))