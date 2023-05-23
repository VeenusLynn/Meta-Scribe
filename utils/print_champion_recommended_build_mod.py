from bs4 import BeautifulSoup
from .extract_a_html_mod import extract_a_html


def print_champion_recommended_build(champion_name):
        
    try:
        html = extract_a_html(f'https://www.leagueofgraphs.com/champions/builds/{champion_name.lower()}', f'/champions/items/{champion_name.lower()}')
        
        soup = BeautifulSoup(html, 'html.parser')
        item_divs = soup.find_all('div', class_='iconsRow')
        
        starter_items = []
        core_build = []
        boots = []
        final_build = []


        for item_div in item_divs:
            items = item_div.find_all('img')
            names = [item['alt'] for item in items]

            
            if 'Starting Build' in item_div.parent.get_text():
                starter_items = names

            elif 'Core Build' in item_div.parent.get_text():
                core_build = names
            elif 'Boots' in item_div.parent.get_text():
                boots = names
            elif 'End Build' in item_div.parent.get_text():
                final_build = names
        
        return starter_items, core_build, boots, final_build

    except:
        print("Champion not found.")
        return None, None, None, None

