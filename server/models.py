class Entry():
    entries =[]

    def __init__(self, title, description, date_created):
        self.title = title
        self.description = description
        self.date_created = date_created

    def save(self):
        self.entries.append(self)

    @classmethod
    def get_all_entries(cls):
        return cls.entries

    @classmethod
    def get_entry(cls, id):
        entry = cls.entries[id]
        print("##############################################")
        print(entry.description)
        return entry

    @classmethod
    def modify_entry(cls, id, modified_object):
        cls.entries[id] = modified_object
        return modified_object