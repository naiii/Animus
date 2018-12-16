import configparser


Config = configparser.ConfigParser()
Config.read('config.ini')
Config.sections()


def config_section_map(section):
    config_dict = {}
    options = Config.options(section)
    for option in options:
        try:
            config_dict[option] = Config.get(section, option)
            if config_dict[option] == -1:
                print('Skip: %s' % option)
        except Exception as err:
            print('Exception on %s' % option)
            print(str(err))
            config_dict[option] = None

    return config_dict


# BotSetup

token = config_section_map('BotSetup')['token']
command_prefix = config_section_map('BotSetup')['command_prefix']
description = config_section_map('BotSetup')['description']


# Century's Den
server_id = 234755524145446912

test_role_id = 414436453897207838
