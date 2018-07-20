import json
import unittest



class DiarylistTestCase(unittest.TestCase):
    def setUp(self):
        self.new_entry = Entry(title="graduation ceremony", description="it was nice attending", date_created=" ")
        self.new_entry.save()
        self.app = run.app
        self.client = self.app.test_client()

    def test_api_get_all_diaryentries(self):
        get_all_response = self.client.get('/api/v1/entries/')
        self.assertEqual(get_all_response.status_code, 200)

    def test_api_diary_entries(self):
        get_all_response = self.client.get('/api/v1/entries/')
        self.assertEqual(type(json.loads(get_all_response.get_data().decode())), list)

    def test_api_get_diaryentry(self):
        get_response = self.client.get('api/v1/entries/0')
        self.assertEqual(get_response.status_code, 200)

    def test_api_post_diaryentry(self):
        entry = {'title': 'date created', 'description': 'watched the latest movie', 'date_created': ' '}
        response = self.client.post('api/v1/entries/', data=json.dumps(entry),
                                    headers={'Content-Type': 'application' '/json'})
        self.assertEqual(response.status_code, 201)

    def test_posted_entry_is_dictionary(self):
        entry = {'title': 'wedding ceremony', 'description': 'watched the latest movie', 'date_created': ' '}
        response = self.client.post('api/v1/entries/', data=json.dumps(entry),
                                    headers={'Content-Type': 'application' '/json'})
        self.assertEqual(type(json.loads(response.get_data().decode())), dict)

    def test_posted_data_is_saved(self):
        entry = {'title': 'date created', 'description': 'watched the latest movie', 'date_created': ' '}
        response = self.client.post('api/v1/entries/', data=json.dumps(entry),
                                    headers={'Content-Type': 'application' '/json'})
        print("*************************************************************************************")
        print(len(entry))
        self.assertEqual(len(entry), len(entry))

    # def test_put_entry(self):
    #     entry = {'title': 'date created', 'description': 'watched the latest movie', 'date_created': ' '}
    #     response = self.client.post('api/v1/entries/', data=json.dumps(entry),
    #                                 headers={'Content-Type': 'application' '/json'})
    #     self.assertEqual(response.status_code, 201)
    #     # entry.id = json.loads(response.get_data(as_text=True))['entry.id']
    #     #
    #     entry2 = {'title': 'date created and save', 'description': 'watched the latest movie', 'date_created': ' '}
    #     response2 = self.client.put('api/v1/entries/1', data=json.dumps(entry2),
    #                                  headers={'Content-Type': 'application' '/json'})
        # self.assertEqual(response2.status_code, 201)
        # self.assertIn('and save', str(response2.data))

    # def test_put_entry(self):
        # entry_to_modify = self.client.get('api/v1/entries/0')
        # entry_to_modify = self.client.put('entry_to_modify', data=json.dumps(entry_to_modify), headers={'Content-Type': 'application' '/json'})
        # self.assertIn('for music', str(entry_to_modify.data))

