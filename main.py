# This is a sample Python script.

# Press ⇧F10 to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.
# TODO to increase speed and scale up try https://github.com/dask-contrib/dask-sql
# TODO create cpu/gpu switch where it checks if GPU exists then uses dask

from os import environ, path
from dotenv import load_dotenv
import dask


load_dotenv()  # take environment variables from .env.


def main():
    """
    get users name for db admin priveledges and personalization
    :return:
    """
    print_hi(user_name=USER_NAME)
    which_database()
    # gpu_exist_active()
    # TODO create menu_generator() function similar to mstables
    create_environment()


def print_hi(user_name):
    """
    get users name for db admin priveledges and personalization
    :param user_name:
    :return:
    """
    # global user_name
    print(f"Hi, {user_name}")  # Press ⌘F8 to toggle the breakpoint.
    return user_name


def which_database():
    """
    Get users preference for database
    :return:
    """
    POSTGRESQL = "postgress_12"
    MYSQL = "mysql_08"
    SQLITE3 = "sqlite_03"
    SQLSERVER = "sqlserver_17"
    ORACLE = "oracle_11"
    AWS = "RDS_09"
    NOSQL = "salesforce_02"

    # TODO use the terms from each database
    # TODO print(f'Hi, {user_name} what database do you want to work with?')
    # TODO print(f'Do you prefer')


# TODO pull from nvidia for GPU check script
def gpu_exist_active():
    """
    checking if a GPU is active
    :return:
    """
    # SOURE https://dask-sql.readthedocs.io/en/latest/
    import dask.datasets

    # TODO error ""
    print("cuda gpu support available but not installed 'import dask_cudf'")

    from dask_sql import Context

    # create a context to register tables
    c = Context()

    # create a table and register it in the context
    df = dask.datasets.timeseries()
    c.create_table("timeseries", df, gpu=True)

    # execute a SQL query; the result is a "lazy" Dask dataframe
    result = c.sql(
        """
       SELECT
          name, SUM(x) as "sum"
       FROM
          timeseries
       GROUP BY
          name
    """
    )

    # actually compute the query...
    result.compute()

    # ...or use it for another computation
    result.sum.mean().compute()
    pass


def create_environment():
    """
    function to create and populate .env file
    """
    # TODO prompt user for database un
    # TODO prompt user for database pw
    # TODO prompt user for database PATH
    # TODO prompt user for database API info (as needed)
    # TODO prompt user for database booster like dask, motin
    # TODO prompt user for database bloom index if accuracy is vital
    # TODO prompt user for database packages, pandas, numpy, matplotlib, seaborn
    # TODO prompt user for database POSTGRESQL, SQLITE, MYSQL, SQLSERVER, ORACLE, AWS, NOSQL
    print("create_environment function pass")


# Press the green button in the gutter to run the script.
if __name__ == "__main__":
    USER_NAME = environ.get("USER_NAME")
    confirm_user_name = input(f"Hello your first name is {USER_NAME}?")
    # TODO add yes/no option else
    # TODO grep day time greetings based on morning, night etc
    # TODO prompt user for user name
    print_hi("Greetings, PyCharm has run")

    # Find .env file
    basedir = path.abspath(path.dirname(__file__))
    load_dotenv(path.join(basedir, ".env"))

    # General Config
    SECRET_KEY = environ.get("SECRET_KEY")
    FLASK_APP = environ.get("FLASK_APP")
    FLASK_ENV = environ.get("FLASK_ENV")
    main()
