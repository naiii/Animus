from discord.ext import commands
from channelmanagement import managementvariables as channelMgmt


def is_channel_leader():
    async def predicate(ctx):
        return ctx.author.id in channelMgmt.channel_leaders
    return commands.check(predicate)
