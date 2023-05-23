import requests
from bs4 import BeautifulSoup


def extract_a_html(url, target_href):

    try:
        headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3'
        }

        # Send a GET request to the URL
        response = requests.get(url, headers=headers)

        # Check if the request was successful
        if response.status_code == 200:
            # Get the HTML content of the page
            html_content = response.text

            # Create a BeautifulSoup object for parsing the HTML
            soup = BeautifulSoup(html_content, 'html.parser')

            # Find all <a> tags with the specified href
            target_a_tags = soup.find_all('a', href=target_href)

            # Check if any <a> tags exist
            if target_a_tags:
                # Concatenate the HTML codes of the <a> tags
                a_html = ''.join(str(a_tag) for a_tag in target_a_tags)

                # Return the concatenated <a> tag HTML codes
                return a_html

            else:
                print(f"No <a> tags found with href '{target_href}'.")
                return None

        else:
            print(f"Request failed with status code {response.status_code}.")
            return None
    
    except:
        return None
