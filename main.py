from discord.ext import commands
import dotenv
import os
import interactions
from discord import Status, Activity, Game
from bs4 import BeautifulSoup
from time import sleep

from utils import *

dotenv.load_dotenv()

# Get API key from .env file
API_KEY = os.getenv("API_KEY")

# Create an instance of the bot
bot = interactions.Client(token=os.getenv("DISCORD_TOKEN"))


@interactions.listen()
async def on_ready():
    print(f'Bot is ready.')
    await bot.change_presence(activity=Game(name="League of Legends"))


@interactions.slash_command(
    name="fr",
    description="Changer la langue du bot en français"
)
async def fr(ctx: interactions.SlashContext):
    global language
    language = "fr_FR"
    await ctx.defer()
    await ctx.send("La langue du bot est maintenant en français.")

@interactions.slash_command(
    name="en",
    description="Change the bot's language to English"
)
async def en(ctx: interactions.SlashContext):
    global language
    language = "en_US"
    await ctx.defer()
    await ctx.send("The bot's language is now in English.")

@interactions.slash_command(
    name="bestmidlaner",
    description="Get the best midlaner"
)
async def best_midlaner(ctx: interactions.SlashContext):
    try:
        await ctx.defer()

        await ctx.send("Please wait while we fetch the best midlaner...")
        sleep(3)
        await ctx.send("Best midlaner in the world is not1cyyy#EUW")
    except:
        await ctx.send("Failed to fetch best midlaner.")

@interactions.slash_command(
    name="besttoplaner",
    description="Get the best toplaner"
)
async def best_toplaner(ctx: interactions.SlashContext):
    try:
        await ctx.defer()
        await ctx.send("Please wait while we fetch the best toplaner...")
        sleep(3)
        await ctx.send("Best toplaner in the world is DistortLynn#EUW")
    except:
        await ctx.send("Failed to fetch best toplaner.")

@interactions.slash_command(
    name="bestsupport",
    description="Get the best support"
)
async def best_support(ctx: interactions.SlashContext):
    try:
        await ctx.defer()
        await ctx.send("Please wait while we fetch the best support...")
        sleep(3)
        await ctx.send("Best support in the world is Eve SatOrU#EUW")
    except:
        await ctx.send("Failed to fetch best support.")

@interactions.slash_command(
    name="bestadc",
    description="Get the best adc"
)
async def best_adc(ctx: interactions.SlashContext):
    try:
        await ctx.defer()
        await ctx.send("Please wait while we fetch the best adc...")
        sleep(3)
        await ctx.send("Best adc in the world is Hi im Lon#EUW")
    except:
        await ctx.send("Failed to fetch best adc.")

@interactions.slash_command(
    name="championrotation",
    description="See the current champion rotation"
    )
async def champion_rotation(ctx: interactions.SlashContext):

    try:
        await ctx.defer()
        await ctx.send("Please wait while we fetch the champion rotation...")
        champion_rotation = print_champion_rotation()
        message = """
\r**Champion Rotation:**
        """
        if champion_rotation:
            for champion_id in champion_rotation:
                champion_info = get_champion_info_by_id(champion_id, language)
                if champion_info:
                    message += f"\r**Champion ID**: {champion_id}"
                    message += f"\r**Name**: {champion_info['name']}"
                    message += f"\r**Title**: {champion_info['title']}"

        await ctx.send(message)
    except:
        await ctx.send("Failed to fetch champion rotation.")


@interactions.slash_command(
    name="championinfo",
    description="Get information about a specific champion",
        options = [
        interactions.SlashCommandOption(
            name="champion_name",
            description="Which champion do you want to get information about?",
            type=interactions.OptionType.STRING,
            required=True,
        ),
    ]
)
async def champion_info(ctx: interactions.SlashContext, champion_name: str):

    try:
        await ctx.defer()
        champ = print_champion_info_by_name(champion_name, language)
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


@interactions.slash_command(
    name="iteminfo",
    description="Get information about a specific item",
        options = [
        interactions.SlashCommandOption(
            name="item_name",
            description="Which item do you want to get information about?",
            type=interactions.OptionType.STRING,
            required=True,
        ),
    ]
)
async def item_info(ctx: interactions.SlashContext, item_name: str):

    try:
        await ctx.defer()
        item = print_item_info_by_name(item_name, language)
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


@interactions.slash_command(
    name="runeinfo",
    description="Get information about a specific rune",
        options = [
        interactions.SlashCommandOption(
            name="rune_name",
            description="Which rune do you want to get information about?",
            type=interactions.OptionType.STRING,
            required=True,
        ),
    ]
)
async def rune_info(ctx: interactions.SlashContext, rune_name: str):

    try:
        await ctx.defer()
        rune = print_rune_info_by_name(rune_name, language)
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


@interactions.slash_command(
    name="summonerspellinfo",
    description="Get information about a specific summoner spell",
        options = [
        interactions.SlashCommandOption(
            name="spell_name",
            description="Which summoner spell do you want to get information about?",
            type=interactions.OptionType.STRING,
            required=True,
        ),
    ]
)
async def summoner_spell_info(ctx: interactions.SlashContext, spell_name: str):

    try:
        await ctx.defer()
        spell = print_summoner_spell_info_by_name(spell_name, language)

        info = f"""
**Spell name**: {spell['name']}
**Spell description**: {spell['description']}
**Cooldown**: {spell['cooldownBurn']} seconds
**Summoner level required**: {spell['summonerLevel']}
        """
        await ctx.send(info)

    except:
        await ctx.send("Summoner spell not found.")


@interactions.slash_command(
    name="championsplashart",
    description="Get a champion's splash art",
        options = [
        interactions.SlashCommandOption(
            name="champion_name",
            description="Which champion do you want to get information about?",
            type=interactions.OptionType.STRING,
            required=True,
        ),
    ]
)
async def champion_splash_art(ctx: interactions.SlashContext, champion_name: str):

    try:
        await ctx.defer()
        splash_art_url = print_champion_splash_art(champion_name)

        await ctx.send(splash_art_url)
    except:
        await ctx.send("Champion not found.")

@interactions.slash_command(
    name="championskinsplashart",
    description="Get a champion's skin splash art",
        options = [
        interactions.SlashCommandOption(
            name="champion_name",
            description="Which champion do you want to get information about?",
            type=interactions.OptionType.STRING,
            required=True
        ),
        interactions.SlashCommandOption(
            name="skin_number",
            description="Which skin do you want to get information about?",
            type=interactions.OptionType.INTEGER,
            required=True
        )
    ]
)
async def champion_skin_splash_art(ctx: interactions.SlashContext, champion_name: str, skin_number: int):

    try:
        await ctx.defer()
        splash_art_url = print_champion_skin_splash_art(champion_name, skin_number)

        await ctx.send(splash_art_url)
    
    except:
        await ctx.send("Skin not found.")

@interactions.slash_command(
    name="championstats",
    description="Get a champion's current stats",
        options = [
        interactions.SlashCommandOption(
            name="champion_name",
            description="Which champion do you want to get information about?",
            type=interactions.OptionType.STRING,
            required=True,
        ),
    ]
)
async def champion_stats(ctx: interactions.SlashContext, champion_name: str):
    
        try:
            await ctx.defer()
            await ctx.send("Please wait while we fetch the champion stats...")

            tier = print_champion_tier(champion_name)
            winrate = print_champion_winrate(champion_name)
            pickrate = print_champion_pickrate(champion_name)
            banrate = print_champion_banrate(champion_name)


            stats = f"""
**Current stats for {champion_name.capitalize()}**:
**Tier**: {tier}
**Winrate**: {winrate}
**Pickrate**: {pickrate}
**Banrate**: {banrate}
            """
            await ctx.send(stats)

        except:
            await ctx.send("Champion not found.")


@interactions.slash_command(
    name="championcounters",
    description="Get a champion's counters",
        options = [
        interactions.SlashCommandOption(
            name="champion_name",
            description="Which champion do you want to get information about?",
            type=interactions.OptionType.STRING,
            required=True,
        ),
    ]
)
async def champion_counters(ctx: interactions.SlashContext, champion_name: str):
    
    try:
        await ctx.defer()
        await ctx.send("Please wait while we fetch the champion counters...")
        best_picks, worst_picks = print_champion_counters(champion_name)
        message = f"""
\r**Best Picks vs {champion_name.capitalize()}**:
        """
        for i in best_picks:
            message += f"\r**Champion Name**: {i['champion_name']}"
            message += f"\r**Win Rate**: {i['win_rate']}"
            message += f"\r**Total Games**: {i['total_games']}"
            message += f"\n"
        
        message += f"""
\r**Worst Picks vs {champion_name.capitalize()}**:
        """
        for i in worst_picks:
            message += f"\r**Champion Name**: {i['champion_name']}"
            message += f"\r**Win Rate**: {i['win_rate']}"
            message += f"\r**Total Games**: {i['total_games']}"
            message += f"\n"
        
        await ctx.send(message)
    
    except:
        await ctx.send("Champion not found.")




@interactions.slash_command(
    name="championrunes",
    description="Get a champion's recommended runes",
        options = [
        interactions.SlashCommandOption(
            name="champion_name",
            description="Which champion do you want to get information about?",
            type=interactions.OptionType.STRING,
            required=True,
        ),
    ]
)

async def champion_recommended_runes(ctx: interactions.SlashContext, champion_name: str):
    
    try:
        await ctx.defer()
        await ctx.send("Please wait while we fetch the champion runes...")
        primary_tree_name, primary_runes, secondary_tree_name, secondary_runes, stat_shards = print_champion_recommended_runes(champion_name)
        message = f"""
\r**Recommended runes for {champion_name.capitalize()}**:
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


@interactions.slash_command(
    name="championspells",
    description="Get a champion's recommended spells",
        options = [
        interactions.SlashCommandOption(
            name="champion_name",
            description="Which champion do you want to get information about?",
            type=interactions.OptionType.STRING,
            required=True,
        ),
    ]
)
async def champion_recommended_spells(ctx: interactions.SlashContext, champion_name: str):

    try:
        await ctx.defer()
        await ctx.send("Please wait while we fetch the champion spells...")
        spells = print_champion_recommended_spells(champion_name)
        message = f"""
\r**Recommended spells for {champion_name.capitalize()}**:
        """
        for spell in spells:
            message += f"\r{spell.replace('Summoner Spell', '').strip()}"

        await ctx.send(message)
        
    except:
        await ctx.send("Champion not found.")

@interactions.slash_command(
    name="championbuild",
    description="Get a champion's recommended build",
            options = [
        interactions.SlashCommandOption(
            name="champion_name",
            description="Which champion do you want to get information about?",
            type=interactions.OptionType.STRING,
            required=True,
        ),
    ]
)
async def champion_recommended_build(ctx: interactions.SlashContext, champion_name: str):
    
    try: 
        await ctx.defer()
        await ctx.send("Please wait while we fetch the champion build...")
        starter_items, core_build, boots, final_build = print_champion_recommended_build(champion_name)
        message = f"""
\r**Recommended build for {champion_name.capitalize()}**:
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



@interactions.slash_command(
    name="championskillorder",
    description="Get a champion's recommended skill order",
        options = [
        interactions.SlashCommandOption(
            name="champion_name",
            description="Which champion do you want to get information about?",
            type=interactions.OptionType.STRING,
            required=True,
        ),
    ]
)
async def champion_skill_order(ctx: interactions.SlashContext, champion_name: str):
    
    try:
        await ctx.defer()
        await ctx.send("Please wait while we fetch the champion skill order...")
        skill_order = print_champion_skill_order(champion_name)
        message = f"""
\r**Recommended skill order for {champion_name.capitalize()}**:
        """
        for skill in skill_order:
            message += f"\r**Ability**: {skill['skill_label']}"
            message += f"\r**Level**: {skill['skill_levels']}"
        
        await ctx.send(message)

    except:
        await ctx.send("Champion not found.")



@interactions.slash_command(
    name="help",
    description="Show available commands"
)
async def help_command(ctx: interactions.SlashContext):
    await ctx.defer()
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
- /championrunes <champion_name>: Get a champion's recommended runes
- /championspells <champion_name>: Get a champion's recommended spells
- /championbuild <champion_name>: Get a champion's recommended build
- /championskillorder <champion_name>: Get a champion's recommended skill order
    """

    await ctx.send(help_text)

if __name__ == '__main__':

    # keep_alive()
    bot.start()
