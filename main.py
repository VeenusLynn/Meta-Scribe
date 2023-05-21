import requests
import dotenv
import os
from bs4 import BeautifulSoup
import json


dotenv.load_dotenv()

# Get API key from .env file
API_KEY = os.getenv('API_KEY') 


def get_version():
    url = f'https://ddragon.leagueoflegends.com/api/versions.json'

    try:
        response = requests.get(url)
        response.raise_for_status()
        version_data = response.json()

        return version_data[0]

    except requests.exceptions.HTTPError as err:
        print(f"HTTP error occurred: {err}")
    except requests.exceptions.RequestException as err:
        print(f"Error occurred: {err}")

########################
VERSION = get_version()#
########################

def get_champion_rotation():
    url = f'https://euw1.api.riotgames.com/lol/platform/v3/champion-rotations?api_key={API_KEY}'

    try:
        response = requests.get(url)
        response.raise_for_status()
        rotation_data = response.json()

        return rotation_data['freeChampionIds']

    except requests.exceptions.HTTPError as err:
        print(f"HTTP error occurred: {err}")
    except requests.exceptions.RequestException as err:
        print(f"Error occurred: {err}")


def get_champion_info_by_id(champion_id):
    url = f'https://ddragon.leagueoflegends.com/cdn/{VERSION}/data/en_US/championFull.json'

    try:
        response = requests.get(url)
        response.raise_for_status()
        champion_data = response.json()

        champions = champion_data['data']
        for champ in champions.values():
            if int(champ['key']) == champion_id:
                return champ

    except requests.exceptions.HTTPError as err:
        print(f"HTTP error occurred: {err}")
    except requests.exceptions.RequestException as err:
        print(f"Error occurred: {err}")


def get_champion_info_by_name(champion_name):
    champion_name = champion_name.capitalize()
    url = f'https://ddragon.leagueoflegends.com/cdn/{VERSION}/data/en_US/champion/{champion_name}.json'

    try:
        response = requests.get(url)
        response.raise_for_status()
        champion_data = response.json()

        champion_data = champion_data['data']
        for champ in champion_data.values():
            return champ

    except requests.exceptions.HTTPError as err:
        print(f"HTTP error occurred: {err}")
    except requests.exceptions.RequestException as err:
        print(f"Error occurred: {err}")


def get_champion_id(champion_name):
    url = f'https://ddragon.leagueoflegends.com/cdn/{VERSION}/data/en_US/championFull.json'

    try:
        response = requests.get(url)
        response.raise_for_status()
        champion_data = response.json()

        champions = champion_data['data']
        for champ in champions.values():
            if champ['name'].lower() == champion_name.lower():
                return int(champ['key'])

    except requests.exceptions.HTTPError as err:
        print(f"HTTP error occurred: {err}")
    except requests.exceptions.RequestException as err:
        print(f"Error occurred: {err}")

def get_item_info_by_name(item_name):

    url = f'https://ddragon.leagueoflegends.com/cdn/{VERSION}/data/en_US/item.json'

    try:
        response = requests.get(url)
        response.raise_for_status()
        item_data = response.json()

        item_data = item_data['data']
        for item in item_data.values():
            if item['name'].lower() == item_name.lower():
                return item

    except requests.exceptions.HTTPError as err:
        print(f"HTTP error occurred: {err}")
    except requests.exceptions.RequestException as err:
        print(f"Error occurred: {err}")

def get_rune_info_by_name(rune_name):
    url = f'https://ddragon.leagueoflegends.com/cdn/{VERSION}/data/en_US/runesReforged.json'

    try:
        response = requests.get(url)
        response.raise_for_status()
        rune_data = response.json()

        for rune in rune_data:
            for slot in rune['slots']:
                for rune_info in slot['runes']:
                    if rune_info['name'].lower() == rune_name.lower():
                        return rune_info

        return None

    except requests.exceptions.HTTPError as err:
        print(f"HTTP error occurred: {err}")
    except requests.exceptions.RequestException as err:
        print(f"Error occurred: {err}")

def get_summoner_spell_info_by_name(spell_name):
    url = f'https://ddragon.leagueoflegends.com/cdn/{VERSION}/data/en_US/summoner.json'

    try:
        response = requests.get(url)
        response.raise_for_status()
        spell_data = response.json()

        spell_data = spell_data['data']
        for spell in spell_data.values():
            if spell['name'].lower() == spell_name.lower():
                return spell

        return None

    except requests.exceptions.HTTPError as err:
        print(f"HTTP error occurred: {err}")
    except requests.exceptions.RequestException as err:
        print(f"Error occurred: {err}")

def get_champion_splash_art(champion_name):
    champion_name = champion_name.capitalize()
    url = f'https://ddragon.leagueoflegends.com/cdn/img/champion/splash/{champion_name}_0.jpg'

    try:
        response = requests.get(url)
        response.raise_for_status()
        return url

    except requests.exceptions.HTTPError as err:
        print(f"HTTP error occurred: {err}")
    except requests.exceptions.RequestException as err:
        print(f"Error occurred: {err}")

def get_champion_skin_splash_art(champion_name, skin_number):
    champion_name = champion_name.capitalize()
    url = f'https://ddragon.leagueoflegends.com/cdn/img/champion/splash/{champion_name}_{skin_number}.jpg'

    try:
        response = requests.get(url)
        response.raise_for_status()
        return url

    except requests.exceptions.HTTPError as err:
        print(f"HTTP error occurred: {err}")
    except requests.exceptions.RequestException as err:
        print(f"Error occurred: {err}")


def main():
    # Prompt the user for their choice
    print("Choose an option:")
    print("1. See current champion rotation")
    print("2. Get information about a specific champion")
    print("3. Get information about a specific item")
    print("4. Get information about a specific rune")
    print("5. Get information about a specific summoner spell")
    print("6. Get a champion's splash art")
    print("7. Get a champion's skin splash art")
    choice = input("Enter your choice: ")

    if choice == '1':
        # Get champion rotation
        champion_rotation = get_champion_rotation()

        if champion_rotation:
            print("Champion Rotation:")
            print("------")
            for champion_id in champion_rotation:
                champion_info = get_champion_info_by_id(champion_id)
                if champion_info:
                    print(f"Champion ID: {champion_id}")
                    print(f"Name: {champion_info['name']}")
                    print(f"Title: {champion_info['title']}")
                    print("------")
        else:
            print("Failed to fetch champion rotation.")
    elif choice == '2':
        # Prompt the user for a champion name
        champion_name = input("Enter a champion name: ")
        champion_info = get_champion_info_by_name(champion_name)
        
        if champion_info:
            print(f"Champion ID: {champion_info['key']}")
            print(f"Name: {champion_info['name']}")
            print(f"Title: {champion_info['title']}")
            print(f"Lore: {champion_info['lore']}")
            print(f"Attack: {champion_info['info']['attack']}")
            print(f"Defense: {champion_info['info']['defense']}")
            print(f"Magic: {champion_info['info']['magic']}")
            print(f"Difficulty: {champion_info['info']['difficulty']}")
            print(f"Type: {champion_info['tags']}")
            print(f"Energy/Mana: {champion_info['partype']}")
            print(f"Health: {champion_info['stats']['hp']}")
            print(f"Health Regen: {champion_info['stats']['hpregen']}")
            print(f"Mana: {champion_info['stats']['mp']}")
            print(f"Mana Regen: {champion_info['stats']['mpregen']}")
            print(f"Armor: {champion_info['stats']['armor']}")
            print(f"Magic Resist: {champion_info['stats']['spellblock']}")
            print(f"Attack Damage: {champion_info['stats']['attackdamage']}")
            print(f"Attack Range: {champion_info['stats']['attackrange']}")
            print(f"Attack Speed: {champion_info['stats']['attackspeed']}")
            print(f"Movement Speed: {champion_info['stats']['movespeed']}")
            print(f"Ally Tips: {champion_info['allytips']}")
            print(f"Enemy Tips: {champion_info['enemytips']}")
            print(f"Passive: {champion_info['passive']['name']}")
            print(f"Passive Description: {champion_info['passive']['description']}")
            print(f"Q: {champion_info['spells'][0]['name']}")
            print(f"Q Description: {champion_info['spells'][0]['description']}")
            print(f"W: {champion_info['spells'][1]['name']}")
            print(f"W Description: {champion_info['spells'][1]['description']}")
            print(f"E: {champion_info['spells'][2]['name']}")
            print(f"E Description: {champion_info['spells'][2]['description']}")
            print(f"R: {champion_info['spells'][3]['name']}")
            print(f"R Description: {champion_info['spells'][3]['description']}")


        else:
            print("Champion not found.")
    
    elif choice == '3':

        item_name = input("Enter an item name: ")
        item_info = get_item_info_by_name(item_name)
        soup = BeautifulSoup(item_info['description'], 'html.parser')
        for br in soup.find_all('br'):
            br.replace_with('\n')

        if item_info:
            print(f"Item name: {item_info['name']}")
            print(f"Item stats:\n{soup.get_text()}")
            print(f"Item cost: {item_info['gold']['total']} Gold")
            
    elif choice == '4':
        rune_name = input("Enter a rune name: ")
        rune_info = get_rune_info_by_name(rune_name)
        soup = BeautifulSoup(rune_info['longDesc'], 'html.parser')
        for br in soup.find_all('br'):
            br.replace_with('\n')

        if rune_info:
            print(f"Rune name: {rune_info['name']}")
            print(f"Rune description:\n{soup.get_text()}")

        else:
            print("Rune not found.")

    elif choice == '5':
        spell_name = input("Enter a summoner spell name: ")
        spell_info = get_summoner_spell_info_by_name(spell_name)

        if spell_info:
            print(f"Spell name: {spell_info['name']}")
            print(f"Spell description: {spell_info['description']}")
            print(f"Spell cooldown: {spell_info['cooldownBurn']}")
            print(f"Summoner level required: {spell_info['summonerLevel']}")

    elif choice == '6':
        champion_name = input("Enter a champion name: ")
        champion_splash_art = get_champion_splash_art(champion_name)

        if champion_splash_art:
            print(f"Splash art: {champion_splash_art}")

        else:
            print("Spell not found.")

    elif choice == '7':
        champion_name = input("Enter a champion name: ")
        skin_number = input("Enter a skin number: ")
        champion_skin_splash_art = get_champion_skin_splash_art(champion_name, skin_number)

        if champion_skin_splash_art:
            print(f"Splash art: {champion_skin_splash_art}")

        else:
            print("Skin not found.")

    else:
        print("Invalid choice.")


if __name__ == '__main__':
    main()
