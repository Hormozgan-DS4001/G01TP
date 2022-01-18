from typing import List, Optional


class DArray:
    class IndexHandler:
        def __init__(self, array, index):
            self.array = array
            self.index = index

        def has_next(self):
            return self.index + 1 < len(self.array)

        def has_prev(self):
            return self.index > 0

        def copy(self):
            return DArray.IndexHandler(self.array, self.index)

        def get(self):
            return self.array[self.index]

        def traverse(self, reverse=False):
            if not reverse:
                while self.index < len(self.array):
                    yield self.array[self.index]
                    self.index += 1
            else:
                while self.index >= 0:
                    yield self.array[self.index]
                    self.index -= 1

    def __init__(self, capacity=10):
        self.length = 0
        self.capacity = capacity
        self.array = [None] * self.capacity

    def __len__(self):
        return self.length

    def __getitem__(self, item):
        assert 0 <= item < self.length
        return self.array[item]

    def __setitem__(self, key, value):
        assert 0 <= key < self.length, 'Index out of range'
        self.array[key] = value

    def is_empty(self):
        return self.length == 0

    def append(self, data):
        if self.capacity == self.length:
            self._resize(2 * self.capacity)
        self.array[self.length] = data
        self.length += 1

    def _resize(self, capacity):
        a = [None] * capacity
        for i in range(self.length):
            a[i] = self.array[i]
        self.capacity = capacity
        self.array = a

    def pop(self):
        assert not self.is_empty()
        self.length -= 1
        a = self.array[self.length]
        if self.is_empty():
            pass
        else:
            if self.capacity % self.length == 0:
                self._resize(int(self.capacity / 2))
        return a

    def __repr__(self):
        return "DArray" + repr(self.array[:self.length])

    def get_node_handler(self, index=0):
        return self.IndexHandler(self, index)


class Sll:

    class _Node:
        def __init__(self, data):
            self.data = data
            self.next = None

    def __init__(self):
        self.head = None
        self.tail = None

    def __iter__(self):
        t = self.head
        while t:
            yield t.data
            t = t.next

    def copy(self):
        new_sll = Sll()
        for i in self:
            new_sll.append(i)
        return new_sll

    def append(self, data):
        new_node = self._Node(data)
        if self.head is None:
            self.head = new_node
            self.tail = new_node
            return
        self.tail.next = new_node
        self.tail = new_node

    def prepend(self, data):
        new_node = self._Node(data)
        if self.head is None:
            self.head = new_node
            self.tail = new_node
            return
        new_node.next = self.head
        self.head = new_node


class HashTable:
    class _Node:
        def __init__(self, key, value):
            self.key = key
            self.value = value

    def __init__(self, size: int = 30):
        self.array: List[Optional[HashTable._Node]] = [None] * size
        self.size = size
        self.count = 0

    def __getitem__(self, key):
        for i in range(self.size):
            index = self._hash_function(key, i)
            if self.array[index] is None:
                raise KeyError(f"Not found {key.data}")
            elif self.array[index].key == key:
                return self.array[index].value

    def __setitem__(self, key, value):
        if self.count >= 0.75 * self.size and self.count >= 2000:
            self._extend()
        new_node = HashTable._Node(key, value)
        for i in range(self.size):
            index = self._hash_function(key, i)
            if self.array[index] is None:
                self.array[index] = new_node
                self.count += 1
                return
            elif self.array[index].key == key:
                self.array[index].value = value
                return
        raise ValueError("Hashtable is full")

    def __iter__(self):
        count = 0
        while count < self.size:
            if self.array[count] is not None:
                yield self.array[count].key
            count += 1

    def __contains__(self, item):
        if item in self.key():
            return True
        return False

    def _hash_function(self, x, i):
        return (hash(x) + i) % self.size

    def _extend(self):
        old_array = self.array
        self.size *= 2
        self.array = [None] * self.size
        self.count = 0
        for element in old_array:
            if isinstance(element, HashTable._Node):
                for i in range(self.size):
                    index = self._hash_function(element.key, i)
                    if self.array[index] is None:
                        self.array[index] = element
                        self.count += 1
                        break

    def key(self):
        count = 0
        while count < self.size:
            if self.array[count] is not None:
                yield self.array[count].key
            count += 1


class Trie:

    class Node:
        def __init__(self):
            self.children = HashTable()
            self.values = Sll()

    def __init__(self):
        self.root: Trie.Node = Trie.Node()

    def insert(self, key: str, value):
        t = self.root
        for char in key:
            if char not in t.children:
                t.children[char] = Trie.Node()
            t = t.children[char]
        t.values.append(value)

    __setitem__ = insert

    def find_exact(self, text: str):
        t = self.root
        for char in text:
            if char not in t.children:
                return None
            t = t.children[char]
        if t.values:
            return t.values.copy()

    def find_prefix(self, text: str):
        t = self.root
        for char in text:
            if char not in t.children:
                return None
            t = t.children[char]
        yield from self._find_prefix_helper(t)

    def _find_prefix_helper(self, root: "Trie.Node"):
        for i in root.values:
            yield i
        for i in root.children:
            yield from self._find_prefix_helper(root.children[i])


class HashTableCamera:
    class _Node:
        def __init__(self, key, value):
            self.key = key
            self.value = value

    def __init__(self, size: int = 2000):
        self.array: List[Optional[HashTableCamera._Node]] = [None] * size
        self.size = size
        self.count = 0

    def __getitem__(self, key):
        if self.size == 8000:
            if self.array[key - 1000] is None:
                return
            return self.array[key - 1000]

        for i in range(self.size):
            index = self._hash_function(key, i)
            if self.array[index] is None:
                return

            elif self.array[index].key == key:
                return self.array[index].value

    def __setitem__(self, key, value):
        if self.size == 8000:
            if self.array[key - 1000] is None:
                self.array[key - 1000] = value
                self.count += 1
                return
            return False

        if self.count >= 0.75 * self.size:
            self._extend()
        new_node = HashTableCamera._Node(key, value)
        for i in range(self.size):
            index = self._hash_function(key, i)
            if self.array[index] is None:
                self.array[index] = new_node
                self.count += 1
                return
            elif self.array[index].key == key:
                return False
        raise ValueError("Hashtable is full")

    def __iter__(self):
        count = -1
        while count < self.size:
            count += 1
            if self.array[count] is None:
                continue
            else:
                yield self.array[count].key, self.array[count].value

    def _hash_function(self, x, i):
        if self.size == 8000:
            return x - 1000
        return (hash(x) + i) % self.size

    def _extend(self):
        old_array = self.array
        self.size *= 2
        self.array = [None] * self.size
        self.count = 0
        for element in old_array:
            if isinstance(element, HashTableCamera._Node):
                for i in range(self.size):
                    index = self._hash_function(element.key, i)
                    if self.array[index] is None:
                        self.array[index] = element
                        self.count += 1
                        break

    def values(self):
        count = -1
        while count < self.size:
            count += 1
            if self.array[count] is None:
                continue
            else:
                yield self.array[count].value

    def key(self):
        count = -1
        while count < self.size:
            count += 1
            if self.array[count] is None:
                continue
            else:
                yield self.array[count].key


class BST:

    class _Node:
        def __init__(self, data, key):
            self.left = None
            self.right = None
            self.data = data
            self.key = key

    def __init__(self):
        self.root = None
        self.length = 0

    def __len__(self):
        return self.length

    def insert(self, data, key):
        new_node = self._Node(data, key)
        self._insert_bst(new_node, key)
        self.length += 1

    def find(self, key):
        t = self.root
        if not t:
            return
        while True:
            if t.key == key:
                return t
            elif t.key > key:
                t = t.left
            else:
                t = t.right

    def _insert_bst(self, node, key):
        t = self.root
        if not t:
            self.root = node
            return
        while True:
            if t.key > key:
                if t.left:
                    t = t.left
                else:
                    t.left = node
                    break
            if t.key < key:
                if t.right:
                    t = t.right
                else:
                    t.right = node
                    break

