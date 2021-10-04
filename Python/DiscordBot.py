# Code Written by Milton (@jmrchelani)
# Illustrates the basic construction of a discord bot with Discord.py lib
# Also provided with a basic example of command using bot

from discord.ext import commands, tasks
from discord.ext.commands.context import Context
from discord.reaction import Reaction

# Prefix for the bot commands
PREFIX = '!'

# the token of discord bot (used to login / run)
TOKEN = 'DC_BOT_TOKEN'

# the particular channel id where we want to allow some particular thing
CODE_ID = 'CHANNEL_ID_OF_PARTICULAR_CHANNEL_IN_SERVER'

# bot object
bot = commands.Bot(command_prefix = PREFIX)

#Bot Command
@bot.command()

# this works like !code
async def code(ctx: Context):                    
    # if the channel in which the command is executed is not the same as the channel with code CODE_ID, return an error
    if ctx.channel is not bot.get_channel(CODE_ID):
        return await ctx.send('`Error:` Invalid channel.')

    # A code to respond with
    code = 'Ezpz'

    # Adding the Like Emoji on command message
    emoji = '\N{THUMBS UP SIGN}'
    await ctx.message.add_reaction(emoji)
    
    # reply with a code
    return await ctx.author.send(f'`Success:` The code is: `{code}`.')

# bot events
@bot.event
# Whenever the bot is successfully connected to the discord server and is logged in, its auto called
async def on_ready():
    print('Logged in as')
    print(bot.user.name)
    print(bot.user.id)
    print('------')
    
# Run the bot
bot.run(TOKEN)
