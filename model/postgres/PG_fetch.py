# SOURCE https://medium.com/analytics-vidhya/part-4-pandas-dataframe-to-postgresql-using-python-8ffdb0323c09


import os
import sys
import psycopg2
from psycopg2 import OperationalError, errorcodes, errors
import psycopg2.extras as extras
import pandas as pd
from io import StringIO
import numpy as np
from sqlalchemy import create_engine
import seaborn as sns
import matplotlib.pyplot as plt
from dotenv import load_dotenv
import cursor


load_dotenv()


# TODO refactor this to local
# TODO refactor this to /data
# TODO refactor this to /data_set
# Loading data from github
irisData = pd.read_csv(
    "https://raw.githubusercontent.com/Muhd-Shahid/Learn-Python-Data-Access/main/iris.csv",
    index_col=False,
)
irisData.head()


def connect(conn_params_dic):
    """
    connect function for PostgreSQL database server
    :param conn_params_dic:
    :return:
    """
    conn = None
    try:
        print("Connecting to the PostgreSQL...........")
        conn = psycopg2.connect(**conn_params_dic)
        print("Connection successfully..................")

    except OperationalError as err:
        # passing exception to function
        show_psycopg2_exception(err)
        # set the connection to 'None' in case of error
        conn = None
    return conn


def show_psycopg2_exception(err):
    """
    handles and parses psycopg2 exceptions
    :param err:
    :return:
    """
    # get details about the exception
    err_type, err_obj, traceback = sys.exc_info()
    # get the line number when exception occured
    line_n = traceback.tb_lineno
    # print the connect() error
    print("\npsycopg2 ERROR:", err, "on line number:", line_n)
    print("psycopg2 traceback:", traceback, "-- type:", err_type)
    # psycopg2 extensions.Diagnostics object attribute
    print("\nextensions.Diagnostics:", err.diag)
    # print the pgcode and pgerror exceptions
    print("pgerror:", err.pgerror)
    print("pgcode:", err.pgcode, "\n")


def create_table(cursor):
    try:
        # Dropping table iris if exists
        cursor.execute("DROP TABLE IF EXISTS iris;")
        sql = """CREATE TABLE iris(
		sepal_length DECIMAL(2,1) NOT NULL,
		sepal_width DECIMAL(2,1) NOT NULL,
		petal_length DECIMAL(2,1) NOT NULL,
		petal_width DECIMAL(2,1),
		species CHAR(11)NOT NULL
		)"""
        # Creating a table
        cursor.execute(sql)
        print("iris table is created successfully...............")
    except OperationalError as err:
        # pass exception to function
        show_psycopg2_exception(err)
        # set the connection to 'None' in case of error
        conn = None


# Example
def run_method(n):
    """

    :param n:
    :return:
    """
    for i in range(n):
        3**n


from timeit import default_timer as timer

start_time = timer()
run_method(10000)
end_time = timer()
elapsed = end_time - start_time
print("function took {:.3f} ms".format((elapsed) * 1000.0))


def single_inserts(conn, df, table):
    """
    obtain baseline we start with the easiest methodology, insert records
    :param conn:
    :param df:
    :param table:
    :return:
    """
    for i in df.index:
        cols = ",".join(list(df.columns))
        vals = [df.at[i, col] for col in list(df.columns)]
        query = "INSERT INTO %s(%s) VALUES(%s,%s,%s,%s,'%s')" % (
            table,
            cols,
            vals[0],
            vals[1],
            vals[2],
            vals[3],
            vals[4],
        )
        cursor.execute(query)
    print("single_inserts() done")


def execute_many(conn, datafrm, table):
    """
    using cursor.executemany() to insert the dataframe
    :param conn:
    :param datafrm:
    :param table:
    :return:
    """

    # Creating a list of tupples from the dataframe values
    tpls = [tuple(x) for x in datafrm.to_numpy()]

    # dataframe columns with Comma-separated
    cols = ",".join(list(datafrm.columns))

    # SQL query to execute
    sql = "INSERT INTO %s(%s) VALUES(%%s,%%s,%%s,%%s,%%s)" % (table, cols)
    cursor = conn.cursor()
    try:
        cursor.executemany(sql, tpls)
        print("Data inserted using execute_many() successfully...")
    except (Exception, psycopg2.DatabaseError) as err:
        # pass exception to function
        show_psycopg2_exception(err)
        cursor.close()


def execute_batch(conn, datafrm, table, page_size=150):
    """
    using psycopg2.extras.execute_batch() to insert the dataframe
    :param conn:
    :param datafrm:
    :param table:
    :param page_size:
    :return:
    """

    # Creating a list of tupples from the dataframe values
    tpls = [tuple(x) for x in datafrm.to_numpy()]

    # dataframe columns with Comma-separated
    cols = ",".join(list(datafrm.columns))

    # SQL query to execute
    sql = "INSERT INTO %s(%s) VALUES(%%s,%%s,%%s,%%s,%%s)" % (table, cols)
    cursor = conn.cursor()
    try:
        extras.execute_batch(cursor, sql, tpls, page_size)
        print("Data inserted using execute_batch() successfully...")
    except (Exception, psycopg2.DatabaseError) as err:
        # pass exception to function
        show_psycopg2_exception(err)
        cursor.close()


def execute_values(conn, datafrm, table):
    """
    using psycopg2.extras.execute_values() to insert the dataframe.
    :param conn:
    :param datafrm:
    :param table:
    :return:
    """

    # Creating a list of tupples from the dataframe values
    tpls = [tuple(x) for x in datafrm.to_numpy()]

    # dataframe columns with Comma-separated
    cols = ",".join(list(datafrm.columns))

    # SQL query to execute
    sql = "INSERT INTO %s(%s) VALUES %%s" % (table, cols)
    cursor = conn.cursor()
    try:
        extras.execute_values(cursor, sql, tpls)
        print("Data inserted using execute_values() successfully..")
    except (Exception, psycopg2.DatabaseError) as err:
        # pass exception to function
        show_psycopg2_exception(err)
        cursor.close()


def execute_mogrify(conn, datafrm, table):
    """
    Using execute.mogrify() to insert the dataframe.
    :param conn:
    :param datafrm:
    :param table:
    :return:
    """

    # Creating a list of tupples from the dataframe values
    tpls = [tuple(x) for x in datafrm.to_numpy()]

    # dataframe columns with Comma-separated
    cols = ",".join(list(datafrm.columns))

    # SQL quert to execute
    cursor = conn.cursor()
    values = [cursor.mogrify("(%s,%s,%s,%s,%s)", tup).decode("utf8") for tup in tpls]
    sql = "INSERT INTO %s(%s) VALUES " % (table, cols) + ",".join(values)
    try:
        cursor.execute(sql, tpls)
        print("Data inserted using execute_mogrify() successfully.")
        cursor.close()
    except (Exception, psycopg2.DatabaseError) as err:
        # pass exception to function
        show_psycopg2_exception(err)
        cursor.close()


def copy_from_dataFile(conn, df, table):
    """
    using copy_from_dataFile to insert the dataframe.
    :param conn:
    :param df:
    :param table:
    :return:
    """

    #  Here we are going save the dataframe on disk as a csv file, load # the csv file and use copy_from() to copy it
    #  to the table
    tmp_df = "../Learn Python Data Access/iris_temp.csv"
    df.to_csv(tmp_df, header=False, index=False)
    f = open(tmp_df, "r")
    cursor = conn.cursor()
    try:
        cursor.copy_from(f, table, sep=",")
        print("Data inserted using copy_from_datafile() successfully....")
    except (Exception, psycopg2.DatabaseError) as err:
        os.remove(tmp_df)
        # pass exception to function
        show_psycopg2_exception(err)
        cursor.close()


def copy_from_dataFile_StringIO(conn, datafrm, table):
    """
    using copy_from() with StringIO to insert the dataframe
    :param conn:
    :param datafrm:
    :param table:
    :return:
    """

    # save dataframe to an in memory buffer
    buffer = StringIO()
    datafrm.to_csv(buffer, header=False, index=False)
    buffer.seek(0)

    cursor = conn.cursor()
    try:
        cursor.copy_from(buffer, table, sep=",")
        print("Data inserted using copy_from_datafile_StringIO() successfully....")
    except (Exception, psycopg2.DatabaseError) as err:
        # pass exception to function
        show_psycopg2_exception(err)
        cursor.close()


# Using alchemy method
# TODO update for .env
"""
connect_alchemy = "postgresql+psycopg2://%s:%s@%s/%s" % (
    conn_params_dic["user"],
    conn_params_dic["password"],
    conn_params_dic["host"],
    conn_params_dic["database"],
)
"""


def using_alchemy(df):
    """
    using df to sql function test a stream of 1000 at a time
    :param df:
    :return:
    """
    try:
        engine = create_engine(connect_alchemy)
        df.to_sql("irisAlchemy", con=engine, index=False, if_exists="append", chunksize=1000)
        print("Data inserted using to_sql()(sqlalchemy) done successfully...")
    except OperationalError as err:
        # passing exception to function
        show_psycopg2_exception(err)
        cursor.close()


def compare_methods_to_insert_bulk_data(df):
    """
    using iris dataset we compare the performance of each method
    :param df:
    :return:
    """
    # execute_query(conn, "delete from iris where true;")
    # Delete records from iris table
    cursor.execute("delete from iris where true;")
    print("Data has been deleted from iris table..........")
    print("")

    methods = [
        single_inserts,
        execute_many,
        execute_batch,
        execute_values,
        execute_mogrify,
        copy_from_dataFile,
        copy_from_dataFile_StringIO,
    ]
    df_performance = pd.DataFrame(
        index=range(len(methods)), columns=["Total_Records", "Method_Name", "Time ()"]
    )

    k = 0
    for method in methods:
        start_time = timer()
        method(conn, df, "iris")
        end_time = timer()

        df_performance.at[k, "Total_Records"] = len(df.index)
        df_performance.at[k, "Method_Name"] = method.__name__
        df_performance.at[k, "Time ()"] = end_time - start_time

        # Delete records for the previous method and prepare test for the next method
        # Delete records from iris table
        cursor.execute("delete from iris where true;")
        print("Data has been deleted from iris table........")
        print("")
        k = k + 1

        # Adding sqlalchemy's to_sql() method
        start_time = timer()
        using_alchemy(df)
        end_time = timer()
        df_performance.at[k, "Total_Records"] = len(df.index)
        df_performance.at[k, "Method_Name"] = "to_sql() | sqlalchemy"
        df_performance.at[k, "Time ()"] = end_time - start_time
        return df_performance


df = irisData
# Repeating our dataframe 667 times to get a large test dataframe
bulk_df = pd.concat([df] * 667, ignore_index=True)
print(len(bulk_df.index))

df_performance_list = []
for records in [1000, 5000, 10000, 50000, 100000]:
    print("records = %s" % records)
    df_cutoff = bulk_df[0:records]
    df_performance = compare_methods_to_insert_bulk_data(df_cutoff)
    df_performance_list.append(df_performance)
method_performances = pd.concat(df_performance_list, axis=0).reset_index()
method_performances.head()
