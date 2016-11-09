import media
import fresh_tomatoes
# no comment
toy_story = media.Movie("Toy Story", 
  "A story of a boy...",
  "https://upload.wikimedia.org/wikipedia/en/1/13/Toy_Story.jpg", 
  "https://www.youtube.com/watch?v=KYz2wyBy3kc")

avatar = media.Movie("Avatar", "A story of an avatar...",
  "https://upload.wikimedia.org/wikipedia/en/b/b0/Avatar-Teaser-Poster.jpg", 
  "https://www.youtube.com/watch?v=cRdxXPV9GNQ")

shawshank = media.Movie("Shawshank Redemption",
  "The Shawshank Redemption is a 1994 American drama film written and directed by Frank Darabont, and starring Tim Robbins and Morgan Freeman. Adapted",
  "https://upload.wikimedia.org/wikipedia/en/8/81/ShawshankRedemptionMoviePoster.jpg","https://www.youtube.com/watch?v=6hB3S9bIaco")
godather = media.Movie("The Godfather",
  "The story spans the years from 1945 to 1955 and chronicles the fictional Italian-American Corleone crime family. When organized crime family patriarch Vito Corleone barely survives an attempt on his life, his youngest son, Michael, steps in to take care of the would-be killers, launching a campaign of bloody revenge","https://upload.wikimedia.org/wikipedia/en/1/1c/Godfather_ver1.jpg","https://www.youtube.com/watch?v=sY1S34973zA")
shindlerslist = media.Movie("Shindler's List",
  "Told from the perspective of businessman Oskar Schindler who saved over a thousand Jewish lives from the Nazis while they worked as slaves in his factory. Schindler’s List is based on a true story, illustrated in black and white and controversially filmed in many original locations.", 
  "https://upload.wikimedia.org/wikipedia/en/3/38/Schindler%27s_List_movie.jpg", 
  "https://www.youtube.com/watch?v=JdRGC-w9syA")

# use the object instances to create a array of objects
movies = [toy_story, avatar, shawshank, godather, shindlerslist]
#use file fresh_tomatoes to open each object/movie for display in html
fresh_tomatoes.open_movies_page(movies)