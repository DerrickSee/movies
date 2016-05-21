from models import Movie
from fresh_tomatoes import open_movies_page


# My list of favorite movies represented as a list of dict
my_list = [
    {
        'title': "The Dark Knight",
        'trailer_youtube_url': "https://www.youtube.com/watch?v=EXeTwQWrcwY",
        'poster_image_url': "http://ia.media-imdb.com/images/M/MV5BMTMxNTMwOD" \
                            "M0NF5BMl5BanBnXkFtZTcwODAyMTk2Mw@@._V1_UX182_CR0" \
                            ",0,182,268_AL_.jpg"
    },
    {
        'title': "Finding Nemo",
        'trailer_youtube_url': "https://www.youtube.com/watch?v=wZdpNglLbt8",
        'poster_image_url': "http://ia.media-imdb.com/images/M/MV5BMTY1MTg1ND" \
                            "AxOV5BMl5BanBnXkFtZTcwMjg1MDI5Nw@@._V1_UX182_CR0" \
                            ",0,182,268_AL_.jpg"
    },
    {
        'title': "Before Sunset",
        'trailer_youtube_url': "https://www.youtube.com/watch?v=oI3UuneLcyU",
        'poster_image_url': "http://ia.media-imdb.com/images/M/MV5BMTQ1MjAwNT" \
                            "M5Ml5BMl5BanBnXkFtZTYwNDM0MTc3._V1_UX182_CR0,0,1" \
                            "82,268_AL_.jpg"
    },
]

def launch():
    # Creates list of movie instances by looping through my_list and using
    # Movie constructor to create Movie instance
    movies = [Movie(**m) for m in my_list]
    # Insert list into open_movies_page function from fresh_tomatoes to
    # launch page
    open_movies_page(movies)
