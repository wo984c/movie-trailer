import webbrowser
class Movie():
    """The Movie class is used to store movie related information.

     Attributes:
        title: A string to store the movie's title
        poster_image_url: A string to store the url of movie's poster image.
        trailer_youtube_url: A string to store the trailer's URL. """
     
    def __init__(self, movie_title, poster_image, trailer_youtube):
        self.title = movie_title
        self.poster_image_url = poster_image
        self.trailer_youtube_url = trailer_youtube

    def show_trailer(self):
        webbrowser.open(self.trailer_youtube_url)
