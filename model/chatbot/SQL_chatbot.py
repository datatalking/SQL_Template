# SOURCE
import csv

FILENAME = "../../data/movies.txt"


def main():
    """
    calls the stack to display column and read menu to terminal
    :return:
    """
    display_menu()

    movies = read_movies()
    while True:
        command = input("Command: ")
        if command == "list":
            list_movies(movies)
        elif command == "add":
            add_movie(movies)
        elif command == "del":
            delete_movie(movies)
        elif command == "exit":
            print("Bye!")
            break
        else:
            print("Not a valid command. Please try again.")


with open("../../data/movies.csv", "w", newline="") as file:
    writer = csv.writer(file)
    writer.writerows(movies)


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
    list all the movies inside movies object
    :param movies:
    :return:
    """
    for i in range(len(movies)):
        movie = movies[i]
        print(str(i + 1) + ". " + movie)
    print()


def add_movie(movies):
    """
        add a movie to end of list
    :param movies:
    :return:
    """
    movie = input("Movie: ")
    movie.append(movie)
    write_movies(movies)
    print(movie + " was added.\n")


def delete_movie(movies):
    """
        delete movie by number
    :param movies:
    :return:
    """
    index = int(input("Number: "))
    movie = movies.pop(index - 1)
    write_movies(movies)
    print(movie + " was deleted.\n")


def display_menu():
    """
        display the menu on screen
    :return:
    """
    print("The Movie List Program")
    print()
    print("COMMAND MENU")
    print("list - List all movies")
    print("add -  Add a movie")
    print("del -  Delete a movie")
    print("exit - Exit program")
    print()


if __name__ == "__main__":
    main()
