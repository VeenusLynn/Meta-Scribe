import requests
from bs4 import BeautifulSoup


def print_champion_tier(champion_name):
    url = f'https://u.gg/lol/champions/{champion_name}/build?rank=overall'

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
    
# "Tier: {tier}"
    