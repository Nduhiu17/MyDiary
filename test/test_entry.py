import unittest
from app.models import Entry


class TestEntry(unittest.TestCase):
    def tearDown(self):
        Entry.entries = []

    def test_entry_init(self):
        """Test Entry object initializes"""
        new_entry = Entry(title="graduation ceremony", description="it was nice attending.", date_created=" ")
        self.assertEqual(new_entry.title, "graduation ceremony")

    def setUp(self):
        self.new_entry = Entry(title="graduation ceremony", description="it was nice attending", date_created=" ")
        self.new_entry.save()

    def test_save(self):
        """Test an entry can be saved"""
        new_entry = self.new_entry
        new_entry.save()
        self.assertEqual(len(Entry.entries), 2)

    def test_get_all_entries(self):
        """Test all entries can be gotten"""
        self.assertEqual(len(Entry.get_all_entries()), 1)

    def test_get_entry(self, id=0):
        """Test an entry can be gotten by id"""
        entry = Entry.get_entry(id)
        self.assertEqual(entry.title, "graduation ceremony")

    def test_save_multiple_entries(self):
        """Test multiple entries can be saved"""
        self.new_entry.save()
        test_entry = Entry("world cup Russia", "it was awesome attending", " ")
        test_entry.save()
        self.assertEqual(len(Entry.entries), 3)

    def test_modify_entry(self, id=0):
        """Test an entry can be saved"""
        entry_to_modify = Entry.get_entry(id)
        entry_to_modify.title = "tech open day"
        entry_to_modify.description = "it was astonishing"
        entry_to_modify.date_created = " "
        modified_entry = Entry.modify_entry(id, entry_to_modify)
        self.assertEqual(modified_entry.title, "tech open day")
        self.assertEqual(modified_entry.date_created, " ")
    
    def test_delete_entry(self):
        """Test an entry can be deleted"""
        self.new_entry.save()
        new_entry = Entry("Silicon Seminar", "theme will be tech influence in economic prosperity", " 3235652")
        new_entry.save()
        self.new_entry.delete()
        self.assertEqual(len(Entry.entries),21)

    def test_entry_exists(self):
        """Test an entry exists"""
        self.new_entry.save()
        new_entry = Entry("attend my garden", "plant some seedlings since its a rainy season", "44444")
        new_entry.save()
        entry_exist = Entry.entry_exists('attend my garden')
        self.assertTrue(entry_exist)


