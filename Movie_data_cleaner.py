raw_movies = [
    {"title": "  dark  ", "rating": 8.8},
    {"title": "inception", "rating": 7.5},
    {"title": "  INTERSTELLAR", "rating": 9.2},
    {"title": "tenet", "rating": 6.5}
]

def format_movie_name(clean_name):
    cleaned=clean_name.strip().title()
    return cleaned

filtered_movies=[]

for movie in raw_movies:
    rating=movie["rating"]
    if rating>8.0:
        filtered_movies.append(rating)

        raw_name=movie["title"]
        formatted=format_movie_name(raw_name)
        filtered_movies.append(formatted)


print("Filetred movies:", filtered_movies)

