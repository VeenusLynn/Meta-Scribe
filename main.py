import discord
from discord.ext import commands
import dotenv
import os

from utils import *

dotenv.load_dotenv()

# Get API key from .env file
API_KEY = os.getenv("API_KEY")

# Create an instance of the bot
intents = discord.Intents.all()
bot = commands.Bot(command_prefix='/', intents=intents)
bot.remove_command('help')


@bot.event
async def on_ready():
    print(f'Bot is ready. Logged in as {bot.user.name} ({bot.user.id})')


@bot.command(
    name="championrotation",
    description="See the current champion rotation"
)
async def champion_rotation(ctx):
    await ctx.send(print_champion_rotation())


@bot.command(
    name="championinfo",
    description="Get information about a specific champion"
)
async def champion_info(ctx, champion_name: str):
    champ = print_champion_info_by_name(champion_name)
    info = f"""
**Name**: {champ['name']}
**Title**: {champ['title']}
**Lore**: {champ['lore']}
**Difficulty**: {champ['info']['difficulty']}
**Type**: {champ['tags']}
**Ally Tips**: {champ['allytips']}
**Enemy Tips**: {champ['enemytips']}
    """

    abilities = f"""
**Passive**: {champ['passive']['name']}
**Passive Description**: {champ['passive']['description']}
**Q**: {champ['spells'][0]['name']}
**Q Description**: {champ['spells'][0]['description']}
**W**: {champ['spells'][1]['name']}
**W Description**: {champ['spells'][1]['description']}
**E**: {champ['spells'][2]['name']}
**E Description**: {champ['spells'][2]['description']}
**R**: {champ['spells'][3]['name']}
**R Description**: {champ['spells'][3]['description']}
    """
    await ctx.send(info)
    await ctx.send(abilities)


@bot.command(
    name="iteminfo",
    description="Get information about a specific item"
)
async def item_info(ctx, item_name: str):
    await ctx.send(print_item_info_by_name(item_name))


@bot.command(
    name="runeinfo",
    description="Get information about a specific rune"
)
async def rune_info(ctx, rune_name: str):
    await ctx.send(print_rune_info_by_name(rune_name))


@bot.command(
    name="summonerspellinfo",
    description="Get information about a specific summoner spell"
)
async def summoner_spell_info(ctx, spell_name: str):
    await ctx.send(print_summoner_spell_info_by_name(spell_name))


@bot.command(
    name="championsplashart",
    description="Get a champion's splash art"
)
async def champion_splash_art(ctx, champion_name: str):
    await ctx.send(print_champion_splash_art(champion_name))


@bot.command(
    name="championskinsplashart",
    description="Get a champion's skin splash art"
)
async def champion_skin_splash_art(ctx, champion_name: str, skin_number: int):
    await ctx.send(print_champion_skin_splash_art(champion_name, skin_number))


@bot.command(
    name="championstats",
    description="Get a champion's current stats"
)
async def champion_stats(ctx, champion_name: str):
    await ctx.send(f"{print_champion_tier(champion_name)}\n"
                   f"{print_champion_winrate(champion_name)}\n"
                   f"{print_champion_pickrate(champion_name)}\n"
                   f"{print_champion_banrate(champion_name)}")


@bot.command(
    name="championcounters",
    description="Get a champion's counters"
)
async def champion_counters(ctx, champion_name: str):
    await ctx.send(print_champion_counters(champion_name))


@bot.command(
    name="championrecommendedrunes",
    description="Get a champion's recommended runes"
)
async def champion_recommended_runes(ctx, champion_name: str):
    await ctx.send(print_champion_recommended_runes(champion_name))


@bot.command(
    name="championrecommendedspells",
    description="Get a champion's recommended spells"
)
async def champion_recommended_spells(ctx, champion_name: str):
    await ctx.send(print_champion_recommended_spells(champion_name))


@bot.command(
    name="championrecommendedbuild",
    description="Get a champion's recommended build"
)
async def champion_recommended_build(ctx, champion_name: str):
    await ctx.send(print_champion_recommended_build(champion_name))


@bot.command(
    name="championskillorder",
    description="Get a champion's recommended skill order"
)
async def champion_skill_order(ctx, champion_name: str):
    await ctx.send(print_champion_skill_order(champion_name))


@bot.command(
    name="help",
    description="Show available commands"
)
async def help_command(ctx):
    help_text = """
    Available commands:
    - /championrotation: See current champion rotation
    - /championinfo <champion_name>: Get information about a specific champion
    - /iteminfo <item_name>: Get information about a specific item
    - /runeinfo <rune_name>: Get information about a specific rune
    - /summonerspellinfo <spell_name>: Get information about a specific summoner spell
    - /championsplashart <champion_name>: Get a champion's splash art
    - /championskinsplashart <champion_name> <skin_number>: Get a champion's skin splash art
    - /championstats <champion_name>: Get a champion's current stats
    - /championcounters <champion_name>: Get a champion's counters
    - /championrecommendedrunes <champion_name>: Get a champion's recommended runes
    - /championrecommendedspells <champion_name>: Get a champion's recommended spells
    - /championrecommendedbuild <champion_name>: Get a champion's recommended build
    - /championskillorder <champion_name>: Get a champion's recommended skill order
    """

    await ctx.send(help_text)

if __name__ == '__main__':
    bot.run(os.getenv("DISCORD_TOKEN"))
