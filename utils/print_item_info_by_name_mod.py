import requests 
from bs4 import BeautifulSoup
from .get_version_mod import get_version


########################
VERSION = get_version()  #
########################


def print_item_info_by_name(item_name):
    url = f"https://ddragon.leagueoflegends.com/cdn/{VERSION}/data/en_US/item.json"

    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3"
    }

    try:
        response = requests.get(url, headers=headers)
        response.raise_for_status()
        item_data = response.json()

        item_data = item_data["data"]
        for item in item_data.values():
            if item["name"].lower() == item_name.lower():
                return item   

    except requests.exceptions.HTTPError as err:
        print(f"HTTP error occurred: {err}")
    except requests.exceptions.RequestException as err:
        print(f"Error occurred: {err}")
        return None


# soup = BeautifulSoup(item["description"], "html.parser")
# for br in soup.find_all("br"):
#     br.replace_with("\n")

# print(f"Item name: {item['name']}")
# print(f"Item stats:\n{soup.get_text()}")
# print(f"Item cost: {item['gold']['total']} Gold")