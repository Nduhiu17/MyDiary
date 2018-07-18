import json
import unittest

import run
from models import Entry

class DiarylistTestCase(unittest.TestCase):
    def setUp(self):
        self.new_entry = Entry(title="graduation ceremony", description="it was nice attending", date_created=" ")
        self.new_entry.save()
        self.app = run.app
        self.client = self.app.test_client()

    def test_api_get_all_diaryentries(self):
        get_all_response = self.client.get('/api/v1/entries')
        self.assertEqual(get_all_response.status_code, 200)
        self.assertEqual(type(json.loads(get_all_response.get_data().decode())), list)

    def test_api_get_diaryentry(self):
        get_response = self.client.get('api/v1/entries/'+'0')
        self.assertEqual(get_response.status_code,200)