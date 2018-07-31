import json
import os
import unittest
from datetime import datetime

from app import app
from app.models import Entry
from database import Database


class DiarylistTestCase(unittest.TestCase):
    def setUp(self):
        connect_str = "dbname='diary_db_test' user='postgres' host='localhost' " + "password='postgres'"
        os.environ['DATABASE_URL'] = connect_str
        self.db = Database()
        self.db.create_entries_table()
        self.app = app
        self.client = self.app.test_client()

    def tearDown(self):
        self.db.drop_entries_table()

    def test_api_get_all_diaryentries(self):
        """Test API can get all entries(GET response)"""
        get_all_response = self.client.get('/api/v1/entries/')
        self.assertEqual(get_all_response.status_code, 200)

    def test_api_diary_entries(self):
        """Test whether data stored is a list"""
        get_all_response = self.client.get('/api/v1/entries/')
        self.assertEqual(type(json.loads(get_all_response.get_data().decode())), list)


    # def test_api_get_diaryentry(self, id=0):
    #     """Test Api can get a single entry"""
    #     get_response = self.client.get('api/v1/entries/0')
    #     self.assertEqual(get_response.status_code, 200)

    def test_api_post_diaryentry(self):
        """Test api can create an entry (POST response)"""
        entry = {'user_id':2,'title': 'test_title', 'description': 'watched the latest movie','date_created':str(datetime.now())}
        response = self.client.post('api/v1/entries/', data=json.dumps(entry),
                                    headers={'Content-Type': 'application' '/json'})
        self.assertEqual(response.status_code, 201)

    def test_posted_entry_is_dictionary(self):
        """Test whether created data is a dictionary"""
        entry = {'title': 'wedding ceremony', 'description': 'watched the latest movie'}
        response = self.client.post('api/v1/entries/', data=json.dumps(entry),
                                    headers={'Content-Type': 'application' '/json'})
        self.assertEqual(type(json.loads(response.get_data().decode())), dict)

    # def test_posted_data_is_saved(self):
    #     """Test Api can save data
    #     """
    #     entry = {'user_id':2,'title': 'wedding ceremony', 'description': 'watched the latest movie'}
    #     response = self.client.post('api/v1/entries/', data=json.dumps(entry),
    #                                 headers={'Content-Type': 'application' '/json'})

    #     get_all_response = self.client.get('/api/v1/entries/')
    #     self.assertTrue(len(json.loads(get_all_response.get_data().decode())) > 0)
#
#     def test_modify_entry(self):
#         """Test whether an Api can modify an entry"""
#         entry = {"title": "got a guiter", "description": "a good guiter for music", "date_created": "3226562"}
#         response = self.client.post('api/v1/entries/', data=json.dumps(entry),
#                                     headers={'Content-Type': 'application/json'})
#         self.assertEqual(response.status_code, 201)
#         item = {"title": "got a guiter", "description": "a good guiter for music", "date_created": "322656"}
#         response1 = self.client.post('api/v1/entries/', data=json.dumps(item),
#                                      headers={'Content-Type': 'application/json'})
#         self.assertEqual(response1.status_code, 201)
#         update = {"title": "got a guiter ", "description": "brand new guiter for playing music practice",
#                   "date_created": "2215652"}
#         response2 = self.client.put('api/v1/entries/0', data=json.dumps(update),
#                                     headers={'Content-Type': 'application/json'})
#         print("HHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHH")
#         print(response2)
#         self.assertEqual(response2.status_code, 201)
#
#     def test_delete_entry(self):
#         """Test Api can delete an entry"""
#         entry = {"title": "title for delete", "description": "this is content to delete", "date_created": "23256532"}
#         response = self.client.post('api/v1/entries/', data=json.dumps(entry), headers={'Content-Type': 'application/json'})
#         self.assertEqual(response.status_code, 201)
#         response2 = self.client.delete('api/v1/entries/1', headers={'Content-Type': 'application/json'})
#         self.assertEqual(response2.status_code, 200)
#
#
