import json
import unittest

from server import run


class DiarylistTestCase(unittest.TestCase):
    def setUp(self):
        self.app = run.app
        self.client = self.app.test_client()

    def test_api_get_all_diaryentries(self):
        get_all_response = self.client.get('/api/v1/entries')
        self.assertEqual(get_all_response.status_code, 200)
        self.assertEqual(type(json.loads(get_all_response.get_data().decode())), list)
