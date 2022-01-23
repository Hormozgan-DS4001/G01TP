from typing import List, Optional


class Dll:

    class _Node:
        def __init__(self, data):
            self.data = data
            self.next = None
            self.prev = None

    class NodeHandler:
        def __init__(self, dll,  node):
            self.dll = dll
            self.node = node

        def next(self):
            self.node = self.node.next

        def prev(self):
            self.node = self.node.prev

        def get(self):
            return self.node.data

        def copy(self):
            return Dll.NodeHandler(self.dll, self.node)

        def delete_node(self):

            if not self.node.next:
                self.dll.delete(len(self.dll) - 1)
            elif not self.node.prev:
                self.dll.delete(0)
            else:
                self.node.prev.next = self.node.next
                self.node.next.prev = self.node.prev
                self.dll._length -= 1

        def traverse(self, reverse=False):

            while True:
                if not reverse:
                    yield self.node.data
                    if not self.node.next:
                        break
                    self.node = self.node.next
                else:
                    yield self.node.data
                    if not self.node.prev:
                        break
                    self.node = self.node.prev

    def __init__(self):
        self.head = None
        self.tail = None
        self._length = 0

    def __len__(self):
        return self._length

    def __iter__(self):
        t = self.head
        while t:
            yield t.data
            t = t.next

    def __str__(self):
        if self._length == 0:
            return "DLL[]"
        result = "DLL["
        t = self.head
        while t:
            result += str(t.data) + ", "
            t = t.next
        return result[:-2] + "]"

    __repr__ = __str__

    def delete(self, index):
        assert 0 <= index < self._length

        if self._length == 1:
            self.head = None
            self.tail = None

        elif index == 0:
            self.head = self.head.next
            self.head.prev = None

        elif index == self._length - 1:
            self.tail = self.tail.prev
            self.tail.next = None

        else:
            del_node = self._get_node(index)
            del_node.perv.next = del_node.next
            del_node.next.prev = del_node.prev

        self._length -= 1

    def prepend(self, data):
        new_node = self._Node(data)
        if self._length == 0:
            self.head = new_node
            self.tail = new_node
        else:
            new_node.next = self.head
            self.head.prev = new_node
            self.head = new_node

    def append(self, data):
        new_node = self._Node(data)
        if self._length == 0:
            self.head = new_node
            self.tail = new_node

        else:
            self.tail.next = new_node
            new_node.prev = self.tail
            self.tail = new_node

        self._length += 1

    def _get_node(self, index):
        assert 0 <= index < self._length

        if self._length - index < index:
            t = self.tail
            counter = self._length
            while index < counter:
                t = t.prev
                counter -= 1

        else:
            t = self.head
            counter = 0
            while counter < index:
                t = t.next
                counter += 1
        return t

    def get_node_handler(self, index):
        return self.NodeHandler(self, self._get_node(index))


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
        if self.count >= 0.75 * self.size:
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

