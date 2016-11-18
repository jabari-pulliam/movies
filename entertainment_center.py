from media import *
from fresh_tomatoes import *

# Build the list of movies
movies = [Movie(movie_title="The Shawshank Redemption",
                poster_image="http://ayay.co.uk/movies/poster/classic/"
                             "the-shawshank-redemption.jpg",
                trailer_youtube="https://www.youtube.com/watch?v=NmzuHjWmXOc"),
          Movie(movie_title="Higher Learning",
                poster_image="https://images-na.ssl-images-amazon.com/"
                             "images/M/MV5BMTI1NDEwMDg4Ml5BMl5BanBnXk"
                             "FtZTcwMzY4MTgxMQ@@._V1_.jpg",
                trailer_youtube="https://www.youtube.com/watch?v=_4KVCVX1MrQ"
                ),
          Movie(movie_title="Love Jones",
                poster_image="https://images-na.ssl-images-amazon.com/images/"
                             "M/MV5BMTY2NjYxMDczNV5BMl5BanBnXkFtZTcwODAwODA"
                             "yMQ@@._V1_.jpg",
                trailer_youtube="https://www.youtube.com/watch?v=xNMoQ_Cqt4E"
                )]

# Display the movies
open_movies_page(movies)
