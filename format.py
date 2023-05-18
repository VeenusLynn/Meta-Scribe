import json
import requests
import os
from urllib.parse import urlparse

def save_json_in_readable_format(json_url):
    response = requests.get(json_url)
    data = response.json()

    # Extract the champion name from the URL
    parsed_url = urlparse(json_url)
    filename = os.path.basename(parsed_url.path)
    champion_name = os.path.splitext(filename)[-2]

    output_file_path = f'{champion_name}.json'

    with open(output_file_path, 'w') as output_file:
        json.dump(data, output_file, indent=4)

# Provide the URL of the JSON file
json_url = 'https://ddragon.leagueoflegends.com/cdn/13.9.1/data/en_US/item.json'

save_json_in_readable_format(json_url)
