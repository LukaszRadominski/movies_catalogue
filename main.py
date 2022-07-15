from flask import Flask, render_template, request
import tmdb_client, random

app = Flask(__name__)

@app.route('/')
def homepage():
    movies = tmdb_client.get_movies(how_many=8) # maksymalnie 8 filmów
    return render_template("homepage.html", movies=movies) # wyświetla szablon html, w którym zmienna movies przejmuje argumenty zmiennej movies z main.py

# pozwala on na wstrzyknięcie do kontekstu każdego szablonu dodatkowych danych lub obiektów, by nie robić tego za każdym razem w widoku
# Teraz każdy szablon będzie miał dostępny obiekt o nazwie tmdb_image_url, czyli funkcję, która przyjmuje dwa parametry: path oraz size.
@app.context_processor
def utility_processor():
    def tmdb_image_url(path, size):
        return tmdb_client.get_poster_url(path, size)
    return {"tmdb_image_url": tmdb_image_url}  # dekorator context proessor zwraca słownik w którym tmdb_image_url to key a wartośc jest funkcją tmdb_image_url



# moja funkcja ..................ma powstać słownik zawierający tytuł i URL do plakatu  ## iteracja przez zagnieżdżone słowniki
# # mam otrzymać {"title": "URL"} 
##??? zamiast"backdrop_path" >> "poster_path" ????? 
## ??? gdzie wykorzystać get_movie-info

def get_movie_info():
    movies_two =  tmdb_client.get_popular_movies() # otrzymuję słownik - JSON  o kluczach "page", "results", 
    results_list = movies_two.get("results") # otrzymuję listę słowników która jest value dla key results
    my_dict = {}
    for element in results_list : # dla każdego objektu (słownika) na liście 
        title = element.get("titile") # do zmiennej "title" przypisuję wartość dla klucza "title" w słowniku, który jest przechowywany w zmiennej results_list
        element_poster_path = element.get("backdrop_path") # zmienna element ... przyjmuje wartośc dka kucza "backdrop_path"
        url = tmdb_client.get_poster_url(element_poster_path) # url do obrazka to wynik funkcji get_poster z argumentem  =  zmiennej element ....
        my_dict[f'{title}'] = f'{url}' # tworzę słownik {"title": "URL"}
    return my_dict


# PRZYKŁAD inny 
# def get_movie_info():
#    movies =  tmdb_client.get_popular_movies(8)
#    for titles_dict in movies: 
#        keys = ["title", "backdrop_path"]
#        dict2 = {x:titles_dict[x] for x in keys}
#        return dict2




@app.route("/movie/<movie_id>")
def movie_details(movie_id): 
    details = tmdb_client.get_single_movie(movie_id)
    cast = tmdb_client.get_single_movie_cast(movie_id)
    movie_images = tmdb_client.get_movie_images(movie_id)
    selected_backdrop = random.choice(movie_images['backdrops'])
    return render_template("movie_details.html", movie=details, cast=cast) 

if __name__ == '__main__':
    app.run(debug=True)