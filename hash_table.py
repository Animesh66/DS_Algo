class HashTable:

    # creating a constructor with an initial list of 7(prime number) and the initial value of that list contains None.
    def __init__(self, size=7) -> None:
        # A list of size 7 containing None value in each one.
        self.__data_map = [None] * size

    # Now defining a hashmap which will operate on the key and return the index where to store the key-value pair

    def __hash(self, key: str) -> int:
        """
        This helper method will take the key of the hash map and returns the index where to store the key-value pair.
        """
        hash_value = 0
        for letter in key:
            hash_value = (hash_value + ord(letter)
                          * 23) % len(self.__data_map)
        return hash_value

    def print_table(self):
        for index, value in enumerate(self.__data_map):
            print(f"{index} : {value}")

    def set_item(self, key: str, value: int) -> None:
        """
        Method to set the value of key-value pair at the given index.
        """
        index = self.__hash(key)
        if self.__data_map[index] == None:
            self.__data_map[index] = []
        self.__data_map[index].append([key, value])

    def get_item(self, key: str) -> int | None:
        """
        Method to get the item of the given key.
        """
        # First get the index of the key from the hash function
        index = self.__hash(key)
        # Go to the index of the data map and check the value exists
        if self.__data_map[index] is not None:
            for i in range(len(self.__data_map[index])):
                if self.__data_map[index][i][0] == key:
                    return self.__data_map[index][i][1]
        return None


hash_map = HashTable()
hash_map.set_item('bolts', 1400)
hash_map.set_item('washers', 50)
hash_map.set_item('lumber', 70)
print(hash_map.get_item('bolts'))
print(hash_map.get_item('abc'))
# hash_map.print_table()
