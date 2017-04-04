import media
import fresh_tomatoes
import operator

# Creating the instances of the class Movie to store the movie's title,
# poster image, and trailer URL.

kong = media.Movie("Kong: Skull Island",
                   "https://upload.wikimedia.org/wikipedia/en/3/34/Kong_Skull_Island_poster.jpg",  # NOQA
                   "https://youtu.be/GfhcFf0voRU")

avatar = media.Movie("Avatar",
                     "https://upload.wikimedia.org/wikipedia/en/b/b0/Avatar-Teaser-Poster.jpg",  # NOQA
                     "https://youtu.be/5PSNL1qE6VY")

matrix = media.Movie("The Matrix",
                     "https://upload.wikimedia.org/wikipedia/en/c/c1/The_Matrix_Poster.jpg",  # NOQA
                     "https://youtu.be/8Qd89ZuCd-0")

jwick = media.Movie("John Wick",
                     "https://upload.wikimedia.org/wikipedia/en/9/98/John_Wick_TeaserPoster.jpg",  # NOQA
                     "https://youtu.be/2AUmvWm5ZDQ")

shrek = media.Movie("Shrek",
                     "https://upload.wikimedia.org/wikipedia/en/3/39/Shrek.jpg",  # NOQA
                     "https://youtu.be/7t6W80lZ1Ss")

swfish = media.Movie("Swordfish",
                     "https://upload.wikimedia.org/wikipedia/en/e/e8/Swordfish_movie.jpg",  # NOQA
                     "https://youtu.be/mfLizCqjz18")

# Generate the list of movie objects sorted by the title attribute.
# Then call fresh_tomatoes module to generate the html with my
# favorite movies.

movies = [kong, avatar, matrix, jwick, shrek, swfish]
sorted_movies = sorted(movies, key=operator.attrgetter('title'))
fresh_tomatoes.open_movies_page(sorted_movies)
