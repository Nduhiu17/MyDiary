import os
import psycopg2


class Database:

    def __init__(self):
        self.db = os.environ['DATABASE_URL']
        self.connection = psycopg2.connect(self.db)
        self.connection.autocommit = True
        self.cursor = self.connection.cursor()

    def create_users_table(self):
        sql_command = """ CREATE TABLE users (
                id SERIAL PRIMARY KEY,
                username VARCHAR(80) NOT NULL,
                firstname VARCHAR(80) NOT NULL,
                secondname VARCHAR(80) NOT NULL,
                email VARCHAR(80) NOT NULL,
                password VARCHAR(80) NOT NULL
                )
                """
        self.cursor.execute(sql_command)

    def drop_users_table(self):
        sql_command = """ 
        
                      DROP TABLE users;
                      """
        self.cursor.execute(sql_command)

    # def create_entries_table(self,cursor):
    #     sql_command = """ CREATE TABLE entries (
    #             id SERIAL ,
    #             title VARCHAR(80) NOT NULL,
    #             description VARCHAR(350) NOT NULL,
    #             date_created VARCHAR(20),
    #             userId INTEGER NOT NULL,
    #             )
    #             """
    #     cursor.execute(self,sql_command)

    # def main(self,config=None):
    #     conn = createdb_con(config=config)
    #     with conn.cursor() as cursor:
    #         cursor.execute("""DROP TABLE IF EXISTS entries CASCADE""" )
    #         create_entries_table(cursor)
    #         conn.commit()

    #     print('entries table created successfully')

# if __name__ == '__main__':
#     main()
