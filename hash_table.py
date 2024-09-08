class HashTable:

    # creating a constructor with a inital list of 7(prime number) and the initial value of that list contains None.
    def __init__(self, size=7) -> None:
        # A list of size 7 containing None value in each one.
        self.data_map = [None] * size

    # Now defining a hasmap which will operate on the key and return the index where to store the key value pair

    def __hash(self, key: str) -> int:
        """
        This helper method will take the key of the hash map and returns the index where to store the key value pair.
        """
        hash_value = 0
        for letter in key:
            hash_value = (hash_value + ord(hash_value)
                          * 23) % len(self.data_map)
        return hash_value

    def print_table(self):
        for index, value in enumerate(self.data_map):
            print(f"{index} : {value}")


hash_map = HashTable()
hash_map.print_table()

