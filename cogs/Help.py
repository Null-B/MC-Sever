import disnake
from disnake.ext import commands

class Help(commands.Cog):

   def __init__(self, client):
       self.client = client

   @commands.command()
   async def help(self, ctx, *, command=None):
       if command:
           cmd = self.client.get_command(command)
           if cmd:
               embed = cmd.embed()
               await ctx.send(embed=embed)
           else:
               await ctx.send(f'Command `{command}` not found!')
       else:
           embed = disnake.Embed(title='Help', description='List of commands')
           embed.set_author(name=self.client.user.name, icon_url=self.client.user.avatar_url)
           await ctx.send(embed=embed)

def setup(client):
   client.add_cog(Help(client))