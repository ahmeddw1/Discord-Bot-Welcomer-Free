import discord
from discord.ext import commands
from discord import File
from easy_pil import Editor, load_image_async, Font
import os

# --- 1. LOAD TOKEN FROM TXT FILE ---
try:
    with open("token.txt", "r") as f:
        TOKEN = f.read().strip()
except FileNotFoundError:
    print("❌ ERROR: token.txt not found!")
    TOKEN = None

intents = discord.Intents.default()
intents.members = True 
intents.message_content = True

bot = commands.Bot(command_prefix="!", intents=intents)

@bot.event
async def on_ready():
    # Status: Watching the server
    await bot.change_presence(
        status=discord.Status.dnd,
        activity=discord.Activity(
            type=discord.ActivityType.watching,
            name="the server"
        )
    )
    print(f'✅ {bot.user} is online and running!')

@bot.event
async def on_member_join(member):
    WELCOME_CHANNEL_ID = 1485781231491743885 
    # Get the correct path for the background image
    base_path = os.path.dirname(__file__)
    BG_PATH = os.path.join(base_path, "background.jpg")
    
    channel = member.guild.get_channel(WELCOME_CHANNEL_ID)
    
    try:
        # --- 2. GENERATE WELCOME CARD ---
        background = Editor(BG_PATH).resize((800, 450))
        
        avatar_data = await load_image_async(str(member.display_avatar.url))
        profile = Editor(avatar_data).resize((160, 160)).circle_image()
        
        background.paste(profile, (320, 80))
        
        font_big = Font.poppins(size=50, variant="bold")
        font_small = Font.poppins(size=30, variant="regular")
        
        background.text((400, 270), "WELCOME", color="white", font=font_big, align="center")
        background.text((400, 325), member.name, color="white", font=font_small, align="center")
        
        file = File(fp=background.image_bytes, filename="welcome.png")

        # --- 3. SEND TO CHANNEL ---
        if channel:
            await channel.send(f"Welcome to the server, {member.mention}! ✨", file=file)

        # --- 4. SEND RULES IN DM ---
        rules_embed = discord.Embed(
            title=f"Welcome to {member.guild.name}!",
            description="Please read our rules carefully:",
            color=discord.Color.gold()
        )
        rules_embed.add_field(name="📜 Rule #1", value="Be respectful to all members.", inline=False)
        rules_embed.add_field(name="🚫 Rule #2", value="No spamming or EMOJI SPAM.", inline=False)
        rules_embed.add_field(name="🔗 Rule #3", value="No unauthorized invite links.", inline=False)
        rules_embed.set_footer(text="By chatting, you agree to these rules.")
        
        try:
            await member.send(embed=rules_embed)
        except discord.Forbidden:
            print(f"Skipped DM for {member.name} (DMs closed).")

    except Exception as e:
        print(f"Error: {e}")

# Start the bot
if TOKEN:
    bot.run(TOKEN)