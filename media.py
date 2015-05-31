class Movie:
    """Stores information about a given movie.

    Attributes:
        title: Title of the Movie.
        trailer_youtube_url: url of the movie trailer on youtube.
        poster_image_url: url of a poster of the movie.
        description: a short description of the movie
    """

    def __init__(self, title, trailer_youtube_url, poster_image_url, description):
    """Instantiates a movie object.
    """
        self.title = title
        self.trailer_youtube_url = trailer_youtube_url
        self.poster_image_url = poster_image_url
        self.description = description
