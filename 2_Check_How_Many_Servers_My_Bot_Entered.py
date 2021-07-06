import discord
from discord.ext import commands

# External File
import load_json_variable as variable

bot = commands.Bot()


@bot.event
async def on_ready():
    """
    This event runs when load the bot or re-load.

    :return: None
    """
    game = discord.Game("Comment What You Want")
    await bot.change_presence(status=discord.Status.online, activity=game)
    print("READY")

    # Get Guild List with bots
    guild_list = bot.guilds

    # Print Guild List
    for i in guild_list:
        print(f"Guild ID: {i.id} / Guild Name: {i.name}")

    # End of Session
    await bot.close()

# Referencing token in Json file and run the bot.
bot.run(variable.get_token())

