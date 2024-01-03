import requests
from bs4 import BeautifulSoup

# Search parameters.
uri_dni = "https://eldni.com/pe/buscar-datos-por-dni"
headers = {
    'User-Agent':   "Mozilla/5.0 (Windows NT 10.0; Win64; x64) "
                    "AppleWebKit/537.36 (KHTML, like Gecko) "
                    "Chrome/107.0.0.0 Safari/537.36"
}

# Method GET.
response = requests.get(uri_dni, headers=headers)
if response.status_code == 200:
    # Parsing the target web page with Beautiful Soup.
    soup = BeautifulSoup(response.text, 'html.parser')
    token = soup.find('input', {'name': '_token'}).get('value')
    print(token)
else:
    print('Error page')
