class HashTable:
    def __init__(self, size):
        self.table = [None] * size

    def hash_function(self, key):
        return key % len(self.table)

    def insert(self, key, value):
        index = self.hash_function(key)
        self.table[index] = (key, value)

    def search(self, key):
        index = self.hash_function(key)
        if self.table[index] and self.table[index][0] == key:
            return self.table[index][1]
        return "Chave não encontrada"
