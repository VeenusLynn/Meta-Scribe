import requests
from bs4 import BeautifulSoup

def extract_div_html(url, div_class):
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3'
    }
    
    try:
        # Send a GET request to the URL
        response = requests.get(url, headers=headers)
        
        # Check if the request was successful
        if response.status_code == 200:
            # Create a BeautifulSoup object for parsing the HTML
            soup = BeautifulSoup(response.content, 'lxml')
            
            # Find the div with the specified class name
            target_div = soup.find('div', class_=div_class)
            
            # Check if the div exists
            if target_div:
                # Process the extracted data without storing the entire HTML code
                # For example, you can extract specific data or perform other operations
                # directly on the 'target_div' object.

                return str(target_div)
                
            else:
                print(f"Div with class '{div_class}' not found.")
        
        else:
            print(f"Request failed with status code {response.status_code}.")
    
    except requests.exceptions.RequestException as e:
        print(f"Request failed with an exception: {e}")
    
    return None
