import requests
import logging

# funkcja, która pobierze dane o najpopularniejszych filmach
# nalezy stworzyć osobny plik, w którym będziemy przechowywać cały kod odpowiedzialny za komunikację z API : tmdb_client.py

def get_popular_movies(): # funkcja która zwraca pełną listę popularnych filmów 
    endpoint = "https://api.themoviedb.org/3/movie/popular"  # adres używany do wysyłania zapytania GET na adres ...
    api_token ="eyJhbGciOiJIUzI1NiJ9.eyJhdWQiOiIwYjgwZTc0OWVhZGI5YjA0NDQ0MTYxYTVlMmMxY2UxZSIsInN1YiI6IjYyOTA4Y2M5ZWQyYWMyMTZiOTAyOTlkYiIsInNjb3BlcyI6WyJhcGlfcmVhZCJdLCJ2ZXJzaW9uIjoxfQ.AqfzLL-wtdgqzIfh5AjyZvIi7b8yrl7B1MOEyGqJFW8" # klucz autoryzacyjny przechowywany w zmiennej> dzięki temu nie trzeba podawać klucza w  URL, za każdym zapytaniem 
    headers = {
        "Authorization": f"Bearer {api_token}"
    }                                           # nagówek Authorization występujący w każdym zapytaniu 
    response = requests.get(endpoint, headers=headers)
    return response.json()

# poniżej funkcja do tworzenia adresu do obrazka; adres  składa się z 3 elementów:
    # 1/ base_url - adres bazowy ( pochodzi z https://developers.themoviedb.org/3/configuration/get-api-configuration), 
    # 2/ size - podawany  jako zmienna w funkcji 
    # 3/ file_path ( tu jest "poster_api_path" - opis dalej ) - ścieżka do pliku (  "poster_path": "/9Gtg2DzBhmYamXBS1hKAhiwbBKS.jpg"< podawana jest w JSON - który ściągany jest pezez def get_popular_movies(): - 


def get_poster_url(poster_api_path, size="w342"): ### ??? JAKIE JEST ŹRÓDŁO "poster_api_path"  ### funkcja, która potrafi stworzyć działający adres do obrazka # MOJE UWAGI: podczas wywoływania funkcji podawany jest tylko argument "poster_api_path" - reszta jest juz w funkcji
    base_url = "https://image.tmdb.org/t/p/"
    return f"{base_url}{size}/{poster_api_path}"


# wykorzystywane w main.py > aby funkcja odpowiedzialna za stronę główną, jedynie pobierała odpowiednią liczbę filmów, którą chcemy pokazać
def get_movies(how_many):  
    data = get_popular_movies()
    print("abc",flush=True)
    print(data,flush=True)
    return data["results"][:how_many]
