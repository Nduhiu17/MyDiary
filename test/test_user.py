import json
import unittest

from app import app
from config import TestingConfig


class LoggingTestCase(unittest.TestCase):

    def setUp(self):
        """Define test variables and initialize app."""
        self.app = app
        self.app.config.from_object(TestingConfig)
        self.client = self.app.test_client()

    def register_user(self, email="user@gmail.com", password="password"):
        user = {
            "email": email,
            "password": password
        }
        return self.client.post('/api/v1/register/', data=json.dumps(user), content_type='application/json')

    def test_successful_user_login(self):
        self.register_user()
        login_user = {"email": "user@gmail.com", "password": "password"}
        login_response = self.client.post('/api/v1/login/', data=json.dumps(login_user),
                                          headers={'Content-Type': 'application/json'})
        self.assertEqual(login_response.status_code, 200)