# create python dictionaries from scratch using hash tables.
"""
Implement a hashtable class that supports the following operations:
 1. Insert a new key-value pair
 2. find value associated with the key
 3. update the value associated with the key
 4. list all keys in the hash table
"""
"""phone_numbers = {
    'Akash' : '987654321',
    'Haddish' : '123456789',
    'kunta' : '678954321'
}
print(phone_numbers)

phone_numbers['kinte'] = '8989898989'
print(phone_numbers)
"""
# create a list to store data of lenght 4096
data_list = [None] * 4096


# convert character into integer using the ord built in function 
def get_index(data_list, a_string):
    result = 0
    for char in a_string:
        """convert character to an integer"""
        num = ord(char)
        # update result by adding the number
        result += num

    # take the remainder of the result with the size of data list(4096)
    list_index = result % len(data_list)
    return list_index



class HashTable:
    def __init__(self):
        """create a list of size 4096 with all values NONE"""
        self.data_list = [None] * 4096

    def insert(self, key, value):
        """ insert keys and value pairs"""
        idx = get_index(self.data_list, key)
        self.data_list[idx] = key, value

    def find(self, key):
        """find the index for the key using get_idex
            - retrieve the data stored at the index using key-value pair
            - return: value if found , else return None
        """
        idx = get_index(self.data_list, key)
        kv = self.data_list[idx]
        if kv is None:
            return None
        else:
            key, value = kv
            return value

    def update(self, key, value):
        """get the index for the key using get_index and
        store the new key-value pair at the right index"""

        idx = get_index(self.data_list, key)
        self.data_list[idx] = key, value

    def list_all(self):
        # find key from each key-value pair 
        return [kv[0] for kv in self.data_list if kv is not None]


table = HashTable()
table.insert('Kunta', '989898989')
table.insert('Vumbi', '987654321')

print(table)