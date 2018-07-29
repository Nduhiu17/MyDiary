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
    def save(cls, title, description):
        """Method to save an entry"""
        format_str = f"""
        INSERT INTO public.entries (title,description,datecreated)
        VALUES ('{title}','{description}','{str(datetime.now())}') ;
        """
        sql_result = cursor.execute(format_str)

        return {
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
            z['title'] = item[1]
            z["description"] = item[2]
            z['datecreated'] = item[3]

            list_dict.append(z)
            print("list_dict")
            print(os.environ['DATABASE_URL'])

        return list_dict

    @classmethod
    def get_entry(cls, entry_id):
        """Method to get an entry by id"""
        # entry = cls.entries[entry_id]
        # return entry
        cursor.execute('SELECT * FROM "public"."entries"')
        rows = cursor.fetchone()
        print("######################################")
        print(rows)

        # list_dict = []
        #
        # for item in rows:
        #
        #     z = {}
        #
        #     z['id'] = item[0]
        #     z['title'] = item[1]
        #     z["description"] = item[2]
        #     z['datecreated'] = item[3]
        #     list_dict.append(z)
        #
        # entry = list_dict[entry_id]
        # print("$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$")
        # print("this is my",entry)

        return {}

    @classmethod
    def modify_entry(cls, id, modified_object):
        """Method to modify an entry"""
        cls.entries[id] = modified_object
        return modified_object

    def delete(self):
        """Method to delete an entry"""
        Entry.entries.remove(self)

    @classmethod
    def entry_exists(cls, title):
        """Method to check whether an entry exists"""
        for entry in cls.entries:
            if entry.title == title:
                return True
        return False
