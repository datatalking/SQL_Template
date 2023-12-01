# TODO_scanner.py
# SOURCE


import time
import os
import csv
import shutil
from os import environ, path
from dotenv import load_dotenv
import TODO_scanner

load_dotenv()


def main():
    scan_todo_tags()


def scan_todo_tags():
    """creates a CSV file named todo_tags.csv under the data/ folder and writes the following information for each TODO tag found
    :param file_name: The name of the file containing the TODO tag
    :param project_name: The name of the project (which is the same as the file
    name without the .py extension)
    :param tag_FOUND: The TODO tag found (e.g., TODO, FIXME, #TODO)
    :param tag_message: The message following the TODO tag
    :param date_added: The date the TODO tag was added to the file (using the file's creation time)
    :param USER_NAME: The username of the user running the script (using the os.environ.get('USER_NAME') function call)
    :param

    """

    cwd = os.getcwd()
    os.environ.get("USER_NAME")

    project_path = "/Users/{USER_NAME}/sbox/PycharmProjects/SQL_Template/"

    # Create the CSV file and write the header
    with open("data/todo_tags.csv", "w", newline="") as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow(
            ["file_name", "project_name", "tag_FOUND", "tag_message", "date_added", "user"]
        )

        # Loop through all files in the current directory
        for file_name in os.listdir(cwd):
            # Only check Python files
            if file_name.endswith(".py"):
                # Get the project name
                project_name = file_name.split(".")[0]

                # Open the file and loop through each line
                with open(file_name, "r") as f:
                    for i, line in enumerate(f):
                        # Check for TODO tags
                        if "TODO" in line or "FIXME" in line or "#TODO" in line:
                            # Get the tag message and date added
                            tag_message = line.strip()
                            date_added = os.path.getctime(file_name)

                            # Write the information to the CSV file
                            writer.writerow(
                                [
                                    file_name,
                                    project_name,
                                    line[: line.find(tag_message)],
                                    tag_message,
                                    date_added,
                                    os.environ.get("USERNAME"),
                                ]
                            )


if __name__ == "__main__":
    USER_NAME = environ.get("USER_NAME")
    DIRECTORY_PATH = f"/Users/" f"{USER_NAME}/sbox/PycharmProjects/SQL_Template/data/"
    DESTINATION_PATH = f"/Users/{USER_NAME}/sbox/PycharmProjects/SQL_Template/data/processed/"
    PROJECT_PATH = f"/Users/{USER_NAME}/sbox/PycharmProjects/SQL_Template/"

    # Find .env file
    basedir = path.abspath(path.dirname(__file__))
    load_dotenv(path.join(basedir, ".env"))
    main()
