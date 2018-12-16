# Animus
Animus, a discord bot



## Dependencies:

-  discord.py rewrite: 
    
    ```python3.6 -m pip install -U git+https://github.com/Rapptz/discord.py@rewrite#egg=discord.py[voice]```
    
    
    
## Features
- **Voice Channel Management**:
    First user that joins a voice channel has the ability to manage the voice channel, i.e. change channel name, user 
    limit or category.
    
    ```bash
      !channel name <new name>
      !channel limit <user limit>
      !channel category <category name>
    ```
    
- **Auto opening and closing of voice channel inside of a category**:
    When a user enters an empty channel the next channel in the category is set ot visible and contactable. When the 
    last user leaves the channel, that channel is closed unless is the last in the category.

