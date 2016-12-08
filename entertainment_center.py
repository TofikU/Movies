import fresh_tomatoes
import media

catch_me_if_you_can = media.Movie("Catch Me If You Can",
                                  "The most successful bank robber in history",
                                  "https://upload.wikimedia.org/wikipedia/en/4/4d/Catch_Me_If_You_Can_2002_movie.jpg",  # noqa
                                  "https://www.youtube.com/watch?v=71rDQ7z4eFg")  # noqa

the_great_gatsby = media.Movie("The Great Gatsby",
                               "The story of a millionaire named Jay Gatsby",
                               "https://upload.wikimedia.org/wikipedia/en/2/26/TheGreatGatsby2012Poster.jpg",  # noqa
                               "https://www.youtube.com/watch?v=rARN6agiW7o")

limitless = media.Movie("Limitless",
                        "A drug that produces enhanced mental acuity",
                        "https://upload.wikimedia.org/wikipedia/en/1/17/Limitless_Poster.jpg", # noqa
                        "https://www.youtube.com/watch?v=4TLppsfzQH8")

angel_a = media.Movie("Ange-A",
                      "The story of unlucky man and his angel",
                      "https://upload.wikimedia.org/wikipedia/en/4/4d/Angel-A_Poster.jpg",  # noqa
                      "https://www.youtube.com/watch?v=IaoYTgbUmdc")

end_of_watch = media.Movie("End of Watch",
                           "The story of LAPD partners and friends",
                           "https://upload.wikimedia.org/wikipedia/en/6/64/End_of_Watch_Poster.jpg",  # noqa
                           "https://www.youtube.com/watch?v=QG28aIUyG3k")

in_time = media.Movie("In Time",
                      "The story of future where time is money",
                      "https://upload.wikimedia.org/wikipedia/en/e/e0/Intimefairuse.jpg",  # noqa
                      "https://www.youtube.com/watch?v=6Re51joTIYA")

movies = [catch_me_if_you_can, the_great_gatsby,
          limitless, angel_a, end_of_watch, in_time]
# Uses list of movie instances as input to generate an HTML file
# and open it in the browser.
fresh_tomatoes.open_movies_page(movies)
