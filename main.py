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

def get_champion_info(champion_id):
    url = 'https://ddragon.leagueoflegends.com/cdn/13.9.1/data/en_US/champion.json'

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
            champion_info = get_champion_info(champion_id)
            if champion_info:
                print(f"Champion ID: {champion_id}")
                print(f"Name: {champion_info['name']}")
                print(f"Title: {champion_info['title']}")
                print("------")
    else:
        print("Failed to fetch champion rotation.")
elif choice == '2':
    # Prompt the user for a champion ID
    champion_id = int(input("Enter a champion ID: "))

    champion_info = get_champion_info(champion_id)
    if champion_info:
        print(f"Champion ID: {champion_id}")
        print(f"Name: {champion_info['name']}")
        print(f"Title: {champion_info['title']}")
        print(f"Blurb: {champion_info['blurb']}")
        # TO DO : Add more champion info
    else:
        print("Champion not found.")
else:
    print("Invalid choice. Please select either 1 or 2.")
