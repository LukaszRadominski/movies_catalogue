import requests

# funkcja, która pobierze dane o najpopularniejszych filmach
# nalezy stworzyć osobny plik, w którym będziemy przechowywać cały kod odpowiedzialny za komunikację z API : tmdb_client.py

def get_popular_movies(): 
    endpoint = "https://api.themoviedb.org/3/movie/popular"  # wysyłanie zapytania GET na adres ...
    api_token = "0b80e749eadb9b04444161a5e2c1ce1e" # wysyłanie klucza autoryzujacego  ......
    headers = {
        "Authorization": f"Bearer {api_token}"
    }
    response = requests.get(endpoint, headers=headers)
    return response.json()

# poniżej funkcja do tworzenia adresu do obrazka; adres  składa się z 3 elementów:
    # 1/ base_url - adres bazowy ( pochodzi z https://developers.themoviedb.org/3/configuration/get-api-configuration), 
    # 2/ size - podawany  jako zmienna w funkcji 
    # 3/ file_path ( tu jest "poster_api_path" - opis dalej ) - ścieżka do pliku (  "poster_path": "/9Gtg2DzBhmYamXBS1hKAhiwbBKS.jpg"< podawana jest w JSON - który ściągany jest pezez def get_popular_movies(): - 


def get_poster_url(poster_api_path, size="w342"): 
    base_url = "https://image.tmdb.org/t/p/"
    return f"{base_url}{size}/{poster_api_path}"
