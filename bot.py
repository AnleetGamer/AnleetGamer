import discord
from discord.ext import commands, tasks

# Bot setup
intents = discord.Intents.default()
intents.members = True  # Enables member tracking
intents.guilds = True
intents.presences = True

bot = commands.Bot(command_prefix="!", intents=intents)

# Function to update status
@tasks.loop(minutes=5)
async def update_status():
    for guild in bot.guilds:
        member_count = guild.member_count
        await bot.change_presence(activity=discord.Activity(type=discord.ActivityType.watching, name=f"{member_count} Members"))

@bot.event
async def on_ready():
    print(f"Logged in as {bot.user}")
    update_status.start()  # Start updating status

# Ban Command
@bot.command()
@commands.has_permissions(ban_members=True)
async def ban(ctx, member: discord.Member, *, reason="No reason provided"):
    await member.ban(reason=reason)
    await ctx.send(f"{member.name} has been banned! 🚫")

# Timeout (mute) command (duration in seconds)
@bot.command()
@commands.has_permissions(moderate_members=True)
async def timeout(ctx, member: discord.Member, duration: int, *, reason="No reason provided"):
    await member.timeout(duration=duration, reason=reason)
    await ctx.send(f"{member.name} has been timed out for {duration} seconds! ⏳")

bot.run("MTM1NzM2NjA2NDI5MTI1MDM0Nw.Gd2362.N5zl2px93oeD0gmtx3iUPgvO5BvBlsJ9cQ2idcN")  # Replace with your bot token
