import requests
from bs4 import BeautifulSoup


def print_champion_banrate(champion_name):
    url = f"https://u.gg/lol/champions/{champion_name}/build?rank=overall"

    # Set custom headers to mimic a web browser
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3"
    }

    # Send an HTTP GET request to the u.gg champion build page with custom headers
    response = requests.get(url, headers=headers)

    # Check if the request was successful
    if response.status_code == 200:
        # Parse the HTML content using BeautifulSoup
        soup = BeautifulSoup(response.content, "html.parser")

        # Find the elements containing the pick rate
        ban_rate_element = soup.find("div", {"class": "ban-rate"})

        # Extract the text from the element
        ban_rate = ban_rate_element.text.strip()

        if ban_rate_element:
            # Extract the text from the element and add a space after the percentage sign
            ban_rate = (
                ban_rate_element.text.strip().replace("%", "% ").replace("Ban Rate", "")
            )

            if ban_rate:
                return ban_rate
            else:
                print("Champion not found.")
                
    else:
        # Request was unsuccessful
        print(f"Failed to retrieve ban rate. Status code: {response.status_code}")


# "ban rate: {ban_rate}"