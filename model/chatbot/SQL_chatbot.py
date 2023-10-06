# SOURCE


FILENAME = "movies.txt"


def write_movies(movies):
    """
    open FILENAME and add movies
    :param movies:
    :return:
    """
    with open(FILENAME, "w") as file:
        for movie in movies:
            file.write(movie + "\n")


def read_movies():
    """
        open FILENAME and read each line as a new movie
    :return:
    """
    movies = []
    with open(FILENAME) as file:
        for line in file:
            line = line.replace("\n", "")
            movies.append(line)
    return movies


def list_movies(movies):
    """

    :param movies:
    :return:
    """
    for i in range(len(movies)):
        movie = movies[i]
        print(str(i + 1) + ". " + movie)
    print()


def add_movie(movies):
    """

    :param movies:
    :return:
    """
    movie = input("Movie: ")
    movie.append(movie)
    write_movies(movies)
    print(movie + " was added.\n")


def delete_movie(movies):
    """

    :param movies:
    :return:
    """
    index = int(input("Number: "))
    movie = movies.pop(index - 1)
    write_movies(movies)
    print(movie + " was deleted.\n")


def display_menu():
    """

    :return:
    """
    print("The Movie List Program")
    print()
    print("COMMAND MENU")
    print("list - List")
