from flask import Flask, render_template
import tmdb_client

app = Flask(__name__)

@app.route('/')
def homepage():
    movies = tmdb_client.get_movies(8) # maksymalnie 8 filmów
    return render_template("homepage.html", movies=movies) # wyświetla szablon html, w którym zmienna movies przejmuje argumenty zmiennej movies z main.py


# pozwala on na wstrzyknięcie do kontekstu każdego szablonu dodatkowych danych lub obiektów, by nie robić tego za każdym razem w widoku
# Teraz każdy szablon będzie miał dostępny obiekt o nazwie tmdb_image_url, czyli funkcję, która przyjmuje dwa parametry: path oraz size.
@app.context_processor
def utility_processor():
    def tmdb_image_url(path, size):
        return tmdb_client.get_poster_url(path, size)
    return {"tmdb_image_url": tmdb_image_url}  # dekorator context proessor zwraca słownik w którym tmdb_image_url to key a wartośc jest funkcją tmdb_image_url



# moja funkcja ..................
def get_movie_info():
    movies =  tmdb_client.get_popular_movies["results"][:8]
    for titles_dict in movies: 
        keys = ["title", "backdrop_path"]
        dict2 = {x:titles_dict[x] for x in keys}
        return dict2


if __name__ == '__main__':
    app.run(debug=True)