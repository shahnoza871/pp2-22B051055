import psycopg2
from  cofig import hostname, database, username, pwd, port_id
conn = None
cursor = None

try:
        conn = psycopg2.connect(
                host = hostname,
                dbname = database,
                user = username,
                password = pwd,
                port = port_id)
        cursor = conn.cursor()
        conn.autocommit = True


        # Design tables for PhoneBook
        create_t = """CREATE TABLE IF NOT EXISTS PhoneBook (
                            id SERIAL PRIMARY KEY,
                            name VARCHAR(20),
                            phone_num VARCHAR(20))"""
        cursor.execute(create_t)


        # INSERT DATA FROM CSV FILE
        # insert = """
        #      COPY phonebook (name, phone_num)
        #      FROM 'C:/Users/DELL/Desktop/folder/csv_for_lab10_phone_book.csv'
        #      DELIMITER ','
        #      CSV HEADER;
        #      """
        # cursor.execute(insert)


        # INSERT DATA FROM CONSOLE
        # N = int(input("Enter number of Users: "))
        # print("Enter USER NAME and his PHONE NUMBER separated by SPACE:")
        # for i in range(N):
        #     data = input()
        #     cursor.execute(
        #         """
        #         INSERT INTO phonebook(name, phone_num)
        #         VALUES (%s, %s);
        #         """, (data.split())
        #     )


        # UPDATING PHONE NUMBER BY NAME
        # name = input("Enter users first name: ")
        # updated_num = input("Enter new phone number: ")
        # cursor.execute(
        #         """UPDATE phonebook
        #         SET phone_num = (%s)
        #         WHERE name = (%s)
        #         """, (updated_num, name)
        # )

        # UPDATING NAME BY PHONE NUMBER
        # upadated_num = input("Enter phone number: ")
        # name = input("Enter user's new name: ")
        # cursor.execute(
        #         """
        #         UPDATE phonebook
        #         SET name = (%s)
        #         WHERE phone_num = (%s)
        #         """, (name, upadated_num)
        # )

        # UPDATE NAME
        # crrnt_name = input("Enter current name: ")
        # updated_name = input("Enter new name: ")
        # cursor.execute(
        #         """
        #         UPDATE phonebook
        #         SET name = (%s)
        #         WHERE name = (%s)
        #         """, (updated_name, crrnt_name)
        # )

        # UPDATE PHONE NUMBER
        # crrnt_num = input("Enter current phone number: ")
        # updated_num = input("Enter new phone number: ")
        # cursor.execute(
        #         """
        #         UPDATE phonebook
        #         SET phone_num = (%s)
        #         WHERE phone_num = (%s)
        #         """, (updated_num, crrnt_num)
        # )


        # QUERYING THROUGH THE PHONE BOOK

        # fetches users with phone numbers containing 54
        # cursor.execute(
        #     """
        #     SELECT id, name from phonebook WHERE phone_num like '%54%'
        #     """
        # )
        # print("Number of users:", cursor.rowcount)
        # row = cursor.fetchone()
        # while row is not None:
        #     print(row)
        #     row = cursor.fetchone()

        # fetches users with id less than N
        # cursor.execute(
        #     """
        #     SELECT user_name, phone_num from phone_book WHERE user_id <= 3
        #     """
        # )
        # rows = cursor.fetchall()
        #
        # for row in rows:
        #     print(row)


        # DELETING DATA BY NAME:
        # user_name = input("Enter name: ")
        # cursor.execute(
        #         """
        #         DELETE FROM phonebook
        #         WHERE name = 'Greta'
        #         """
        # )




except Exception as error:
        print('ERROR IS:', error)
finally:
        if cursor is not None:
                cursor.close()
        if conn is not None:
                conn.close()