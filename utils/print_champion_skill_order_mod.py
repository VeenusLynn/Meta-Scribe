from bs4 import BeautifulSoup
from .extract_div_html_mod import extract_div_html


def print_champion_skill_order(champion_name):

    try:
        html = extract_div_html(f'https://u.gg/lol/champions/{champion_name.lower()}/build?rank=overall', 'skill-path-container')

        soup = BeautifulSoup(html, 'html.parser')
        skill_order_rows = soup.find_all(class_='skill-order-row')

        skill_order = []

        for row in skill_order_rows:
            skill_label = row.find(class_='skill-label').text.strip()
            skill_name = row.find(class_='skill-name').text.strip()
            skill_levels = [int(div.text.strip()) if div.text.strip() != '' else 0 for div in row.find_all('div', class_='skill-up')]

            skill_order.append({
                'skill_label': skill_label,
                'skill_name': skill_name,
                'skill_levels': skill_levels
            })

        return skill_order
    
    except:
        print("Champion not found.")
        return None

