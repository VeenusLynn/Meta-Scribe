import requests
from bs4 import BeautifulSoup

def extract_div_html(url, div_class):

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
        
        # Find the div with the specified class name
        target_div = soup.find('div', class_=div_class)
        
        # Check if the div exists
        if target_div:
            # Get the HTML code of the div
            div_html = str(target_div)
            
            # Return the div HTML
            return div_html
        
        else:
            print(f"Div with class '{div_class}' not found.")
            return None
    
    else:
        print(f"Request failed with status code {response.status_code}.")
        return None
    
    return None