import os
import csv
import pyodbc
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# Database connection details
db_host = os.getenv("SSMS_DB_HOST")
db_port = os.getenv("SSMS_DB_PORT")
db_user = os.getenv("SSMS_DB_USER")
db_password = os.getenv("SSMS_DB_PASSWORD")
db_name = os.getenv("SSMS_DB_NAME")

# Define TSV file path
tsv_file_path = (
    "Users/wadewilson/sbox/PycharmProjects/realestate_data/data"
    "/state_market_tracker.tsv000",  # "_your_data.tsv"
)

# Establish a database connection
try:
    conn = pyodbc.connect(
        f"Driver={{SQL Server}};Server={db_host},{db_port};Database={db_name};User Id={db_user};Password={db_password};"
    )
    cursor = conn.cursor()
except pyodbc.Error as e:
    print(f"Database connection error: {str(e)}")
    exit(1)

# Create a table to store the TSV data
try:
    cursor.execute(
        """
        CREATE TABLE IF NOT EXISTS your_table_name (
            period_begin DATE,
            period_end DATE,
            period_duration INT,
            region_type VARCHAR(255),
            region_type_id INT,
            table_id INT,
            is_seasonally_adjusted CHAR(1),
            region VARCHAR(255),
            city VARCHAR(255),
            state VARCHAR(255),
            state_code CHAR(2),
            property_type VARCHAR(255),
            property_type_id INT,
            median_sale_price INT,
            median_sale_price_mom FLOAT,
            median_sale_price_yoy FLOAT,
            median_list_price INT,
            median_list_price_mom FLOAT,
            median_list_price_yoy FLOAT,
            median_ppsf INT,
            median_ppsf_mom FLOAT,
            median_ppsf_yoy FLOAT,
            median_list_ppsf INT,
            median_list_ppsf_mom FLOAT,
            median_list_ppsf_yoy FLOAT,
            homes_sold INT,
            homes_sold_mom FLOAT,
            homes_sold_yoy FLOAT,
            pending_sales INT,
            pending_sales_mom FLOAT,
            pending_sales_yoy FLOAT,
            new_listings INT,
            new_listings_mom FLOAT,
            new_listings_yoy FLOAT,
            inventory INT,
            inventory_mom FLOAT,
            inventory_yoy FLOAT,
            months_of_supply FLOAT,
            months_of_supply_mom FLOAT,
            months_of_supply_yoy FLOAT,
            median_dom FLOAT,
            median_dom_mom FLOAT,
            median_dom_yoy FLOAT,
            avg_sale_to_list FLOAT,
            avg_sale_to_list_mom FLOAT,
            avg_sale_to_list_yoy FLOAT,
            sold_above_list FLOAT,
            sold_above_list_mom FLOAT,
            sold_above_list_yoy FLOAT,
            price_drops FLOAT,
            price_drops_mom FLOAT,
            price_drops_yoy FLOAT,
            off_market_in_two_weeks FLOAT,
            off_market_in_two_weeks_mom FLOAT,
            off_market_in_two_weeks_yoy FLOAT,
            parent_metro_region VARCHAR(255),
            parent_metro_region_metro_code INT,
            last_updated DATETIME
        );
    """
    )
    conn.commit()
except pyodbc.Error as e:
    print(f"Error creating table: {str(e)}")
    conn.rollback()
    conn.close()
    exit(1)

# Load data from TSV file into the database
try:
    with open(tsv_file_path, "r", newline="", encoding="utf-8") as tsvfile:
        reader = csv.reader(tsvfile, delimiter="\t")
        next(reader)  # Skip header row
        for row in reader:
            cursor.execute(
                """
                INSERT INTO your_table_name
                VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
            """,
                row,
            )
    conn.commit()
    print("Data loaded successfully.")
except pyodbc.Error as e:
    print(f"Error loading data: {str(e)}")
    conn.rollback()

# Close the database connection
conn.close()
