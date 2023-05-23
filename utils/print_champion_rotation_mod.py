import requests
import dotenv
import os
from .get_champion_info_by_id_mod import get_champion_info_by_id


dotenv.load_dotenv()

# Get API key from .env file
API_KEY = os.getenv("API_KEY")


def print_champion_rotation():
    url = f"https://euw1.api.riotgames.com/lol/platform/v3/champion-rotations?api_key={API_KEY}"

    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3"
    }

    try:
        response = requests.get(url, headers=headers)
        response.raise_for_status()
        rotation_data = response.json()

        champion_rotation = rotation_data["freeChampionIds"]

        if champion_rotation:
            return champion_rotation
        else:
            print("Failed to fetch champion rotation.")
            return None

    except requests.exceptions.HTTPError as err:
        print(f"HTTP error occurred: {err}")
        return None
    except requests.exceptions.RequestException as err:
        print(f"Error occurred: {err}")
        return None

# print("Champion Rotation:")
# print("------")
# for champion_id in champion_rotation:
#     champion_info = get_champion_info_by_id(champion_id)
#     if champion_info:
#         print(f"Champion ID: {champion_id}")
#         print(f"Name: {champion_info['name']}")
#         print(f"Title: {champion_info['title']}")
#         print("------")
