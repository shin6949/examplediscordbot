import discord
from discord.ext import commands

# External File
import load_json_variable as variable

# Define the prefix. All command can call after prefix.
prefix = "!"
bot = commands.Bot(command_prefix=prefix)


@bot.event
async def on_ready():
    """
    This event runs when load the bot or re-load.

    :return: None
    """

    # Define the activity 'Playing A Game' as 'comment'
    game = discord.Game("comment")
    await bot.change_presence(status=discord.Status.online, activity=game)
    print("READY")


@bot.event
async def on_message(message):
    """
    This event runs when receive message. but It has no restriction of prefix.

    :param message: discord.Message
    :return: None
    """

    # When bot sent message, do nothing.
    if message.author.bot:
        return None

    # Process Commands
    await bot.process_commands(message)


@bot.command(name="test")
async def react_test(ctx):
    """
    This command runs when user call 'test' after prefix.

    :param ctx: discord.context
    :return: None
    """

    # Send a message to channel what user sent
    await ctx.channel.send("testing!")
    return None


# Referencing token in Json file and run the bot.
bot.run(variable.get_token())

