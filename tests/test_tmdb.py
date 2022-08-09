# import tmdb_client, pytest
import os
import tmdb_client 
from unittest.mock import Mock

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

###  poniżej testy przy użyciu Mock() i monkeypath
# test 1 
def some_function_to_mock():
   raise Exception("Original was called")

def test_mocking(monkeypatch):  # Po pierwsze nasz test zyskał nowy parametr monkeypatch, wykorzystaliśmy w ten sposób wbudowany w pytest mechanizm fixtures. Taki zapis będzie działał jedynie w obrębie testów pisanych z użyciem tej biblioteki. # taki zapis  traktujemy jako "sprytny import" – definiujemy, że nasz test wymaga kodu fixture o nazwie monkeypatch, a pytest to wykryje i uruchomi funkcję testującą z odpowiednim parametrem.
   my_mock = Mock() # Następnie tworzymy obiekt klasy Mock() z modułu unittest.mock, który służy do "udawania" zachowań innych obiektów. Dzięki bardzo elastycznej konfiguracji można łatwo symulować oczekiwane zachowania w kodzie testowym. Mock() będzie tak naprawdę wszystkim, czym chcemy.
   my_mock.return_value = 2 # W naszym przypadku przysłonimy całą funkcję przy pomocy naszego obiektu Mock, więc ustawiamy mu pole return_value na wartość, której oczekujemy.  ## Jeśli wywołamy mock jak funkcję, to zostanie zawsze zwrócona zawartość pola return_value. Domyślnie jest ona ustawiona na nowy obiekt Mock().
   monkeypatch.setattr("tests.test_tmdb.some_function_to_mock", my_mock) # Ostatnia nowość to wywołanie monkeypatch.setattr() – ten fragment jest najważniejszy z punktu widzenia naszych testów. To on odpowiada za finalne przesłonięcie obiektu innym. Funkcja setattr() jako pierwszy argument przyjmuje dokładną ścieżkę do obiektu, który ma zostać przysłonięty. Drugim argumentem natomiast jest obiekt, którym przysłaniamy.
   result = some_function_to_mock()
   assert result == 2
   # Spróbuj teraz uruchomić testy przy pomocy pytest i przekonaj się, czy zobaczysz wyjątek. Jeśli testy przejdą pomyślnie — oznacza to, że przesłanianie obiektów z użyciem Mock zadziałało.

# test 2 
def test_get_movies_list(monkeypatch):
   # Lista, która będzie zwracać przysłonięte "zapytanie do API"
   mock_movies_list = ['Movie 1', 'Movie 2']

   requests_mock = Mock()
   # Wynik wywołania zapytania do API
   response = requests_mock.return_value
   # Przysłaniamy wynik wywołania metody .json()
   response.json.return_value = mock_movies_list # Nadpisujemy metodę .json() i ustawiamy jej zwracaną wartość jako wcześniej zdefiniowaną listę. # W ten sposób możesz przesłaniać zachowania metod, które są wywoływane na obiekcie Mock().
   monkeypatch.setattr("tmdb_client.requests.get", requests_mock)


   movies_list = tmdb_client.get_movies_list(list_type="popular")
   assert movies_list == mock_movies_list