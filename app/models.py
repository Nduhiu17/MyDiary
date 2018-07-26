import psycopg2
from psycopg2._json import Json

try:
    connect_str = "dbname='diary_db' user='antony' host='localhost' " + \
                  "password='password'"
    # use our connection values to establish a connection
    conn = psycopg2.connect(connect_str)
    # create a psycopg2 cursor that can execute queries
    cursor = conn.cursor()
    print("db connectd!!!")
except Exception as e:
    print("Uh oh, can't connect. Invalid dbname, user or password?")
    print(e)


class Entry:

    def __init__(self, entryid, title, description, datecreated):
        """Method to initialize Entry class"""
        self.entryid = entryid
        self.title = title
        self.description = description
        self.datecreated = datecreated

    @classmethod
    def save(cls, entryid, title, description, datecreated):
        """Method to save an entry"""
        print("title in models.py", title)
        print("description in models.py", description)
        print("datecreated in models.py", datecreated)


        sql_command = "INSERT INTO entries VALUES(null, '%s', '%s', '%s')" % \
                      (title, description, datecreated)
        cursor.execute(sql_command)
        	

        return sql_command

    @classmethod
    def get_all_entries(cls):
        """Method to get all entries"""
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

    @classmethod
    def get_entry(cls, entry_id):
        """Method to get an entry by id"""
        cursor.execute('SELECT * FROM "public"."entries"')
        rows = cursor.fetchall()

        list_dict = []

        for item in rows:
            z = {}

            z['id'] = item[0]
            z['title'] = item[1]
            z["description"] = item[2]
            z['datecreated'] = item[3]
            list_dict.append(z)

        entry = list_dict[entry_id]

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
    def entry_exists(cls, title):
        """Method to check whether an entry exists"""
        for entry in cls.entries:
            if entry.title == title:
                return True
        return False
