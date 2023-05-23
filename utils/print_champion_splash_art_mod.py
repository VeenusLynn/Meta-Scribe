import requests


def print_champion_splash_art(champion_name):
    champion_name = champion_name.capitalize()
    url = f"https://ddragon.leagueoflegends.com/cdn/img/champion/splash/{champion_name}_0.jpg"

    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3"
    }

    try:
        response = requests.get(url, headers=headers)
        response.raise_for_status()

        champion_splash_art = url

        if champion_splash_art:
            return champion_splash_art
        else:
            print("Splash art not found.")

    except requests.exceptions.HTTPError as err:
        print(f"HTTP error occurred: {err}")
    except requests.exceptions.RequestException as err:
        print(f"Error occurred: {err}")

# "Splash art: {champion_splash_art}"