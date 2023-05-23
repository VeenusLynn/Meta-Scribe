import requests
from bs4 import BeautifulSoup


def print_champion_pickrate(champion_name):
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
        pick_rate_element = soup.find("div", {"class": "pick-rate"})

        # Extract the text from the element
        pick_rate = pick_rate_element.text.strip()

        if pick_rate_element:
            # Extract the text from the element and add a space after the percentage sign
            pick_rate = (
                pick_rate_element.text.strip()
                .replace("%", "% ")
                .replace("Pick Rate", "")
            )

            if pick_rate:
                return pick_rate
            else:
                print("Champion not found.")
    else:
        # Request was unsuccessful
        print(f"Failed to retrieve pick rate. Status code: {response.status_code}")


# "pick rate: {pick_rate}"