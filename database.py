import os
import psycopg2

# export DATABASE_URL="postgres://jkxwwyumvnralw:7da5145d4d847858d077725513fb772ce186f8f263e7e203bc9ffb277619465e@ec2-50-19-86-139.compute-1.amazonaws.com:5432/dfnto48h4ufbi7"


class Database:
    # Method that defines variables
    def __init__(self):
        self.db = os.environ['DATABASE_URL']
        self.connection = psycopg2.connect(self.db)
        self.connection.autocommit = True
        self.cursor = self.connection.cursor()

    # method that creates table users
    def create_users_table(self):
        sql_command = """ CREATE TABLE IF NOT EXISTS  users (
            id SERIAL PRIMARY KEY,
            username VARCHAR(255) NOT NULL,
            email VARCHAR(255) NOT NULL UNIQUE,
            password VARCHAR(225) NOT NULL
                )
                """
        self.cursor.execute(sql_command)

    # method that creates entries table
    def create_entries_table(self):
        sql_command = """ 
        CREATE TABLE IF NOT EXISTS "public"."entries"  (
            id SERIAL ,
            user_id INTEGER NOT NULL,
            date_created VARCHAR(80),
            date_modified VARCHAR(80),
            title VARCHAR(255) NOT NULL,
            description TEXT NOT NULL,
            PRIMARY KEY (user_id,id),
            FOREIGN KEY (user_id)
            REFERENCES users (id)
                )
                """
        self.cursor.execute(sql_command)

    # method that drops users table
    def drop_users_table(self):
        sql_command = """ 

                      DROP TABLE users;
                      """
        self.cursor.execute(sql_command)

    # method that drops entries table
    def drop_entries_table(self):
        sql_command = """ 

                      DROP TABLE entries;
                      """
        self.cursor.execute(sql_command)
