import requests 
from bs4 import BeautifulSoup
from .get_version_mod import get_version


########################
VERSION = get_version()  #
########################


def print_rune_info_by_name(rune_name):
    url = f"https://ddragon.leagueoflegends.com/cdn/{VERSION}/data/en_US/runesReforged.json"

    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3"
    }

    try:
        response = requests.get(url, headers=headers)
        response.raise_for_status()
        rune_data = response.json()

        for rune in rune_data:
            for slot in rune["slots"]:
                for rune_info in slot["runes"]:
                    if rune_info["name"].lower() == rune_name.lower():
                        soup = BeautifulSoup(rune_info["longDesc"], "html.parser")
                        for br in soup.find_all("br"):
                            br.replace_with("\n")

        if rune_info:
            return rune_info

        else:
            print("Rune not found.")

    except requests.exceptions.HTTPError as err:
        print(f"HTTP error occurred: {err}")
    except requests.exceptions.RequestException as err:
        print(f"Error occurred: {err}")

# soup = BeautifulSoup(rune_info["longDesc"], "html.parser")
# for br in soup.find_all("br"):
#     br.replace_with("\n")

# print(f"Rune name: {rune_info['name']}")
# print(f"Rune description:\n{soup.get_text()}")