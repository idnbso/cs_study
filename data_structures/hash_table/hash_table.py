from enum import Enum


class HashTable:
    def __init__(self, size=97):
        self.key_map = [None] * size

    def get(self, key):
        """
        O(1)
        :param key:
        :return:
        """
        key_index = self._hash(key)
        cur_value = self.key_map[key_index]
        if cur_value is None:
            return None

        value = [v for v in cur_value if v.key == key]
        return value[0].value if len(value) > 0 else None

    def set(self, key, value):
        """
        O(1)
        :param key:
        :param value:
        :return:
        """
        key_index = self._hash(key)
        cur_value = self.key_map[key_index]
        if cur_value is None:
            cur_value = []
        elif self.contains(key):
            self.remove(key)

        cur_value.append(Pair(key, value))
        self.key_map[key_index] = cur_value
        return self

    def remove(self, key):
        key_index = self._hash(key)
        cur_value = self.key_map[key_index]
        value = None
        for index in range(len(cur_value)):
            if cur_value[index].key == key:
                value = cur_value.pop(index)
        return value

    def contains(self, key):
        return self.get(key) is not None

    def keys(self):
        return self._get_items(ItemType.KEY.value[0])

    def values(self):
        return self._get_items(ItemType.VALUE.value)

    def _get_items(self, item_type):
        exists_key_map = list(filter(lambda k: k is not None, self.key_map))
        if exists_key_map is None or len(exists_key_map) == 0:
            return None

        items = []
        for chain_index, chain in enumerate(exists_key_map):
            for chain_item_index, chain_item in enumerate(chain):
                item = chain_item.key if item_type == 'key' else chain_item.value
                if item not in items:
                    items.append(item)

        return items

    def _hash(self, key):
        """
        Hash function for strings only
        :param key:
        :return:
        """
        total = 0
        prime = 31
        for index in range(min(len(key), 100)):
            char = key[index]
            value = ord(char) - ord('a')
            total = (total * prime + value) % len(self.key_map)
        return total

    def __str__(self):
        display = [kv for kv in self.key_map if kv is not None]
        return str(display)


class Pair():
    def __init__(self, key=None, value=None):
        self.key = key
        self.value = value

    def __repr__(self):
        return str(self.__dict__)


class ItemType(Enum):
    KEY = 'key',
    VALUE = 'value'


if __name__ == '__main__':
    ht = HashTable()
    print(ht.set('hello', 1332424).set('world', 1242453))
    print(ht.get('hello'))
    print(ht.get('world'))
    print(ht.get('test'))
    print(ht.set('hello', 1234567))
    print(ht.get('hello'))
    print(ht.keys())
    print(ht.values())
    print(ht)
