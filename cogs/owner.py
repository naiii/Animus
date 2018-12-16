from discord.ext import commands
from utility import decorators as perms
from utility import botutility


class OwnerCog:

    def __init__(self, bot):
        self.bot = bot

    @commands.group(name="channel")
    @commands.is_owner()
    @perms.is_channel_leader()
    async def channel_mgmt(self, ctx):
        if ctx.invoked_subcommand is None:
            await ctx.send('Invalid sub-command.')

    @channel_mgmt.command(name="name")
    async def channel_mgmt_name(self, ctx, name: str):
        voice_channel = ctx.author.voice.channel
        await voice_channel.edit(name=name)
        await ctx.send('Channel name successfully changed.')

    @channel_mgmt.command(name="limit")
    async def channel_mgmt_limit(self, ctx, limit: int):
        voice_channel = ctx.author.voice.channel
        await voice_channel.edit(user_limit=limit)
        await ctx.send('Channel user limit successfully changed.')

    @channel_mgmt.command(name="category")
    async def channel_mgmt_category(self, ctx, category: str):
        if category == 'animus1':
            category = botutility.get_category_by_id(self.bot, 523842356366016512)
        elif category == 'animus2':
            category = botutility.get_category_by_id(self.bot, 523860544390692864)

        voice_channel = ctx.author.voice.channel
        await voice_channel.edit(category=category)
        await ctx.send('Channel category successfully changed.')


def setup(bot):
    bot.add_cog(OwnerCog(bot))
