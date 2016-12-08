" A module which provides a class for retrieving, storing and representing information about movies

import webbrowser

class Movie():
    """...Docstring..."""
    def __init__(self, movie_title, movie_storyline,
                 poster_image, trailer_youtube):
        """[Docstring about the init, typically what the input arguments do]"""

        self.title = movie_title
        self.storyline = movie_storyline
        self.poster_image_url = poster_image
        self.trailer_youtube_url = trailer_youtube

    def show_trailer(self):
        webbrowser.open(self.trailer_youtube_url)
    
print Movie.__doc__
"...Docstring..."

print Movie.__init__.__doc__
"[Docstring about the init]"
