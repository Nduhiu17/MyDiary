import os
from datetime import datetime

import psycopg2

try:
    # connect_str = "dbname='diary_db' user='antony' host='localhost' " + \
    #               "password='password'"
    connect_str = "dbname='diary_db_test' user='postgres' host='localhost' " + \
      "password='postgres'"
    # enabled for testing
    os.environ['DATABASE_URL'] = connect_str
    conn = psycopg2.connect(os.environ['DATABASE_URL'])
    conn.autocommit = True
    cursor = conn.cursor()
    print("db connectd!!!")

except Exception as e:
    print("Uh oh, can't connect. Invalid dbname, user or password?")
    print(e)


class Entry:

    @classmethod
    def save(cls, user_id, date_created, date_modified, title, description):
        """Method to save an entry"""
        format_str = f"""
        INSERT INTO public.entries (user_id,title,description,date_created,date_modified)
        VALUES ('{user_id}','{title}','{description}','{str(datetime.now())}','{str(datetime.now())}') ;
        """
        cursor.execute(format_str)

        return {
            "user_id": user_id,
            "date_created": date_created,
            "title": title,
            "description": description
        }

    @classmethod
    def get_all_entries(cls):
        """Method to get all entries"""

        cursor.execute('SELECT * FROM "public"."entries";')
        rows = cursor.fetchall()
        print(rows)

        list_dict = []

        for item in rows:
            z = {}

            z['id'] = item[0]
            z['user_id'] = item[1]
            z['date_created'] = item[2]
            z['date_modified'] = item[3]
            z['title'] = item[4]
            z["description"] = item[5]

            list_dict.append(z)
            print("list_dict")
            print(os.environ['DATABASE_URL'])

        return list_dict

    # @classmethod
    # def get_entry(cls, entry_id):
    #     """Method to get an entry by id"""
    #     # entry = cls.entries[entry_id]
    #     # return entry
    #     cursor.execute('SELECT * FROM "public"."entries"')
    #     rows = cursor.fetchone()
    #     print("######################################")
    #     print(rows)

    #     list_dict = []

    #     for item in rows:

    #         z = {}

    #         z['id'] = item[0]
    #         z['user_id'] = item[1]
    #         z['date_created'] = item[2]
    #         z['title'] = item[3]
    #         z["description"] = item[4]

    #         list_dict.append(z)

    #     entry = list_dict[id]
    #     print("$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$")
    #     print("this is my",entry)

    #     return {}

    # @classmethod
    # def modify_entry(cls, id, modified_object):
    #     """Method to modify an entry"""
    #     cls.entries[id] = modified_object
    #     return modified_object


class User:

    @classmethod
    # this method registers a user in the database
    def save(cls, username, email, password):
        format_str = f"""
        INSERT INTO public.users (username,email,password)
        VALUES ('{username}','{email}','{password}');
        """
        cursor.execute(format_str)
        return {
            "username": username,
            "email": email,
        }

    @classmethod
    def find_by_email(cls, email):
        # This method gets a user using email
        try:
            cursor.execute("select * from users where email = %s", (email,))
            user = cursor.fetchone()
            return list(user)
        except Exception as e:
            return e
