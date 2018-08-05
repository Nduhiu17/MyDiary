import os
import inspect
import sys

from app import app
from database import Database
import unittest
import json


class RegistrationTestCase(unittest.TestCase):

    def tearDown(self):
        self.db.drop_entries_table()
        self.db.drop_users_table()

    def setUp(self):
        connect_str = "dbname='diary_db_test' user='postgres' host='localhost' " + "password='postgres'"
        os.environ['DATABASE_URL'] = connect_str
        self.db = Database()
        self.db.create_users_table()
        self.db.create_entries_table()
        self.app = app
        self.client = self.app.test_client()

    def register_user(self, username="nduhiu", email="nduhiu2020@gmail.com", password="password"):
        user = {
            "username": username,
            "email": email,
            "password": password
        }
        return self.client.post('/api/v1/register/', data=json.dumps(user), content_type='application/json')

    # def test_user_is_registered(self):
    #     """This tests sucessful user registration"""
    #     username = "nduhiu"
    #     email = "nduhiu2020@gmail.com"
    #     password = "password"
    #     user = {
    #         "username": username,
    #         "email": email,
    #         "password": password
    #     }
    #     response = self.client.post('/api/v1/register/', data=json.dumps(user),
    #                                 headers={'Content-Type': 'application/json'})
    #     self.assertEqual(response.status_code, 201)

    def test_registration_with_empty_password_field(self):
        """This tests registering a user with missing password"""
        username = "nduhiu"
        email = "nduhiu2020@gmail.com"
        password = " "
        user = {
            "username": username,
            "email": email,
            "password": password
        }
        response = self.client.post('/api/v1/register/', data=json.dumps(user),
                                    headers={'Content-Type': 'application/json'})
        self.assertEqual(response.status_code, 400)

    if __name__ == "__main__":
        unittest.main()
