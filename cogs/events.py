from datetime import datetime
from channelmanagement import managementvariables as channelMgmt
from utility import botutility
import animusvariables as animusvars

import discord


class EventCog:

    def __init__(self, bot):
        self.bot = bot

    async def on_ready(self):
        """
        Called when the client is done preparing the data received from Discord. Usually after login is successful and
        the Client.guilds and co. are filled up.

        Warning:
        This function is not guaranteed to be the first event called. Likewise, this function is not guaranteed to only be
        called once. This library implements reconnection logic and thus will end up calling this event whenever a RESUME
        request fails.

        :return:
        """
        date = datetime.utcnow()
        print('Logged in as')
        print(self.bot.user.name)
        print(self.bot.user.id)
        print(date.strftime('%m/%d/%y %H:%M:%S'))
        print('---------')

    async def on_voice_state_update(self, member: discord.Member, before: discord.VoiceState, after: discord.VoiceState):
        """
        Called when a Member changes their VoiceState.

        The following, but not limited to, examples illustrate when this event is called:
            - A member joins a voice room.
            - A member leaves a voice room.
            - A member is muted or deafened by their own accord.
            - A member is muted or deafened by a guild administrator.

        :param member: The Member whose voice states changed.
        :param before: The VoiceState prior to the changes.
        :param after: The VoiceState after to the changes.
        :return:
        """
        # define channel leader
        if after.channel is not None and len(after.channel.members) == 1:
            channelMgmt.channel_leaders[member.id] = after.channel.id

        # channel mgmt -- open or close channel if necessary
        tester_role = botutility.get_role_by_id(self.bot, animusvars.test_role_id)

        # someone entered an empty channel -> new one needs to be opened
        if after.channel is not None and len(after.channel.members) == 1:
            channel = after.channel
            category = channel.category
            channel_index = category.channels.index(channel)
            next_index = channel_index + 1 if channel_index != len(category.channels)-1 else None

            if next_index is not None:
                next_channel = category.channels[next_index]
                await next_channel.set_permissions(tester_role, connect=True, read_messages=True)

        # last user leaves channel -> channel needs to be closed
        if before.channel is not None and len(before.channel.members) == 0:
            channel = before.channel
            category = channel.category
            channel_index = category.channels.index(channel)

            if channel_index != 0:
                await channel.set_permissions(tester_role, connect=False, read_messages=False)


def setup(bot):
    bot.add_cog(EventCog(bot))
