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

    # def tearDown(self):
    #     self.db.drop_users_table()
    #     self.db.drop_entries_table()

    def test_database_init(self):
        cursor = self.db.cursor
        cursor.execute('SELECT * FROM "public"."users"')
        rows = cursor.fetchall()
        print(rows)
        self.assertTrue(type(rows), list)

    def test_entries_table_created(self):
        cursor = self.db.cursor
        cursor.execute('SELECT * FROM "public"."entries"')
        rows = cursor.fetchall()
        print(rows)
        self.assertTrue(type(rows), list)
