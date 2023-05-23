import discord
from discord.ext import commands
import dotenv
import os
from bs4 import BeautifulSoup

from utils import *

dotenv.load_dotenv()

# Get API key from .env file
API_KEY = os.getenv("API_KEY")

# Create an instance of the bot
intents = discord.Intents.all()
bot = commands.Bot(command_prefix='!', intents=intents)
bot.remove_command('help')


@bot.event
async def on_ready():
    print(f'Bot is ready. Logged in as {bot.user.name} ({bot.user.id})')


@bot.command(
    name="championrotation",
    description="See the current champion rotation"
)
async def champion_rotation(ctx):

    try:
        await ctx.send("Please wait while we fetch the champion rotation...")
        champion_rotation = print_champion_rotation()
        message = """
\r**Champion Rotation:**
        """
        if champion_rotation:
            for champion_id in champion_rotation:
                champion_info = get_champion_info_by_id(champion_id)
                if champion_info:
                    message += f"\r**Champion ID**: {champion_id}"
                    message += f"\r**Name**: {champion_info['name']}"
                    message += f"\r**Title**: {champion_info['title']}"

        await ctx.send(message)
    except:
        await ctx.send("Failed to fetch champion rotation.")


@bot.command(
    name="championinfo",
    description="Get information about a specific champion"
)
async def champion_info(ctx, champion_name: str):

    try:
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
    
    except:
        await ctx.send("Champion not found.")


@bot.command(
    name="iteminfo",
    description="Get information about a specific item"
)
async def item_info(ctx, item_name: str):

    try:
        item = print_item_info_by_name(item_name)
        soup = BeautifulSoup(item["description"], "html.parser")
        for br in soup.find_all("br"):
            br.replace_with("\n")
        
        info = f"""
**Item name**: {item['name']}
**Item stats**:\n{soup.get_text()}
**Item cost**: {item['gold']['total']} Gold
        """

        await ctx.send(info)
    
    except:
        await ctx.send("Item not found.")


@bot.command(
    name="runeinfo",
    description="Get information about a specific rune"
)
async def rune_info(ctx, rune_name: str):

    try:
        rune = print_rune_info_by_name(rune_name)
        soup = BeautifulSoup(rune["longDesc"], "html.parser")
        for br in soup.find_all("br"):
            br.replace_with("\n")
        info = f"""
**Rune name**: {rune['name']}
**Rune description**:\n{soup.get_text()}
        """
        await ctx.send(info)

    except:
        await ctx.send("Rune not found.")


@bot.command(
    name="summonerspellinfo",
    description="Get information about a specific summoner spell"
)
async def summoner_spell_info(ctx, spell_name: str):

    try:
        spell = print_summoner_spell_info_by_name(spell_name)

        info = f"""
**Spell name**: {spell['name']}
**Spell description**: {spell['description']}
**Cooldown**: {spell['cooldownBurn']} seconds
**Summoner level required**: {spell['summonerLevel']}
        """
        await ctx.send(info)

    except:
        await ctx.send("Summoner spell not found.")


@bot.command(
    name="championsplashart",
    description="Get a champion's splash art"
)
async def champion_splash_art(ctx, champion_name: str):

    try:
        splash_art_url = print_champion_splash_art(champion_name)
        # load image from url and send it to the channel
        await ctx.send(splash_art_url)
    except:
        await ctx.send("Champion not found.")

@bot.command(
    name="championskinsplashart",
    description="Get a champion's skin splash art"
)
async def champion_skin_splash_art(ctx, champion_name: str, skin_number: int):

    try:
        splash_art_url = print_champion_skin_splash_art(champion_name, skin_number)
        # load image from url and send it to the channel
        await ctx.send(splash_art_url)
    
    except:
        await ctx.send("Skin not found.")

@bot.command(
    name="championstats",
    description="Get a champion's current stats"
)
async def champion_stats(ctx, champion_name: str):
    
        try:
            await ctx.send("Please wait while we fetch the champion stats...")

            tier = print_champion_tier(champion_name)
            winrate = print_champion_winrate(champion_name)
            pickrate = print_champion_pickrate(champion_name)
            banrate = print_champion_banrate(champion_name)


            stats = f"""
**Current stats for {champion_name}**:
**Tier**: {tier}
**Winrate**: {winrate}
**Pickrate**: {pickrate}
**Banrate**: {banrate}
            """
            await ctx.send(stats)

        except:
            await ctx.send("Champion not found.")


@bot.command(
    name="championcounters",
    description="Get a champion's counters"
)
async def champion_counters(ctx, champion_name: str):
    
    try:
        await ctx.send("Please wait while we fetch the champion counters...")
        best_picks, worst_picks = print_champion_counters(champion_name)
        message = f"""
\r**Best Picks vs {champion_name}**:
        """
        for i in best_picks:
            message += f"\r**Champion Name**: {i['champion_name']}"
            message += f"\r**Win Rate**: {i['win_rate']}"
            message += f"\r**Total Games**: {i['total_games']}"
            message += f"\n"
        
        message += f"""
\r**Worst Picks vs {champion_name}**:
        """
        for i in worst_picks:
            message += f"\r**Champion Name**: {i['champion_name']}"
            message += f"\r**Win Rate**: {i['win_rate']}"
            message += f"\r**Total Games**: {i['total_games']}"
            message += f"\n"
        
        await ctx.send(message)
    
    except:
        await ctx.send("Champion not found.")




@bot.command(
    name="championrunes",
    description="Get a champion's recommended runes"
)
async def champion_recommended_runes(ctx, champion_name: str):
    
    try:
        await ctx.send("Please wait while we fetch the champion runes...")
        primary_tree_name, primary_runes, secondary_tree_name, secondary_runes, stat_shards = print_champion_recommended_runes(champion_name)
        message = f"""
\r**Recommended runes for {champion_name}**:
\r**Primary Tree**: {primary_tree_name}
\r**Primary Runes**:
        """
        for rune in list(dict.fromkeys(primary_runes)):
            message += f"\r{rune.replace('The Rune', '').replace('The Keystone', '').strip()}"

        message += f"""
\r**Secondary Tree**: {secondary_tree_name}
\r**Secondary Runes**:
        """
        for rune in list(dict.fromkeys(secondary_runes)):
            message += f"\r{rune.replace('The Rune', '').strip()}"

        message += f"""
\r**Stat Shards**:
        """
        for shard in list(dict.fromkeys(stat_shards)):
            message += f"\r{shard.replace('The', '').replace('Shard', '').strip()}"

        await ctx.send(message)

    except:
        await ctx.send("Champion not found.")


@bot.command(
    name="championspells",
    description="Get a champion's recommended spells"
)
async def champion_recommended_spells(ctx, champion_name: str):

    try:
        await ctx.send("Please wait while we fetch the champion spells...")
        spells = print_champion_recommended_spells(champion_name)
        message = f"""
\r**Recommended spells for {champion_name}**:
        """
        for spell in spells:
            message += f"\r{spell.replace('Summoner Spell', '').strip()}"

        await ctx.send(message)
        
    except:
        await ctx.send("Champion not found.")

@bot.command(
    name="championbuild",
    description="Get a champion's recommended build"
)
async def champion_recommended_build(ctx, champion_name: str):
    
    try: 
        await ctx.send("Please wait while we fetch the champion build...")
        starter_items, core_build, boots, final_build = print_champion_recommended_build(champion_name)
        message = f"""
\r**Recommended build for {champion_name}**:
\r**Starter items**:
        """
        for item in starter_items:
            message += f"\r{item}"
            
        message += f"""
\r**Core build**:
        """
        for item in core_build:
            message += f"\r{item}"

        message += f"""
\r**Boots**:
        """
        for item in boots:
            message += f"\r{item}"

        message += f"""
\r**Final build**:
        """
        for item in final_build:
            message += f"\r{item}"

        await ctx.send(message)

    except:
        await ctx.send("Champion not found.")



@bot.command(
    name="championskillorder",
    description="Get a champion's recommended skill order"
)
async def champion_skill_order(ctx, champion_name: str):
    
    try:
        await ctx.send("Please wait while we fetch the champion skill order...")
        skill_order = print_champion_skill_order(champion_name)
        message = f"""
\r**Recommended skill order for {champion_name}**:
        """
        for skill in skill_order:
            message += f"\r**Ability**: {skill['skill_label']}"
            message += f"\r**Level**: {skill['skill_levels']}"
        
        await ctx.send(message)

    except:
        await ctx.send("Champion not found.")



@bot.command(
    name="help",
    description="Show available commands"
)
async def help_command(ctx):
    help_text = """
Available commands:
- !championrotation: See current champion rotation
- !championinfo <champion_name>: Get information about a specific champion
- !iteminfo <item_name>: Get information about a specific item
- !runeinfo <rune_name>: Get information about a specific rune
- !summonerspellinfo <spell_name>: Get information about a specific summoner spell
- !championsplashart <champion_name>: Get a champion's splash art
- !championskinsplashart <champion_name> <skin_number>: Get a champion's skin splash art
- !championstats <champion_name>: Get a champion's current stats
- !championcounters <champion_name>: Get a champion's counters
- !championrecommendedrunes <champion_name>: Get a champion's recommended runes
- !championrecommendedspells <champion_name>: Get a champion's recommended spells
- !championrecommendedbuild <champion_name>: Get a champion's recommended build
- !championskillorder <champion_name>: Get a champion's recommended skill order
    """

    await ctx.send(help_text)

if __name__ == '__main__':
    bot.run(os.getenv("DISCORD_TOKEN"))
