import unittest
import os

from database import Database


class DatabaseTestCase(unittest.TestCase):
    def setUp(self):
        connect_str = "dbname='diary_db' user='postgres' host='localhost' " + "password='postgres'"
        os.environ['DATABASE_URL'] = connect_str
        self.db = Database()
        self.db.create_users_table()

    def tearDown(self):
        self.db.drop_users_table()

    #
    def test_database_init(self):
        cursor = self.db.cursor
        cursor.execute('SELECT * FROM "public"."users"')
        rows = cursor.fetchall()
        print(rows)
        self.assertTrue(type(rows), list)

# # #
#     def test_api_diary_entries(self):
#         """Test whether data stored is a list"""
#         get_all_response = self.client.get('/api/v1/entries/')
#         self.assertEqual(type(json.loads(get_all_response.get_data().decode())), list)
# #
#     def test_api_get_diaryentry(self, id=0):
#         """Test Api can get a single entry"""
#         get_response = self.client.get('api/v1/entries/0')
#         self.assertEqual(get_response.status_code, 200)
#
