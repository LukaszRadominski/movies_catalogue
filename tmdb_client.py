import requests

API_TOKEN = "eyJhbGciOiJIUzI1NiJ9.eyJhdWQiOiIwYjgwZTc0OWVhZGI5YjA0NDQ0MTYxYTVlMmMxY2UxZSIsInN1YiI6IjYyOTA4Y2M5ZWQyYWMyMTZiOTAyOTlkYiIsInNjb3BlcyI6WyJhcGlfcmVhZCJdLCJ2ZXJzaW9uIjoxfQ.AqfzLL-wtdgqzIfh5AjyZvIi7b8yrl7B1MOEyGqJFW8"

# funkcja, która pobierze dane o najpopularniejszych filmach
# nalezy stworzyć osobny plik, w którym będziemy przechowywać cały kod odpowiedzialny za komunikację z API : tmdb_client.py

def get_popular_movies(): # funkcja która zwraca pełną listę popularnych filmów 
    endpoint = "https://api.themoviedb.org/3/movie/popular"  # adres używany do wysyłania zapytania GET na adres ...
    headers = {
        "Authorization": f"Bearer {API_TOKEN}"
    }                                           # nagówek Authorization występujący w każdym zapytaniu 
    response = requests.get(endpoint, headers=headers)
    return response.json()
 

def get_movies_list(list_type):
    endpoint = f"https://api.themoviedb.org/3/movie/{list_type}"
    headers = {
        "Authorization": f"Bearer {API_TOKEN}"
    }
    response = requests.get(endpoint, headers=headers)
    response.raise_for_status() # eśli odpowiedź od API zakończy się czymkolwiek innym niż sukcesem – aplikacja zwróci wyjątek. Dzięki temu możemy mieć pewność, że operujemy tylko i wyłącznie na poprawnych danych pobranych z API
    return response.json()

# poniżej funkcja do tworzenia adresu do obrazka; adres  składa się z 3 elementów:
    # 1/ base_url - adres bazowy ( pochodzi z https://developers.themoviedb.org/3/configuration/get-api-configuration), 
    # 2/ size - podawany  jako zmienna w funkcji 
    # 3/ file_path ( tu jest "poster_api_path" - opis dalej ) - ścieżka do pliku (  "poster_path": "/9Gtg2DzBhmYamXBS1hKAhiwbBKS.jpg"< podawana jest w JSON - który ściągany jest pezez def get_popular_movies(): - 


def get_poster_url(poster_api_path, size="w342"): ### funkcja, która potrafi stworzyć działający adres do obrazka # MOJE UWAGI: podczas wywoływania funkcji podawany jest tylko argument "poster_api_path" - reszta jest juz w funkcji
    base_url = "https://image.tmdb.org/t/p/"
    return f"{base_url}{size}/{poster_api_path}"


# wykorzystywane w main.py > aby funkcja odpowiedzialna za stronę główną, jedynie pobierała odpowiednią liczbę filmów, którą chcemy pokazać
def get_movies(how_many):  
    # data = get_popular_movies()
    data = get_movies_list("popular") # zamiast get_popular_movies() > do zmiennej data przekazywany jest wynik funkcji get_movies_list (czyli filmy wg API "popular" albo "top_rated" albo "upcoming" albo "now_playing" <czyli rożne typy list dostępnych w testowanych API>, w zalezności od tego co jest przekazywane jako parametr funkcji (obecnie "popular"))
    print("abc",flush=True)
    # print(data,flush=True)
    return data["results"][:how_many] # wywołanie ze słownika  zagnieżdżonego  za pomocą metody: nazwa zmiennej['nazwa klucza'][nr indeksu w  LIŚCIE obiektów]

def get_single_movie(movie_id):
    endpoint = f"https://api.themoviedb.org/3/movie/{movie_id}"
    headers = {
        "Authorization": f"Bearer {API_TOKEN}"
    }
    response = requests.get(endpoint, headers=headers)
    return response.json()

def get_single_movie_cast(movie_id):
    endpoint = f"https://api.themoviedb.org/3/movie/{movie_id}/credits"
    headers = {
        "Authorization": f"Bearer {API_TOKEN}"
    }
    response = requests.get(endpoint, headers=headers)
    return response.json()["cast"]   


def get_movie_images(movie_id):
    endpoint = f"https://api.themoviedb.org/3/movie/{movie_id}/images"
    headers = {
        "Authorization": f"Bearer {API_TOKEN}"
    }
    response = requests.get(endpoint, headers=headers)
    return response.json()    