class Entry:
    entries = []

    def __init__(self, title, description, date_created):
        """Method to initialize Entry class"""

        self.title = title
        self.description = description
        self.date_created = date_created

    def save(self):
        """Method to save an entry"""
        self.entries.append(self)

    @classmethod
    def get_all_entries(cls):
        """Method to get all entries"""
        entries = cls.entries
        my_entries_json = []
        for entry in entries:
            my_entries_json.append(entry.__dict__)
        return my_entries_json

    @classmethod
    def get_entry(cls, entry_id):
        """Method to get an entry by id"""
        entry = cls.entries[entry_id]
        return entry

    @classmethod
    def modify_entry(cls, id, modified_object):
        """Method to modify an entry"""
        cls.entries[id] = modified_object
        return modified_object

    def delete(self):
        """Method to delete an entry"""
        Entry.entries.remove(self)

    
    @classmethod
    def entry_exists(cls,title):
        """Method to check whether an entry exists"""
        for entry in cls.entries:
            if entry.title == title:
                return True
        return False
