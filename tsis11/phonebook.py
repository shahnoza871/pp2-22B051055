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






        # CODE FOR SQL QUERY
        # SELECT *
        # FROM phonebook
        # WHERE phone_num LIKE '%111%' 

        #OR

        # CODE FOR SQL QUERY
        # SELECT *
        # FROM phonebook
        # WHERE surname LIKE '__e%' 

        # ADD A COLUMN FOR SURNAME
        # ALTER TABLE phonebook
        # ADD COLUMN surname VARCHAR(20)


        # -- CREATE
        # OR
        # REPLACE
        # PROCEDURE
        # insert_user(
        #     --    IN
        # usr_name
        # VARCHAR(30),
        # --    IN
        # usr_surname
        # VARCHAR(30),
        # --    IN
        # usr_phone_num
        # VARCHAR(30)
        # - - )
        # -- LANGUAGE
        # 'plpgsql'
        #
        # -- AS
        # -- $$
        #
        # -- DECLARE
        # --    DECLARE
        # usr_id
        # INT;
        # -- BEGIN
        # --    SELECT
        # user_id
        # INTO
        # usr_id
        # FROM
        # phone_book
        # WHERE
        # user_name = usr_name or user_surname = usr_surname;
        #
        # -- if usr_id
        # IS
        # NOT
        # NULL
        # THEN
        # --        UPDATE
        # phone_book
        # --        SET
        # phone_num = usr_phone_num
        # WHERE
        # id = user_id;
        # --    ELSE
        # --        INSERT
        # INTO
        # phone_book(user_name, user_surname, phone_num)
        # --        VALUES(usr_name, usr_surname, usr_phone_num);
        # --    END
        # IF;
        # -- END;
        # -- $$
        #
        # -- CALL
        # insert_user('new_user', 'new_user_surname', '102040506')
        # -- SELECT * FROM
        # phone_book;        


        # delete_by_name_or_phone(IN name_or_phone)
        # BEGIN
        # DELETE FROM phone_book WHERE user_name = name_or_phone;
        # DELETE FROM phone_book WHERE phone_num = name_or_phone;
        # END;



        # procedure to insert user or update phone_num if user already exists
        # insert_user( IN usr_name character varying, IN usr_surname character varying, IN usr_phone_num character varying)
        # DECLARE
        # DECLARE usr_id INT;
        # BEGIN
        # SELECT user_id INTO usr_id FROM phone_book WHERE user_name = usr_name or user_surname = usr_surname;
        
        # if usr_id IS NOT NULL THEN
        # UPDATE phone_book
        # SET phone_num = usr_phone_num WHERE id = user_id;
        # ELSE
        # INSERT INTO phone_book(user_name, user_surname, phone_num)
        # VALUES (usr_name, usr_surname, usr_phone_num);
        # END IF;
        # END;




        #procedure to insert users by a list and check if given phone number is correct
        # insert_users(IN name_list text[], IN phone_list text[], OUT incorrect_data text[])
        # DECLARE
        # i integer := 1;
        # phone_format text := '^[0-9\-\+]{9,15}$';
        # BEGIN
        # WHILE i <= array_length(name_list, 1) AND i <= array_length(phone_list, 1) LOOP
        #         IF NOT phone_list[i] ~ phone_format THEN
        #         incorrect_data := array_append(incorrect_data, name_list[i]  ': '  phone_list[i]);
        #         ELSE
        #         INSERT INTO phone_book (user_name, phone_num) VALUES (name_list[i], phone_list[i]);
        #         END IF;
        #         i := i + 1;
        # END LOOP;
        # END;





except Exception as error:
        print('ERROR IS:', error)
finally:
        if cursor is not None:
                cursor.close()
        if conn is not None:
                conn.close()