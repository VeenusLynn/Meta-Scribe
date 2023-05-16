import requests
import dotenv
import os

dotenv.load_dotenv()

# Get API key from .env file
API_KEY = os.getenv('API_KEY') 

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
    url = 'https://ddragon.leagueoflegends.com/cdn/13.9.1/data/en_US/championFull.json'

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
    url = f'https://ddragon.leagueoflegends.com/cdn/13.9.1/data/en_US/champion/{champion_name}.json'

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
    url = 'https://ddragon.leagueoflegends.com/cdn/13.9.1/data/en_US/championFull.json'

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

# Prompt the user for their choice
print("Choose an option:")
print("1. See current champion rotation")
print("2. Get information about a specific champion")
choice = input("Enter your choice (1 or 2): ")

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
    # champion_id = get_champion_id(champion_name) 

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


        # TO DO : Add more champion info
    else:
        print("Champion not found.")
else:
    print("Invalid choice. Please select either 1 or 2.")

