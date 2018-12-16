import traceback

import animusvariables as animusVars
from discord import ClientException
from discord.ext import commands

cogs_extensions = ["cogs.owner",
                   "cogs.events"]

bot = commands.Bot(command_prefix=animusVars.command_prefix, description=animusVars.description)

if __name__ == '__main__':
    for extension in cogs_extensions:
        try:
            bot.load_extension(extension)
            print('Successfully loaded extension {0}'.format(extension))
        except (ClientException, ModuleNotFoundError) as err:
            print('Failed to load extension {0}'.format(extension))
            traceback.print_exc()

    bot.run(animusVars.token, bot=True, reconnect=True)
