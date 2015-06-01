from media import Movie
import fresh_tomatoes

# Instantiate the list of movie objects in a list
movie_list = [
    Movie(
        'Fast And Furious',
        'https://www.youtube.com/watch?v=2TAOizOnNPo',
        'http://api.ning.com/files/aoq71LIlZOChX3eftNIu5RGmNOdK9a7PkZZbE1dyOvHhzCqylhhDdRFcDv2\
        SzAIO-5-glP9eVwdSJJ5TnK2GmnIIJnZGG52B/fullhdhizliveofkeli1fastandfurious1turkcedublaji\
        zle.jpg',
        'The First Fast And Furious Movie! Brian is a renegade cop who teams up with renegade driver Dominick Toretto.'
    ),
    Movie(
        '2 Fast 2 Furious',
        'https://www.youtube.com/watch?v=F_VIM03DXWI',
        'http://onlinemovies.pro/wp-content/uploads/2014/06/2-Fast-2-Furious-2003-poster.jpg',
        'The second, fairly underwhelming, Fast and Furious. The only good part of this is Tyrese!'
    ),
    Movie(
        'Fast And Furious 3: Tokyo Drift',
        'https://www.youtube.com/watch?v=xZ96tl5MrfU',
        'http://imagerip.net/images/tokyodrift.jpg',
        'The third, and vastly underrated, Fast and Furious where we see the underground drift scene in Tokyo, Japan!'
    )]

# Have fresh_tomatoes render the movies
fresh_tomatoes.open_movies_page(movie_list)
