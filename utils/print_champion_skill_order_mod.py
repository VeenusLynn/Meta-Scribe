from bs4 import BeautifulSoup
from .extract_div_html_mod import extract_div_html


def print_champion_skill_order(champion_name):

    html = extract_div_html(f'https://u.gg/lol/champions/{champion_name.lower()}/build?rank=overall', 'skill-path-container')

    soup = BeautifulSoup(html, 'html.parser')
    skill_order_rows = soup.find_all(class_='skill-order-row')

    return skill_order_rows

    # print(f"Recommended Skill Order for {champion_name.capitalize()}: \n")

    # for row in skill_order_rows:
    #     skill_label = row.find(class_='skill-label').text.strip()
    #     skill_name = row.find(class_='skill-name').text.strip()
    #     skill_levels = [int(div.text.strip()) if div.text.strip() != '' else 0 for div in row.find_all('div', class_='skill-up')]

    #     print(f"Skill: {skill_label}")
    #     print(f"Name: {skill_name}")
    #     print("Levels:", end=' ')
    #     for level in skill_levels:
    #         print(level, end=' ')
    #     print("\n")