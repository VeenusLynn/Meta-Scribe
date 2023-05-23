import requests
from .get_version_mod import get_version


########################
VERSION = get_version()  #
########################


def print_champion_info_by_name(champion_name):
    champion_name = champion_name.capitalize()
    url = f"https://ddragon.leagueoflegends.com/cdn/{VERSION}/data/en_US/champion/{champion_name}.json"

    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3"
    }

    try:
        response = requests.get(url, headers=headers)
        response.raise_for_status()
        champion_data = response.json()

        champion_data = champion_data["data"]
        for champ in champion_data.values():
            if champ["name"].lower() == champion_name.lower():
                return champ
            
        else:
            print("Champion not found.")

    except requests.exceptions.HTTPError as err:
        print(f"HTTP error occurred: {err}")
    except requests.exceptions.RequestException as err:
        print(f"Error occurred: {err}")



# print(f"Champion ID: {champ['key']}")
# print(f"Name: {champ['name']}")
# print(f"Title: {champ['title']}")
# print(f"Lore: {champ['lore']}")
# print(f"Attack: {champ['info']['attack']}")
# print(f"Defense: {champ['info']['defense']}")
# print(f"Magic: {champ['info']['magic']}")
# print(f"Difficulty: {champ['info']['difficulty']}")
# print(f"Type: {champ['tags']}")
# print(f"Energy/Mana: {champ['partype']}")
# print(f"Health: {champ['stats']['hp']}")
# print(f"Health Regen: {champ['stats']['hpregen']}")
# print(f"Mana: {champ['stats']['mp']}")
# print(f"Mana Regen: {champ['stats']['mpregen']}")
# print(f"Armor: {champ['stats']['armor']}")
# print(f"Magic Resist: {champ['stats']['spellblock']}")
# print(f"Attack Damage: {champ['stats']['attackdamage']}")
# print(f"Attack Range: {champ['stats']['attackrange']}")
# print(f"Attack Speed: {champ['stats']['attackspeed']}")
# print(f"Movement Speed: {champ['stats']['movespeed']}")
# print(f"Ally Tips: {champ['allytips']}")
# print(f"Enemy Tips: {champ['enemytips']}")
# print(f"Passive: {champ['passive']['name']}")
# print(f"Passive Description: {champ['passive']['description']}")
# print(f"Q: {champ['spells'][0]['name']}")
# print(f"Q Description: {champ['spells'][0]['description']}")
# print(f"W: {champ['spells'][1]['name']}")
# print(f"W Description: {champ['spells'][1]['description']}")
# print(f"E: {champ['spells'][2]['name']}")
# print(f"E Description: {champ['spells'][2]['description']}")
# print(f"R: {champ['spells'][3]['name']}")
# print(f"R Description: {champ['spells'][3]['description']}")
