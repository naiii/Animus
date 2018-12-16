import discord
import animusvariables as animusVars


def get_category_by_name(bot, name) -> discord.CategoryChannel:
    guild = discord.utils.get(bot.guilds, id=int(animusVars.server_id))
    return discord.utils.get(guild.categories, name=name)


def get_category_by_id(bot, id) -> discord.CategoryChannel:
    guild = discord.utils.get(bot.guilds, id=int(animusVars.server_id))
    return discord.utils.get(guild.categories, id=id)


def get_role_by_id(bot, id) -> discord.Role:
    guild = discord.utils.get(bot.guilds, id=int(animusVars.server_id))
    return discord.utils.get(guild.roles, id=id)
