import discord
from discord.ext import commands
from config import API_TOKEN

bot = commands.Bot(command_prefix="/", intents = discord.Intents.all(), help_command=None)

@bot.event
async def on_ready():
    print(f'Logged in as {bot.user} (ID: {bot.user.id})')
    print('------')
    activity = discord.Activity(name=f'/help', type=discord.ActivityType.watching, details="Watching", state="Discord")
    await bot.change_presence(activity=activity)
    try:
        sync = await bot.tree.sync()
        print(f'Synced {len(sync)} command')
    except Exception as e:
        print(e)

@bot.tree.command(name="badgeclaim")
async def badgeclaim(interaction: discord.Interaction):
    await interaction.response.send_message(f"{interaction.user.mention}, wow, you just got the active developer badge. ",
                                            ephemeral=True)

@bot.command()
async def help(ctx):
    embed = discord.Embed(title="Bot commands", color=0x00ff00)
    embed.add_field(name="/badgeclaim", value="Allows you to get an active Discord developer badge.", inline=False)
    embed.add_field(name=" ",value=" ", inline=False)
    embed.add_field(name="Author of this bot:", value="**Jeyen**", inline=False)
    await ctx.send(embed=embed)

bot.run(API_TOKEN)