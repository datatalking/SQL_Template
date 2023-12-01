# SOURCE https://medium.com/@BetterEverything/automate-incoming-file-processing-with-python-df7daca0e7ff
# TODO merge this with larger deduper and watchdog.
"""
The directory watcher that we will create will consist of 4 systems:
1. a system to repeat a process every X seconds
2. a system to check whether there are files in a directory
3. a system that processes the files (this is specific to the use case)
4. a system that moves a file out of the watched directory
"""


import time
import os
import shutil
from os import environ, path
from dotenv import load_dotenv
import TODO_scanner

load_dotenv()


def main():
    """
    runs each time Folder_watchdog.py runs
    :return:
    """
    csv_order_collection()
    TODO_scanner()


# TODO need to adjust split as we are missing first few words in /data
# TODO error "UnicodeDecodeError: 'utf-8' codec can't decode byte 0xa6 in position 343: invalid start byte"
def csv_order_collection():
    """
    using os.listdir iterate through PATh to parse order number from filename
    :return:
    """
    while True:
        files = os.listdir(directory_path)
        for file in files:
            filepath = directory_path + file
            ##BEGIN: USE CASE SPECIFIC##
            ordernumber = file[5:].split(".csv")[0]
            orderlines = []
            with open(filepath, "r") as f:
                for line in f:
                    line = line.strip()
                    orderlines.append("{},{}\n".format(ordernumber, line))
            # TODO move path to .env file
            # TODO remove duplicated path below
            with open("./data/collected_orders.csv", "a") as f:
                for line in orderlines:
                    f.write(line)
            ##END: USE CASE SPECIFIC##

            destination_file = destination_path + file
            shutil.move(filepath, destination_file)

        time.sleep(10)


if __name__ == "__main__":
    USER_NAME = environ.get("USER_NAME")
    directory_path = f"/Users/" f"{USER_NAME}/sbox/PycharmProjects/SQL_Template/data/"
    destination_path = f"/Users/{USER_NAME}/sbox/PycharmProjects/SQL_Template/data/processed/"

    # Find .env file
    basedir = path.abspath(path.dirname(__file__))
    load_dotenv(path.join(basedir, ".env"))
    main()
