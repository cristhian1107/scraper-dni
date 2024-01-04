import requests
from bs4 import BeautifulSoup


def SearchDNI(dni):
    """ Search for basic information about the person on the web according
        to the peruvian identity document.
    """
    uri_dni = 'https://eldni.com/pe/buscar-datos-por-dni'
    get_headers = {
        'User-Agent':   "Mozilla/5.0 (Windows NT 10.0; Win64; x64) "
                        "AppleWebKit/537.36 (KHTML, like Gecko) "
                        "Chrome/107.0.0.0 Safari/537.36"
    }
    get_response = requests.get(uri_dni, headers=get_headers)
    if get_response.status_code == 200:
        print(get_response.cookies)
        # Parsing the target web page with Beautiful Soup.
        get_soup = BeautifulSoup(get_response.text, 'html.parser')
        # Get hidden token.
        token = get_soup.find('input', {'name': '_token'}).get('value')
        # Request POST.
        post_json = {
            '_token': token,
            'dni': dni
        }
        post_headers = {
            'User-Agent': "Mozilla/5.0 (Windows NT 10.0; Win64; x64) "
                          "AppleWebKit/537.36 (KHTML, like Gecko) "
                          "Chrome/107.0.0.0 Safari/537.36",
            'Host': "eldni.com",
            'Origin': "https://eldni.com",
            'Referer': "https://eldni.com/pe/buscar-por-dni",
            'Sec-Ch-Ua': "\"Not A;Brand\";v=\"8\", "
                         "\"Chromium\";v=\"120\", "
                         "\"Google Chrome\";v=\"120\"",
            'Sec-Ch-Ua-Mobile': "?0",
            'Sec-Ch-Ua-Platform': "\"Windows\"",
            'Sec-Fetch-Dest': "document",
            'Sec-Fetch-Mode': "navigate",
            'Sec-Fetch-Site': "same-origin",
            'Sec-Fetch-User': "?1",
            'Upgrade-Insecure-Requests': "1"
        }
        print(post_headers)
        post_response = requests.post(
            url=uri_dni,
            json=post_json,
            headers=post_headers
        )
        print(post_response.status_code)
    else:
        print('Error page')


if __name__ == "__main__":
    SearchDNI('72809924')
