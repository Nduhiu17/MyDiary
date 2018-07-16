import unittest
from models import Entry

class TestEntry(unittest.TestCase):
    def tearDown(self):
        Entry.entries = []

    def test_entry_init(self):
        new_entry = Entry(title="graduation ceremony", description="it was nice attending.",date_created=" ")
        self.assertEqual(new_entry.title, "graduation ceremony")

    def setUp(self):
        self.new_entry = Entry(title="graduation ceremony",description="it was nice attending",date_created=" ")
        self.new_entry.save()

    def test_save(self):
        new_entry = self.new_entry
        new_entry.save()
        self.assertEqual(len(Entry.entries), 2)

    def test_get_all_entries(self):
        self.assertEqual(len(Entry.get_all_entries()), 1)
