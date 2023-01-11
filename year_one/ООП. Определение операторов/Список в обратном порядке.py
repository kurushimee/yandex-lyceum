class ReversedList:
    def __init__(self, data):
        self.data = data

    def __len__(self):
        return len(self.data)

    def __getitem__(self, key):
        return self.data[-(key + 1)]

    def __setitem__(self, key, value):
        self.data[-(key + 1)] = value
