from bs4 import BeautifulSoup
from .extract_div_html_mod import extract_div_html


def print_champion_recommended_spells(champion_name):
        
    try:    
        # HTML content of the div
        div_content = extract_div_html(f'https://u.gg/lol/champions/{champion_name.lower()}/build?rank=overall', 'content-section_content summoner-spells')

        # Create a BeautifulSoup object to parse the HTML
        soup = BeautifulSoup(div_content, 'html.parser')

        # Find the div that contains the summoner spells
        summoner_spells_div = soup.find('div', class_='content-section_content summoner-spells')

        # Extract the summoner spell images and get their alt attributes
        summoner_spell_images = summoner_spells_div.find_all('img')
        summoner_spell_names = [img['alt'] for img in summoner_spell_images]

        return summoner_spell_names
    
    except:
        print("Champion not found.")
        return None

    # # Print the summoner spell names
    # for spell_name in summoner_spell_names:
    #     print(spell_name.replace('Summoner Spell', '').strip())

