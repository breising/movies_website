import webbrowser

class Movie():
	"""
	Constructs an instance of a "Movie" object adding properties and methods and returns the Movie object instance.
	"""
	def __init__(self, movie_title, movie_storyline, poster_image, trailer_youtube):
		"""
		Returns an instance of a Movie object.
		Arguments contain the data for associated text strings and images: movie title, movie storyline, poster image, and trailer.
		Methods include: "show_trailer" to show the associated video trailer.
		"""
		self.title = movie_title
		self.storyline= movie_storyline
		self.poster_image_url = poster_image
		self.trailer_youtube_url = trailer_youtube
	def show_trailer(self):
		webbrowser.open(self.trailer_youtube_url)