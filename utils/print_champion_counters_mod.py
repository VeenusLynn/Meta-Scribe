from bs4 import BeautifulSoup
from .extract_div_html_mod import extract_div_html



def print_champion_counters(champion_name):

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