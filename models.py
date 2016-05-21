

class Movie():
    """
    This stores a movie's title, a trailer url from youtube and a poster image
    url.
    """
    def __init__(self, title, trailer_youtube_url, poster_image_url):
        """
        Initialize movie instance with movie title, trailer url and
        image url as parameter
        """
        self.title = title
        self.trailer_youtube_url = trailer_youtube_url
        self.poster_image_url = poster_image_url
