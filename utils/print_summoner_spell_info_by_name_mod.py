import requests
from .get_version_mod import get_version


########################
VERSION = get_version()  #
########################


def print_summoner_spell_info_by_name(spell_name, language):
    url = f"https://ddragon.leagueoflegends.com/cdn/{VERSION}/data/{language}/summoner.json"

    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3"
    }

    try:
        response = requests.get(url, headers=headers)
        response.raise_for_status()
        spell_data = response.json()

        spell_data = spell_data["data"]
        for spell in spell_data.values():
            if spell["name"].lower() == spell_name.lower():
                if spell:
                    return spell
                else :
                    print("Spell not found")
                    return None

    except requests.exceptions.HTTPError as err:
        print(f"HTTP error occurred: {err}")
        return None
    except requests.exceptions.RequestException as err:
        print(f"Error occurred: {err}")
        return None

# print(f"Spell name: {spell['name']}")
# print(f"Spell description: {spell['description']}")
# print(f"Spell cooldown: {spell['cooldownBurn']}")
# print(f"Summoner level required: {spell['summonerLevel']}")