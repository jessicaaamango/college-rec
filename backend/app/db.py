import mysql.connector
from mysql.connector import Error
import pandas as pd

# https://www.freecodecamp.org/news/connect-python-with-sql/

def create_server_connection(host_name, user_name, user_password):
    connection = None #closes any existing connections so server isn't confused
    try: #handling any potential erros
        connection = mysql.connector.connect(
            host = host_name,
            user = user_name,
            password = user_password
        )
        print("MySQL Database connection successful")
    except Error as err:
        print(f"Error: '{err}'")
    return connection

# using function to connect to MySQL
pw = "12345678"
connection = create_server_connection("localhost", "root", pw)