class card():
    def __init__(self, ID=0, name='', value=''):
        self.ID = ID
        self.name = name
        self.value = value

    def get_ID(self):
        return self.ID

    def get_name(self):
        return self.name

    def get_value(self):
        return self.value

    def __str__(self):
        string= self.name
        return string

    def __repr__(self):
        return self.name