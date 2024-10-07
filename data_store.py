from interface import DataStoreInterface
class DataStore(DataStoreInterface):
    def __init__(self):
        self.data = {}
        self.uncommited_data = {}
        self.in_transaction = False

    def begin(self):
        self.uncommited_data = self.data.copy()
        self.in_transaction = True
    
    def commit(self):
        self.data = self.uncommited_data.copy()
        self.uncommited_data = {}
        self.in_transaction = False
    
    def rollback(self):
        self.uncommited_data = {}
        self.in_transaction = False
    
    def set(self, key, value):
        if self.in_transaction:
            self.uncommited_data[key] = value
        else:
            self.data[key] = value

    def get(self, key):
        if key in self.uncommited_data:
            return self.uncommited_data[key]
        return self.data.get(key)
    

    def delete(self, key):
        if self.in_transaction:
            self.uncommited_data.pop(key, None)
        else:
            self.data.pop(key, None)
    