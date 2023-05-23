import requests
from .get_version_mod import get_version


########################
VERSION = get_version()  #
########################


def get_champion_info_by_id(champion_id):
    url = f'https://ddragon.leagueoflegends.com/cdn/{VERSION}/data/en_US/championFull.json'

    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3'
    }
    

    try:
        response = requests.get(url, headers=headers)
        response.raise_for_status()
        champion_data = response.json()

        champions = champion_data['data']
        for champ in champions.values():
            if int(champ['key']) == champion_id:
                return champ

    except requests.exceptions.HTTPError as err:
        print(f"HTTP error occurred: {err}")
        return None
    except requests.exceptions.RequestException as err:
        print(f"Error occurred: {err}")
        return None