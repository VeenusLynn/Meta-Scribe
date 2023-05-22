from bs4 import BeautifulSoup
from .extract_a_html_mod import extract_a_html


def print_champion_recommended_build(champion_name):
    
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