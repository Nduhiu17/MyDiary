import os
import psycopg2


class Database:

    def __init__(self):
        self.db = os.environ['DATABASE_URL']
        self.connection = psycopg2.connect(self.db)
        self.connection.autocommit = True
        self.cursor = self.connection.cursor()

    def create_users_table(self):
        sql_command = """ CREATE TABLE IF NOT EXISTS  users (
            id SERIAL PRIMARY KEY,
            username VARCHAR(255) NOT NULL,
            email VARCHAR(255) NOT NULL UNIQUE,
            password VARCHAR(225) NOT NULL
                )
                """
        self.cursor.execute(sql_command)

    def create_entries_table(self):
        sql_command = """ 
        CREATE TABLE IF NOT EXISTS "public"."entries"  (
            id SERIAL ,
            user_id INTEGER NOT NULL,
            date_created VARCHAR(80),
            title VARCHAR(255) NOT NULL,
            description TEXT NOT NULL,
            PRIMARY KEY (user_id,id),
            FOREIGN KEY (user_id)
            REFERENCES users (id)
                )
                """
        self.cursor.execute(sql_command)

    def drop_users_table(self):
        sql_command = """ 

                      DROP TABLE users;
                      """
        self.cursor.execute(sql_command)

    def drop_entries_table(self):
        sql_command = """ 

                      DROP TABLE entries;
                      """
        self.cursor.execute(sql_command)
