import requests


def print_champion_skin_splash_art(champion_name, skin_number):
    champion_name = champion_name.capitalize()
    url = f"https://ddragon.leagueoflegends.com/cdn/img/champion/splash/{champion_name}_{skin_number}.jpg"

    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3"
    }

    try:
        response = requests.get(url, headers=headers)
        response.raise_for_status()

        champion_skin_splash_art = url          

        if champion_skin_splash_art:
            print(f"Splash art: {champion_skin_splash_art}")
        else:
            print("Skin not found.")

    except requests.exceptions.HTTPError as err:
        print(f"HTTP error occurred: {err}")
    except requests.exceptions.RequestException as err:
        print(f"Error occurred: {err}")