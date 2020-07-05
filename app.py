import datetime
import database

menu = """Please select one of the following options:
1) Add new movie.
2) View upcoming movies.
3) View all movies
4) Watch a movie
5) View watched movies.
6) Add user
7) Search for movies.
8) Exit.

Your selection: """
welcome = "Welcome to the watchlist app!"

print(welcome)
database.create_tables()
user_input = input(menu)


def prompt_add_movie():
    title = input("Enter movie title: ")
    release_date = input("Insert movie release date (mm-dd-YYYY): ")
    parsed_datetime = datetime.datetime.strptime(release_date, "%m-%d-%Y")
    timestamp = parsed_datetime.timestamp()

    database.add_movie(title, timestamp)


def prompt_add_user():
    username = input("Create new username: ")
    database.add_user(username)


def print_movies(heading, movies):
    print(f" ----- {heading} movies ----- ")
    # for movie in movies:
    # instead, use tuple destructuring
    for _id, title, release_date in movies:
        movie_date = datetime.datetime.fromtimestamp(release_date)
        human_date = movie_date.strftime("%b-%d-%Y")
        print(f"-- {title} (released on {human_date}, id: {_id})")
    print("\n")


def watch_movie():
    username = input("Username: ")
    movie_id = input("Enter id of watched movie: ")
    database.watch_movie(username, movie_id)


def prompt_print_watched_movies():
    username = input("Username: ")
    watched_movies = database.get_watched_movies(username)
    if watched_movies:
        print_movies(f"{username}'s watched", watched_movies)
    else:
        print("User has not watched any movies yet.")

    print('\n')


def prompt_search_movies():
    search_term = input("What would you like to search for? ")
    movies = database.search_movies(search_term)
    if movies:
        print_movies('Search results:', movies)
    else:
        print('No matching search results.')
    print('\n')


while user_input != "8":
    if user_input == "1":
        prompt_add_movie()
    elif user_input == "2":
        movies = database.get_movies(True)
        print_movies('Upcoming movies', movies)
    elif user_input == "3":
        movies = database.get_movies()
        print_movies('All movies', movies)
    elif user_input == "4":
        watch_movie()
    elif user_input == "5":
        prompt_print_watched_movies()
    elif user_input == "6":
        prompt_add_user()
    elif user_input == "7":
        prompt_search_movies()
    else:
        print("Invalid input, please try again!")

    user_input = input(menu)
