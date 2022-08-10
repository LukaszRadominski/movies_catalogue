import requests
import os

API_TOKEN = os.environ.get("TMDB_API_TOKEN", "")

# funkcja, która pobierze dane o najpopularniejszych filmach
# nalezy stworzyć osobny plik, w którym będziemy przechowywać cały kod odpowiedzialny za komunikację z API : tmdb_client.py

# JEDNO ZAPYTANIE DO API (z modułu 9,1) do comitu "Add test picture size" włącznie  , funkcja call_tmdb_api nie występowała, a każra inne funkcja pobierała dane zamodzielnie z  oddzielnych API
# po wprowadzeniu call_tmdb_api w commicie "Add one api call", poniższe funkcje sa mjuż uproszczone hgdyz sięgają do  call_tmdb_api

def call_tmdb_api(endpoint):
   full_url = f"https://api.themoviedb.org/3/{endpoint}"
   headers = {
       "Authorization": f"Bearer {API_TOKEN}"
   }
   response = requests.get(full_url, headers=headers)
   response.raise_for_status()
   return response.json()


def get_popular_movies(): # funkcja która zwraca pełną listę popularnych filmów 
    # endpoint = "https://api.themoviedb.org/3/movie/popular"  # adres używany do wysyłania zapytania GET na adres ...
    # headers = {
    #    "Authorization": f"Bearer {API_TOKEN}"
    # }                                           # nagówek Authorization występujący w każdym zapytaniu 
    # response = requests.get(endpoint, headers=headers)
    # return response.json()
    
    ## POWYŻEJ wersja przed uproszczeniem  PONIŻEJ wersja po uproszczeniu o funkcję call_tmdb_api
    return call_tmdb_api(f"movie/popular")
 

def get_movies_list(list_type):
    # endpoint = f"https://api.themoviedb.org/3/movie/{list_type}"
    # headers = {
    #    "Authorization": f"Bearer {API_TOKEN}"
    # }
    # response = requests.get(endpoint, headers=headers)
    # response.raise_for_status() # jeśli odpowiedź od API zakończy się czymkolwiek innym niż sukcesem – aplikacja zwróci wyjątek. Dzięki temu możemy mieć pewność, że operujemy tylko i wyłącznie na poprawnych danych pobranych z API
    # return response.json()
    
    ## POWYŻEJ wersja przed uproszczeniem  PONIŻEJ wersja po uproszczeniu o funkcję call_tmdb_api
    return call_tmdb_api(f"movie/{list_type}")


# poniżej funkcja do tworzenia adresu do obrazka; adres  składa się z 3 elementów:
    # 1/ base_url - adres bazowy ( pochodzi z https://developers.themoviedb.org/3/configuration/get-api-configuration), 
    # 2/ size - podawany  jako zmienna w funkcji 
    # 3/ file_path ( tu jest "poster_api_path" - opis dalej ) - ścieżka do pliku (  "poster_path": "/9Gtg2DzBhmYamXBS1hKAhiwbBKS.jpg"< podawana jest w JSON - który ściągany jest pezez def get_popular_movies(): - 


def get_poster_url(poster_api_path, size="w342"): ### funkcja, która potrafi stworzyć działający adres do obrazka # MOJE UWAGI: podczas wywoływania funkcji podawany jest tylko argument "poster_api_path" - reszta jest juz w funkcji
    base_url = "https://image.tmdb.org/t/p/"
    return f"{base_url}{size}/{poster_api_path}"


# wykorzystywane w main.py > aby funkcja odpowiedzialna za stronę główną, jedynie pobierała odpowiednią liczbę filmów, którą chcemy pokazać
def get_movies(how_many,list_type):  
    # data = get_popular_movies()
    data = get_movies_list('popular' if list_type is None else list_type) # zamiast get_popular_movies() > do zmiennej data przekazywany jest wynik funkcji get_movies_list (czyli filmy wg API "popular" albo "top_rated" albo "upcoming" albo "now_playing" <czyli rożne typy list dostępnych w testowanych API>, w zalezności od tego co jest przekazywane jako parametr funkcji (obecnie "popular" jeżeli list_type nie istnieje  a jeżeli listy type_istnieje wówczas wartość zmiennej list_type jest przekazywana))
    # print("abc",flush=True)
    #print(data,flush=True)
    return data["results"][:how_many] # wywołanie ze słownika  zagnieżdżonego  za pomocą metody: nazwa zmiennej['nazwa klucza'][nr indeksu w  LIŚCIE obiektów]

def get_single_movie(movie_id):
    # endpoint = f"https://api.themoviedb.org/3/movie/{movie_id}"
    # headers = {
    #    "Authorization": f"Bearer {API_TOKEN}"
    # }
    # response = requests.get(endpoint, headers=headers)
    # return response.json()

    ## POWYŻEJ wersja przed uproszczeniem  PONIŻEJ wersja po uproszczeniu o funkcję call_tmdb_api
    return call_tmdb_api(f"movie/{movie_id}")

def get_single_movie_cast(movie_id):
    endpoint = f"https://api.themoviedb.org/3/movie/{movie_id}/credits"
    headers = {
      "Authorization": f"Bearer {API_TOKEN}"
    }
    response = requests.get(endpoint, headers=headers)
    return response.json()["cast"] 

    ## POWYŻEJ wersja przed uproszczeniem  PONIŻEJ wersja po uproszczeniu o funkcję call_tmdb_api
    # return call_tmdb_api(f"movie/{movie_id}/credits")  


def get_movie_images(movie_id):
    # endpoint = f"https://api.themoviedb.org/3/movie/{movie_id}/images"
    # headers = {
    #    "Authorization": f"Bearer {API_TOKEN}"
    # }
    # response = requests.get(endpoint, headers=headers)
    # return response.json()    
    
    ## POWYŻEJ wersja przed uproszczeniem  PONIŻEJ wersja po uproszczeniu o funkcję call_tmdb_api
    return call_tmdb_api(f"movie/{movie_id}/images")  