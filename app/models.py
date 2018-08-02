import os
from datetime import datetime

import psycopg2
from passlib.handlers.pbkdf2 import pbkdf2_sha256

try:
    # connect_str = "dbname='diary_db' user='antony' host='localhost' " + \
    #               "password='password'"
    # connect_str = "dbname='diary_db_test' user='postgres' host='localhost' " + \
    #   "password='postgres'"
    connect_str = "dbname='dfnto48h4ufbi7' user='jkxwwyumvnralw' host='ec2-50-19-86-139.compute-1.amazonaws.com' " + \
                  "password='7da5145d4d847858d077725513fb772ce186f8f263e7e203bc9ffb277619465e'"
    # enabled for testing
    # os.environ['DATABASE_URL'] = connect_str
    conn = psycopg2.connect(os.environ['DATABASE_URL'])
    conn.autocommit = True
    cursor = conn.cursor()
    print("db connectd!!!")

except Exception as e:
    print("can't connect. Invalid dbname, user or password?")
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

    @classmethod
    def get_entry(cls,id):
        """Method to get an entry by id"""
        cursor.execute('SELECT * FROM "public"."entries" WHERE id=%s', (id,))
        row = cursor.fetchone()

        return{
            "id":row[0],
            "user_id":row[1],
            "date_created":row[2],
            "date_modified":row[3],
            "title":row[4],
            "description":row[5]
        }

    @classmethod
    def delete(cls,id):
        try:
            cursor.execute('DELETE FROM public.entries WHERE id = %s', (id,))
            return "success"
        except:
            return "failed"

    @classmethod
    def update(cls, title, description,id):
        """Method to save an entry"""

        format_str = f"""
        UPDATE public.entries SET title = '{title}', description = '{description}', date_modified = '{str(datetime.now())}' WHERE id = {id};
        """
        # format_str = f"""
        # INSERT INTO public.entries (user_id,title,description,date_created,date_modified)
        # VALUES ('{user_id}','{title}','{description}','{str(datetime.now())}','{str(datetime.now())}') ;
        # """
        cursor.execute(format_str)

        return {
            "date_modified": str(datetime.now()),
            "title": title,
            "description": description
        }

class User:

    # this method registers a user in the database
    @classmethod
    def save(cls, username, email, password):
        found_user = cls.find_by_email(email)
        if found_user != False:
            return {'status': "failed", "message": 'email already registered'}
        format_str = f"""
        INSERT INTO public.users (username,email,password)
        VALUES ('{username}','{email}','{password}');
        """
        cursor.execute(format_str)

        return {
            "username": username,
            "email": email,
            # "token": password,
        }

    # This method gets a user using email
    @classmethod
    def find_by_email(cls, email):
        try:
            cursor.execute("select * from users where email = %s", (email,))
            user = cursor.fetchone()
            return list(user)
        except Exception as e:
            return False

    # method to generate hash from the password
    @staticmethod
    def generate_hash(password):
        return pbkdf2_sha256.hash(password)


    # method to verify the harshed password
    @staticmethod
    def verify_hash(password, hash):
        # hash = pbkdf2_sha256.encrypt("toomanysecrets")
        # print("im here",pbkdf2_sha256.verify(password, hash))
        return pbkdf2_sha256.verify(password,hash)
