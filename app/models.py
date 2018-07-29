# from . import cursor

# cursor = ''
import os

import psycopg2

try:
    # connect_str = "dbname='diary_db' user='antony' host='localhost' " + "password='password'"
    connect_str=os.environ['DATABASE_URL']
    # use our connection values to establish a connection
    conn = psycopg2.connect(connect_str)
    # create a psycopg2 cursor that can execute queries
    cursor = conn.cursor()
    # cursor.execute('SELECT * FROM "public"."entries"')
    # rows = cursor.fetchall()
    # print(rows)


    # db = os.environ['DATABASE_URL']
    # connection = psycopg2.connect(db)
    # connection.autocommit = True
    # cursor = connection.cursor()
    # print("db connectd!!!",db)
except Exception as e:
    print("Uh oh, can't connect. Invalid dbname, user or password?")
    print(e)
# from app import db


class Entry:
    entries = []

    def __init__(self, title, description, date_created):
        """Method to initialize Entry class"""

        self.title = title
        self.description = description
        self.date_created = date_created

    def save(self):
        """Method to save an entry"""
        self.entries.append(self)
        # format_str = """INSERT INTO entries (entry_id, title, description, date_created)
        # VALUES (NULL, "{title}", "{description}", "{date_created}");"""
        # sql_command = format_str.format(title=[0], description=[1], date_created=[2])
        # cursor.execute(sql_command)
    

    @classmethod
    def get_all_entries(cls):
        """Method to get all entries"""
        # entries = cls.entries

        cursor.execute('SELECT * FROM "public"."entries"')
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
        return list_dict

        # for row in rows:
        #     lis.append(Entry(title=))
        # my_entries_json = []
        # for entry in lis:
        #     my_entries_json.append(entry.__dict__)
        # return

    


    @classmethod
    def get_entry(cls, entry_id):
        """Method to get an entry by id"""
        # entry = cls.entries[entry_id]
        # return entry
        # cursor = db.cursor()
        cursor.execute('SELECT * FROM "public"."entries"')
        rows = cursor.fetchall()
        print("######################################")
        print(rows)

        list_dict = []

        for item in rows:

            z = {}

            z['id'] = item[0]
            z['title'] = item[1]
            z["description"] = item[2]
            z['datecreated'] = item[3]
            list_dict.append(z)

        entry = list_dict[entry_id]
        print("$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$")
        print("this is my",entry)
        
        return entry



    @classmethod
    def modify_entry(cls, id, modified_object):
        """Method to modify an entry"""
        cls.entries[id] = modified_object
        return modified_object

    def delete(self):
        """Method to delete an entry"""
        Entry.entries.remove(self)

    
    @classmethod
    def entry_exists(cls,title):
        """Method to check whether an entry exists"""
        for entry in cls.entries:
            if entry.title == title:
                return True
        return False
