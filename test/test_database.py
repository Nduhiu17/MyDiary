import unittest
import os

from database import Database


class DatabaseTestCase(unittest.TestCase):
    def setUp(self):
        connect_str = "dbname='diary_test' user='postgres' host='localhost' " + "password='postgres'"
        os.environ['DATABASE_URL'] = connect_str
        self.db = Database()
        self.db.create_users_table()
        self.db.create_entries_table()


    def test_database_init(self):
        #test database initialization
        cursor = self.db.cursor
        cursor.execute('SELECT * FROM "public"."users"')
        rows = cursor.fetchall()
        print(rows)
        self.assertTrue(type(rows), list)

    def test_entries_table_created(self):
        #tests whether table entries is created
        cursor = self.db.cursor
        cursor.execute('SELECT * FROM "public"."entries"')
        rows = cursor.fetchall()
        print(rows)
        self.assertTrue(type(rows), list)

    def test_users_table_created(self):
        #tests table users is created
        cursor = self.db.cursor
        cursor.execute('SELECT * FROM "public"."users"')
        rows = cursor.fetchall()
        print(rows)
        self.assertTrue(type(rows), list)

    def test_table_drop(self):
        # test database table dropped
        cursor = self.db.cursor
        cursor.execute('SELECT EXISTS (SELECT 1 FROM "public"."entries")')
        rows = cursor.fetchall()
        print("test drop table",rows)
        self.assertTrue(rows,False)
