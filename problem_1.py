# Your work here
# Using Hash map and Doubly Linked List
# LRU CACHE
class Node:
    # creating DLL
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.next = None
        self.prev = None


class LRU_Cache(object):

    # defining DLL nodes
    def __init__(self, capacity):
        self.capacity = capacity  # max capacity to hold
        self.hash_map = {}  # creating hash map
        self.head = Node(0, 0)  # creating dummy head node(0,0)
        self.tail = Node(0, 0)  # creating dummy tail node(0,0)
        # linking head and tail to each other
        self.head.next = self.tail
        self.tail.prev = self.head
        # None definition
        self.head.prev = None
        self.tail.next = None

    def add(self, key, value):
        # created new_node
        new_node = Node(key, value)
        # set curr to tail
        curr = self.head.next
        # linking new_node to tail part or curr pointer
        new_node.next = curr
        curr.prev = new_node
        # linking new_node to head part
        self.head.next = new_node
        new_node.prev = self.head
        # added new_node to hashmap
        self.hash_map[key] = new_node

    def delete(self, node):
        # take 2 pointer nxt and prev to node
        nxt = node.next
        prev = node.prev
        # assign and deleted node
        nxt.prev = prev
        prev.next = nxt
        node.next = None
        node.prev = None
        node = None

    def get(self, key):
        # if key in dictionary
        if key in self.hash_map:
            # delete node and get
            self.delete(self.hash_map[key])
            # and add to the most recent
            self.add(key, self.hash_map[key].value)
            return self.hash_map[key].value
        return -1

    def set(self, key, value):
        # if key already in dictionary
        if key in self.hash_map:
            self.delete(self.hash_map[key])  # delete the node at that key
            del self.hash_map[key]  # delete the value at that key
            self.add(key, value)  # add node to that key
        # else if len of hash_map == capacity
        elif len(self.hash_map) == self.capacity:
            # delete LRU node from dict
            del self.hash_map[self.tail.prev.key]
            # delete LRU node
            self.delete(self.tail.prev)
            # add new_node
            self.add(key, value)
        else:
            # add node to DLL and add to hash_map if key not in dict
            # add 1,2,3,4 limit 5
            self.add(key, value)

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
our_cache.get(3) # returns -1 because the cache reached it's capacity and 3 was the least recently used entry