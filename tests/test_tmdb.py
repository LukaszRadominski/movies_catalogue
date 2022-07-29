# import tmdb_client, pytest

from movies_catalogue import tmdb_client 

def test_get_poster_url_uses_default_size(): # test: czy funkcja używa domyślnego rozmiaru zdjęcia
   # Przygotowanie danych
   poster_api_path = "some-poster-path"
   expected_default_size = 'w342'
   # Wywołanie kodu, który testujemy
   poster_url = tmdb_client.get_poster_url(poster_api_path=poster_api_path)
   # Porównanie wyników
   assert expected_default_size in poster_url  # czy domyślny rozmiar, którego oczekujemy, znajduje się w zwróconym adresie URL


def test_get_movies_list_type_popular(): # test pobierania danych z API TheMovieDB >> czy dane zostały pobrane 
   movies_list = tmdb_client.get_movies_list(list_type="popular")
   assert movies_list is not None