import discord
from redbot.core import commands

class Attack(commands.Cog):
	"""attack"""
	def __init__(self, bot):
		self.bot = bot
	
	@commands.command()
	async def attack(self, ctx, id:int):
		"""Add a dagger to a message"""
		m = await ctx.message.channel.get_message(id)
		await m.add_reaction('\N{DAGGER KNIFE}')