
class Node:
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.next = None
        self.prev = None


class LRU_Cache(object):

    def __init__(self, capacity=5):
        # Initialize class variables
        self.capacity = capacity
        self.cache = dict()
        # doubly linked list dummy
        self.head = Node(0, 0)
        self.tail = Node(0, 0)
        self.head.next = self.tail
        self.tail.prev = self.head

    def get(self, key):
        # Retrieve item from provided key. Return -1 if nonexistent. 
        if key in self.cache:
            node = self.cache[key] # get the node
            self._remove(node) 
            self._add(node)
            return node.value
        return -1

    def set(self, key, value):
        # Set the value if the key is not present in the cache. If the cache is at capacity remove the oldest item. 
        if key in self.cache:
            self._remove(self.cache[key])

        node = Node(key, value)
        self._add(node)
        self.cache[key] = node
        if len(self.cache) > self.capacity:
            # Remove from the list and delete the LRU from the dict
            lru = self.head.next
            self._remove(lru)
            del self.cache[lru.key]

    def _add(self, node):
        # Always add the new node right before tail
        prev = self.tail.prev
        prev.next = node
        node.prev = prev
        node.next = self.tail
        self.tail.prev = node

    def _remove(self, node):
        # Remove an existing node from the list
        prev = node.prev
        next = node.next
        prev.next = next
        next.prev = prev

our_cache = LRU_Cache(5)

our_cache.set(1, 1);
our_cache.set(2, 2);
our_cache.set(3, 3);
our_cache.set(4, 4);


our_cache.get(1)       # returns 1
our_cache.get(2)       # returns 2
our_cache.get(9)      # returns -1 because 9 is not present in the cache

our_cache.set(5, 5) 
our_cache.set(6, 6)

our_cache.get(3)      # returns -1 because the cache reached it's capacity and 3 was the least recently used entry

## Add your own test cases: include at least three test cases
## and two of them must include edge cases, such as null, empty or very large values

## Test Case 1
cache = LRU_Cache(2)
cache.set(1, 1)
cache.set(2, 2)
assert cache.get(1) == 1  # returns 1
cache.set(3, 3)           # evicts key 2
assert cache.get(2) == -1 # returns -1 (not found)

## Test Case 2
cache = LRU_Cache(2)
assert cache.get(999) == -1 # returns -1 (not found)

## Test Case 3
cache = LRU_Cache(1)
cache.set(1, 1)
cache.set(2, 2)            # evicts key 1
assert cache.get(1) == -1  # returns -1 (not found)
assert cache.get(2) == 2   # returns 2