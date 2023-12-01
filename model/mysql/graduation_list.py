# graduation_list.py
import pandas as pd
from sqlalchemy import create_engine, Column, String, Integer, Float
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

Base = declarative_base()


def name_recognizer():
	"""
	Searches a dataset for names matching the fnames_data_set
	:return:
	"""
	fbnames_PATH = '/Users/wadewilson/sbox/fbnames'


def preprocess_data(data):
	"""

	:param data:
	:return:
	"""

    data = data.split("\n")  # Split data by newline

    cleaned_data = []
    current_entry = None

    for line in data:
        line = line.strip()
        if line:
            if current_entry is None:
                current_entry = line
            else:
                current_entry += f" {line}"
        else:
            if current_entry is not None:
                cleaned_data.append(current_entry)
                current_entry = None

    if current_entry is not None:
        cleaned_data.append(current_entry)

    return cleaned_data


# TODO move dirty_data to tests and add more
# TODO add handling for '  11'
# Example usage:
dirty_data = """Sona Komeili, Magna Cum Laude Valerie Lange, Magna Cum Laude"""
cleaned_data = preprocess_data(dirty_data)
for entry in cleaned_data:
    print(entry)


class Person(Base):
    __tablename__ = "people"

    id = Column(Integer, primary_key=True)
    first_name = Column(String(50))
    last_name = Column(String(50))
    degree_program = Column(String(100))
    # class_rank = Column(String(50))
    # email = Column(String(100))
    # phone_number = Column(String(20))
    # hobbies = Column(String(200))
    # job_search_status = Column(String(50))


MYSQL_DB_ROOT_PASSWORD = "Civilian_Pop!234"
MYSQL_DB_USER = ["user_001"]
MYSQL_DB_USER_PASSWORD = "Try_Newbie1098"
MYSQL_DB_USER_LIST = ["root", "admin_001", "user_001"]
MYSQL_DB_ALLOWED_USER_LIST = ["root", "admin_001", "user_001"]
MYSQL_DB_DISALLOWED_USER_LIST = ["admin_999", "user_999"]
MYSQL_DB_ADMIN_NAME = ["admin_001"]
MYSQL_DB_ADMIN_LIST = ["admin_001", "admin_002", "admin_003", "admin_004", "admin_005"]

MYSQL_DB_HOSTNAME = ["LOCALHOST"]
MYSQL_DB_NAME = "People_DB"
MYSQL_DB_HOST = "local"
MYSQL_DB_IP = "127.0.0.1"


MYSQL_DB_URL = (
    f"mysql://{MYSQL_DB_USER}:" f"{MYSQL_DB_USER_PASSWORD}@{MYSQL_DB_HOSTNAME}/" f"{MYSQL_DB_NAME}"
)

# Replace 'mysql://username:password@hostname/dbname' with your MySQL connection URL.
DB_URL = MYSQL_DB_URL


def parse_data_and_store_in_db():
    data = pd.read_csv("dirty_graduation_data.csv")

    data = data.splitlines()
    people_data = []
    person = {}
    for line in data:
        if line.strip():
            if line.startswith("#"):
                # Handle degree program line
                person["degree_program"] = line.strip()
            else:
                # Handle person's information
                if not person.get("first_name"):
                    person["first_name"] = line.strip().split(",")[0].strip()
                    person["last_name"] = line.strip().split(",")[1].strip()
                elif "Cum Laude" in line:
                    person["class_rank"] = line.strip()
                elif "✪" in line:
                    person["email"] = line.strip()
                elif "★" in line:
                    person["phone_number"] = line.strip()
                elif "✧" in line:
                    person["hobbies"] = line.strip()
                elif "✪" in line:
                    person["job_search_status"] = line.strip()
        else:
            # New person entry
            people_data.append(person)
            person = {}

    # Connect to the database
    engine = create_engine(DB_URL)
    Session = sessionmaker(bind=engine)
    session = Session()

    # Create the 'people' table if it doesn't exist
    Base.metadata.create_all(engine)

    # Insert data into the 'people' table
    for person_data in people_data:
        person_entry = Person(**person_data)
        session.add(person_entry)

    session.commit()
    session.close()


def main():
    parse_data_and_store_in_db()


if __name__ == "__main__":
    MYSQL_DB_ROOT_PASSWORD = "Civilian_Pop!234"
    MYSQL_DB_USER = ["user_001"]
    MYSQL_DB_USER_PASSWORD = "Try_Newbie1098"
    MYSQL_DB_USER_LIST = ["root", "admin_001", "user_001"]
    MYSQL_DB_ALLOWED_USER_LIST = ["root", "admin_001", "user_001"]
    MYSQL_DB_DISALLOWED_USER_LIST = ["admin_999", "user_999"]
    MYSQL_DB_ADMIN_NAME = ["admin_001"]
    MYSQL_DB_ADMIN_LIST = ["admin_001", "admin_002", "admin_003", "admin_004", "admin_005"]

    MYSQL_DB_HOSTNAME = ["LOCALHOST"]
    MYSQL_DB_NAME = "People_DB"
    MYSQL_DB_HOST = "local"
    MYSQL_DB_IP = "127.0.0.1"

    Configuration_File = "null"
    Base_Directory = "/usr/local/mysql"
    Data_Directory = "/usr/local/mysql/data"
    Plugin_Directory = "/usr/local/mysql/lib/plugin"
    Keyring_Data_File = "/usr/local/mysql/keyring/keyring"
    Error_Log = "/usr/local/mysql/data/mysqld.local.err"
    PID_File = "/usr/local/mysql/data/mysqld.local.pid"

    MYSQL_DB_URL = (
        f"mysql://{MYSQL_DB_USER}:"
        f"{MYSQL_DB_USER_PASSWORD}@{MYSQL_DB_HOSTNAME}/"
        f"{MYSQL_DB_NAME}"
    )
    main()
    parse_data_and_store_in_db()
