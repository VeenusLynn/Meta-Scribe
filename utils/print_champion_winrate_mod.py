import requests
from bs4 import BeautifulSoup


def print_champion_winrate(champion_name):
    url = f"https://u.gg/lol/champions/{champion_name}/build"

    # Set custom headers to mimic a web browser
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3"
    }

    # Send an HTTP GET request to the u.gg Irelia build page with custom headers
    response = requests.get(url, headers=headers)

    # Check if the request was successful
    if response.status_code == 200:
        # Parse the HTML content using BeautifulSoup
        soup = BeautifulSoup(response.content, "html.parser")

        # Find the elements containing the win rate
        win_rate_element = soup.find("span", {"class": "win-rate"})

        # Extract the text from the elements
        win_rate = win_rate_element.text.strip()

        if win_rate_element:
            # Extract the text from the element and add a space after the percentage sign
            win_rate = win_rate_element.text.strip().replace("WR", "")

            if win_rate:
                print(f"Win rate: {win_rate}")
            else:
                print("Champion not found.")
    else:
        # Request was unsuccessful
        print(f"Failed to retrieve winrate. Status code: {response.status_code}")
        return None
