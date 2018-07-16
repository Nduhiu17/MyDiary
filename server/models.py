class Entry():
    entries =[]

    def __init__(self, title, description, date_created):
        self.title = title
        self.description = description
        self.date_created = date_created

    def save(self):
        self.entries.append(self)

