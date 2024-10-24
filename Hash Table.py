class HashTable:
    def __init__(self, size=10):
        # Initialize the hash table with a fixed size
        self.size = size
        self.table = [[] for _ in range(size)]

    def _hash(self, key):
        # Compute the hash value for a given key
        return hash(key) % self.size

    def insert(self, key, value):
        # Insert a key-value pair into the hash table
        hash_key = self._hash(key)
        for kvp in self.table[hash_key]:
            if kvp[0] == key:
                kvp[1] = value
                return
        self.table[hash_key].append([key, value])

    def search(self, key):
        # Search for a value by key in the hash table
        hash_key = self._hash(key)
        for kvp in self.table[hash_key]:
            if kvp[0] == key:
                return kvp[1]
        return None

    def delete(self, key):
        # Delete a key-value pair from the hash table
        hash_key = self._hash(key)
        for i, kvp in enumerate(self.table[hash_key]):
            if kvp[0] == key:
                del self.table[hash_key][i]
                return True
        return False

    def print_table(self):
        # Print the hash table
        for i, bucket in enumerate(self.table):
            print(f"Bucket {i}: {bucket}")

if __name__ == "__main__":
    # Create an instance of HashTable
    ht = HashTable()
    # Insert key-value pairs into the hash table
    ht.insert("apple", 1)
    ht.insert("banana", 2)
    ht.insert("orange", 3)
    ht.insert("grape", 4)

    print("Hash table:")
    ht.print_table()

    print("\nSearch for 'banana':")
    print(ht.search("banana"))

    print("\nDelete 'orange':")
    ht.delete("orange")
    ht.print_table()