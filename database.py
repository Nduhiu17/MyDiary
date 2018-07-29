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
                username VARCHAR(80) NOT NULL,
                firstname VARCHAR(80) NOT NULL,
                secondname VARCHAR(80) NOT NULL,
                email VARCHAR(80) NOT NULL,
                password VARCHAR(80) NOT NULL
                )
                """
        self.cursor.execute(sql_command)

    def create_entries_table(self):
        sql_command = """ 
        CREATE TABLE IF NOT EXISTS "public"."entries"  (
                id SERIAL PRIMARY KEY,
                title VARCHAR(80) NOT NULL,
                description VARCHAR(280) NOT NULL,
                datecreated VARCHAR(80) NOT NULL
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
