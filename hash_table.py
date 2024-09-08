class HashTable:

    # creating a constructor with a inital list of 7(prime number) and the initial value of that list contains None.
    def __init__(self, size=7) -> None:
        # A list of size 7 containing None value in each one.
        self.__data_map = [None] * size

    # Now defining a hasmap which will operate on the key and return the index where to store the key value pair

    def __hash(self, key: str) -> int:
        """
        This helper method will take the key of the hash map and returns the index where to store the key value pair.
        """
        hash_value = 0
        for letter in key:
            hash_value = (hash_value + ord(letter)
                          * 23) % len(self.__data_map)
        return hash_value

    def print_table(self):
        for index, value in enumerate(self.__data_map):
            print(f"{index} : {value}")

    def set_items(self, key: str, value: int) -> None:
        """
        Mehtod to set the value of key value pair at the given index.
        """
        index = self.__hash(key)
        if self.__data_map[index] == None:
            self.__data_map[index] = []
        self.__data_map[index].append([key, value])


hash_map = HashTable()
hash_map.set_items('bolts', 1400)
hash_map.set_items('washers', 50)
hash_map.set_items('lumber', 70)
hash_map.print_table()
