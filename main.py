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

    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3'
    }
    

    try:
        response = requests.get(url, headers=headers)
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

def get_champion_tier(champion_name):
    url = f'https://u.gg/lol/champions/{champion_name}/build'

    # Set custom headers to mimic a web browser
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3'
    }

    # Send an HTTP GET request to the u.gg Irelia build page with custom headers
    response = requests.get(url, headers=headers)

    # Check if the request was successful
    if response.status_code == 200:
        # Parse the HTML content using BeautifulSoup
        soup = BeautifulSoup(response.content, 'html.parser')

        # Find the elements containing the tier
        tier_element = soup.find('div', {'class': 'champion-tier media-query media-query_MOBILE_LARGE__DESKTOP_LARGE'})

        # Extract the text from the elements
        tier = tier_element.text.strip()

        if tier_element:
            # Extract the text from the element and add a space after the percentage sign
            tier = tier_element.text.strip().replace('Tier', '')

            return tier

    else:
        # Request was unsuccessful
        print(f"Failed to retrieve winrate. Status code: {response.status_code}")
        return None
 
def get_champion_winrate(champion_name):
    url = f'https://u.gg/lol/champions/{champion_name}/build'

    # Set custom headers to mimic a web browser
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3'
    }

    # Send an HTTP GET request to the u.gg Irelia build page with custom headers
    response = requests.get(url, headers=headers)

    # Check if the request was successful
    if response.status_code == 200:
        # Parse the HTML content using BeautifulSoup
        soup = BeautifulSoup(response.content, 'html.parser')

        # Find the elements containing the win rate
        win_rate_element = soup.find('span', {'class': 'win-rate'})

        # Extract the text from the elements
        win_rate = win_rate_element.text.strip()

        if win_rate_element:
            # Extract the text from the element and add a space after the percentage sign
            win_rate = win_rate_element.text.strip().replace('WR', '')

            return win_rate

    else:
        # Request was unsuccessful
        print(f"Failed to retrieve winrate. Status code: {response.status_code}")
        return None
 
def get_champion_pickrate(champion_name):
    url = f'https://u.gg/lol/champions/{champion_name}/build'

    # Set custom headers to mimic a web browser
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3'
    }

    # Send an HTTP GET request to the u.gg champion build page with custom headers
    response = requests.get(url, headers=headers)

    # Check if the request was successful
    if response.status_code == 200:
        # Parse the HTML content using BeautifulSoup
        soup = BeautifulSoup(response.content, 'html.parser')

        # Find the elements containing the pick rate
        pick_rate_element = soup.find('div', {'class': 'pick-rate'})

        # Extract the text from the element
        pick_rate = pick_rate_element.text.strip()

        if pick_rate_element:
            # Extract the text from the element and add a space after the percentage sign
            pick_rate = pick_rate_element.text.strip().replace('%', '% ').replace('Pick Rate', '')

            return pick_rate

    else:
        # Request was unsuccessful
        print(f"Failed to retrieve pick rate. Status code: {response.status_code}")
        return None

def get_champion_banrate(champion_name):
    url = f'https://u.gg/lol/champions/{champion_name}/build'

    # Set custom headers to mimic a web browser
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3'
    }

    # Send an HTTP GET request to the u.gg champion build page with custom headers
    response = requests.get(url, headers=headers)

    # Check if the request was successful
    if response.status_code == 200:
        # Parse the HTML content using BeautifulSoup
        soup = BeautifulSoup(response.content, 'html.parser')

        # Find the elements containing the pick rate
        ban_rate_element = soup.find('div', {'class': 'ban-rate'})

        # Extract the text from the element
        ban_rate = ban_rate_element.text.strip()

        if ban_rate_element:
            # Extract the text from the element and add a space after the percentage sign
            ban_rate = ban_rate_element.text.strip().replace('%', '% ').replace('Ban Rate', '')

            return ban_rate

    else:
        # Request was unsuccessful
        print(f"Failed to retrieve pick rate. Status code: {response.status_code}")
        return None

def extract_div_html(url, div_class):

    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3'
    }
    

    # Send a GET request to the URL
    response = requests.get(url, headers=headers)
    
    # Check if the request was successful
    if response.status_code == 200:
        # Get the HTML content of the page
        html_content = response.text
        
        # Create a BeautifulSoup object for parsing the HTML
        soup = BeautifulSoup(html_content, 'html.parser')
        
        # Find the div with the specified class name
        target_div = soup.find('div', class_=div_class)
        
        # Check if the div exists
        if target_div:
            # Get the HTML code of the div
            div_html = str(target_div)
            
            # Return the div HTML
            return div_html
        
        else:
            print(f"Div with class '{div_class}' not found.")
    
    else:
        print(f"Request failed with status code {response.status_code}.")
    
    return None

def extract_a_html(url, target_href):
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3'
    }

    # Send a GET request to the URL
    response = requests.get(url, headers=headers)

    # Check if the request was successful
    if response.status_code == 200:
        # Get the HTML content of the page
        html_content = response.text

        # Create a BeautifulSoup object for parsing the HTML
        soup = BeautifulSoup(html_content, 'html.parser')

        # Find all <a> tags with the specified href
        target_a_tags = soup.find_all('a', href=target_href)

        # Check if any <a> tags exist
        if target_a_tags:
            # Concatenate the HTML codes of the <a> tags
            a_html = ''.join(str(a_tag) for a_tag in target_a_tags)

            # Return the concatenated <a> tag HTML codes
            return a_html

        else:
            print(f"No <a> tags found with href '{target_href}'.")

    else:
        print(f"Request failed with status code {response.status_code}.")

    return None

def get_champion_counters(champion_name):

    # Extract the HTML code of the div with class 'content'
    html_code = extract_div_html(f'https://u.gg/lol/champions/{champion_name.lower()}/counter', 'champion-profile-page')

    soup = BeautifulSoup(html_code, 'html.parser')

    champion_name = champion_name.capitalize()
    tmp = champion_name

    # Extract Best Picks 
    best_picks_div = soup.find('div', class_='counters-column')
    best_picks_title = best_picks_div.find('div', text=f'Best Picks vs {champion_name}')
    best_picks_list = best_picks_title.find_next('div', class_='counters-list').find_all('a')

    best_picks = []
    for pick in best_picks_list:
        champion_name = pick.find('div', class_='champion-name').text
        win_rate = pick.find('div', class_='win-rate').text
        total_games = pick.find('div', class_='total-games').text

        best_picks.append({
            'champion_name': champion_name,
            'win_rate': win_rate.replace('WR',''),
            'total_games': total_games
        })

    # Extract Worst Picks 
    worst_picks_div = soup.find('div', class_='counters-list worst-win-rate')
    worst_picks_list = worst_picks_div.find_all('a')

    worst_picks = []
    for pick in worst_picks_list:
        champion_name = pick.find('div', class_='champion-name').text
        win_rate = pick.find('div', class_='win-rate').text
        total_games = pick.find('div', class_='total-games').text

        worst_picks.append({
            # 'champion_image': champion_image,
            'champion_name': champion_name,
            'win_rate': win_rate.replace('WR',''),
            'total_games': total_games
        })

    champion_name = tmp


    # Print the extracted information
    print(f'\nBest Picks vs {champion_name}:\n')
    print("----------------------------------")
    for pick in best_picks:
        print(f"Champion Name: {pick['champion_name']}")
        print(f"Win Rate: {pick['win_rate']}")
        print(f"Total Games: {pick['total_games']}")
        print("----------------------------------")

    print(f'\nWorst Picks vs {champion_name}:\n')
    print("----------------------------------")
    for pick in worst_picks:
        print(f"Champion Name: {pick['champion_name']}")
        print(f"Win Rate: {pick['win_rate']}")
        print(f"Total Games: {pick['total_games']}")
        print("----------------------------------")

def get_champion_recommended_runes(champion_name):

    html_code = extract_div_html(f'https://u.gg/lol/champions/{champion_name.lower()}/build', 'rune-trees-container-2 media-query media-query_MOBILE_LARGE__DESKTOP_LARGE')

    soup = BeautifulSoup(html_code, 'html.parser')

    primary_tree = soup.find(class_='primary-tree')
    primary_tree_name = primary_tree.find(class_='perk-style-title').text
    resolve_keystone = primary_tree.find(class_='perk keystone perk-active')
    resolve_runes = primary_tree.find_all(class_='perk perk-active')

    secondary_tree = soup.find(class_='secondary-tree')
    secondary_tree_name = secondary_tree.find(class_='perk-style-title').text
    inspiration_keystone = secondary_tree.find(class_='perk perk-active')
    inspiration_runes = secondary_tree.find_all(class_='perk perk-active')

    stat_shards = soup.find(class_='stat-shards-container_v2')
    stat_shard_rows = stat_shards.find_all(class_='perk-row stat-shard-row')
    stat_shards_active = [row.find(class_='shard shard-active') for row in stat_shard_rows]

    primary_runes = [resolve_keystone.img['alt']] + [rune.img['alt'] for rune in resolve_runes]
    secondary_runes = [inspiration_keystone.img['alt']] + [rune.img['alt'] for rune in inspiration_runes]
    stat_shards = [shard.img['alt'] for shard in stat_shards_active]

    print(f"Recommended Runes for {champion_name.capitalize()}: \n")

    print(f"Primary Tree : {primary_tree_name}\n ")
    print("Primary Runes:")
    for rune in list(dict.fromkeys(primary_runes)):
        print(rune.replace('The Rune', '').replace("The Keystone",'').strip())

    print(f"\nSecondary Tree : {secondary_tree_name}\n")
    print("Secondary Runes:")
    for rune in list(dict.fromkeys(secondary_runes)):
        print(rune.replace('The Rune', '').strip())

    print("\nStat Shards:")
    for shard in list(dict.fromkeys(stat_shards)):
        print(shard.replace('The','').replace('Shard', '').strip())

def get_champion_recommended_spells(champion_name):
    # HTML content of the div
    div_content = extract_div_html(f'https://u.gg/lol/champions/{champion_name.lower()}/build', 'content-section_content summoner-spells')

    # Create a BeautifulSoup object to parse the HTML
    soup = BeautifulSoup(div_content, 'html.parser')

    # Find the div that contains the summoner spells
    summoner_spells_div = soup.find('div', class_='content-section_content summoner-spells')

    # Extract the summoner spell images and get their alt attributes
    summoner_spell_images = summoner_spells_div.find_all('img')
    summoner_spell_names = [img['alt'] for img in summoner_spell_images]

    # Print the summoner spell names
    for spell_name in summoner_spell_names:
        print(spell_name.replace('Summoner Spell', '').strip())

def get_champion_recommended_build(champion_name):
    
    html = extract_a_html(f'https://www.leagueofgraphs.com/champions/builds/{champion_name.lower()}', f'/champions/items/{champion_name.lower()}')
    
    soup = BeautifulSoup(html, 'html.parser')
    item_divs = soup.find_all('div', class_='iconsRow')
    
    print(f"\nRecommended Build for {champion_name.capitalize()}: \n")
    
    for item_div in item_divs:
        items = item_div.find_all('img')
        names = [item['alt'] for item in items]

        
        if 'Starting Build' in item_div.parent.get_text():
            print("Starter Items:")
            for name in names:
                print(name)
            print()
        elif 'Core Build' in item_div.parent.get_text():
            print("Core Build:")
            for name in names:
                print(name)
            print()
        elif 'Boots' in item_div.parent.get_text():
            print("Boots:")
            for name in names:
                print(name)
            print()
        elif 'End Build' in item_div.parent.get_text():
            print("Final Build:")
            for name in names:
                print(name)
            print()

def get_champion_rotation():
    url = f'https://euw1.api.riotgames.com/lol/platform/v3/champion-rotations?api_key={API_KEY}'

    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3'
    }
    

    try:
        response = requests.get(url, headers=headers)
        response.raise_for_status()
        rotation_data = response.json()

        return rotation_data['freeChampionIds']

    except requests.exceptions.HTTPError as err:
        print(f"HTTP error occurred: {err}")
    except requests.exceptions.RequestException as err:
        print(f"Error occurred: {err}")

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
    except requests.exceptions.RequestException as err:
        print(f"Error occurred: {err}")

def get_champion_info_by_name(champion_name):
    champion_name = champion_name.capitalize()
    url = f'https://ddragon.leagueoflegends.com/cdn/{VERSION}/data/en_US/champion/{champion_name}.json'

    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3'
    }
    

    try:
        response = requests.get(url, headers=headers)
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

    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3'
    }
    

    try:
        response = requests.get(url, headers=headers)
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

    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3'
    }
    

    try:
        response = requests.get(url, headers=headers)
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

    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3'
    }
    

    try:
        response = requests.get(url, headers=headers)
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

    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3'
    }
    

    try:
        response = requests.get(url, headers=headers)
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

    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3'
    }
    

    try:
        response = requests.get(url, headers=headers)
        response.raise_for_status()
        return url

    except requests.exceptions.HTTPError as err:
        print(f"HTTP error occurred: {err}")
    except requests.exceptions.RequestException as err:
        print(f"Error occurred: {err}")

def get_champion_skin_splash_art(champion_name, skin_number):
    champion_name = champion_name.capitalize()
    url = f'https://ddragon.leagueoflegends.com/cdn/img/champion/splash/{champion_name}_{skin_number}.jpg'

    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3'
    }
    

    try:
        response = requests.get(url, headers=headers)
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
    print("8. Get a champion's current stats")
    print("9. Get a champion's counters")
    print("10. Get a champion's recommended runes")
    print("11. Get a champion's recommended spells")
    print("12. Get a champion's recommended build")
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

    elif choice == '8':
        champion_name = input("Enter a champion name: ")
        champion_tier = get_champion_tier(champion_name)
        champion_winrate = get_champion_winrate(champion_name)
        champion_pickrate = get_champion_pickrate(champion_name)
        champion_banrate = get_champion_banrate(champion_name)

        if champion_winrate:
            print(f"Tier: {champion_tier}")
            print(f"Win rate: {champion_winrate}")
            print(f"Pick rate: {champion_pickrate}")
            print(f"Ban rate: {champion_banrate}")

        else:
            print("Champion not found.")

    elif choice == '9':
        champion_name = input("Enter a champion name: ")
        get_champion_counters(champion_name)

    elif choice == '10': 
        champion_name = input("Enter a champion name: ")
        get_champion_recommended_runes(champion_name)

    elif choice == '11':
        champion_name = input("Enter a champion name: ")
        get_champion_recommended_spells(champion_name)

    elif choice == '12':
        champion_name = input("Enter a champion name: ")
        get_champion_recommended_build(champion_name)

    else:
        print("Invalid choice.")


if __name__ == '__main__':
    main()

