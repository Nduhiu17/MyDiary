class Entry:
    entries = []

    def __init__(self, title, description, date_created):
        self.title = title
        self.description = description
        self.date_created = date_created

    def save(self):
        self.entries.append(self)

    @classmethod
    def get_all_entries(cls):
        entries = cls.entries
        my_entries_json = []
        for entry in entries:
            my_entries_json.append(entry.__dict__)
        return my_entries_json

    @classmethod
    def get_entry(cls, entry_id):
        entry = cls.entries[entry_id]
        return entry

    @classmethod
    def modify_entry(cls, id, modified_object):
        cls.entries[id] = modified_object
        return modified_object

    def delete(self):
        Entry.entries.remove(self)

