import psycopg2
from config import  host, user, password, db_name, port_id


# SQL TABLE CREATION
cursor = None
connect = None

try:
        connect = psycopg2.connect(
                    host = host,
                    dbname = db_name,
                    user = user,
                    password = password,
                    port = port_id
                    )
        cursor = connect.cursor()
        connect.autocommit = True

        create_t = """CREATE TABLE IF NOT EXISTS SnakeGame (
                            id SERIAL PRIMARY KEY,
                            user_name VARCHAR(20),
                            user_score INT, 
                            user_level INT)"""
        cursor.execute(create_t)
except Exception as error:
        print('ERROR IS:', error)
finally:
        if cursor is not None:
                cursor.close()
        if connect is not None:
                connect.close()