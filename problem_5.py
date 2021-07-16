import hashlib
import time


class Block:
    def __init__(self, data, previous_hash):
        self.timestamp = time.strftime("%a, %d %b %Y %I:%M:%S %p %Z", time.gmtime())
        self.data = data
        self.previous_hash = previous_hash
        self.hash = self.calc_hash(self.data)
        self.next = None
        self.prev = None

    def calc_hash(self, hash_str):
        sha = hashlib.sha256()
        hash_str = "We are going to encode this string of data!".encode('utf-8')
        sha.update(hash_str)
        return sha.hexdigest()


class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def append(self, data):
        if self.head is None:
            self.head = Block(data, 0)
            self.tail = self.head
            return

        self.tail.next = Block(data, self.tail.hash)
        self.tail.next.previous = self.tail
        self.tail = self.tail.next
        return

    def __str__(self):
        cur_head = self.head
        out_string = ""
        while cur_head:
            out_string += '|' + cur_head.timestamp + ',' + str(cur_head.data) + ',' + cur_head.hash + ',' + str(
                cur_head.previous_hash) + '|' + " <- "
            cur_head = cur_head.next
        return out_string

    def size(self):
        size = 0
        node = self.head
        while node:
            size += 1
            node = node.next

        return size

b1 = LinkedList()
b1.append('my first blockchain')
b1.append('second blockchain')
b1.append('third blockchain')
b1.append('forth blockchain')
print(b1)

# Test 2: empty blocks
b2 = LinkedList()
try:
    b2.append() #raise error when trying to create a block with no data
except TypeError:
    print("Data is a required input to the block")

# Test 3: intput data has to be integer type
b3 = LinkedList()
b3.append(1)

'''
Output
|Thu, 15 Jul 2021 09:40:20 PM Central Standard Time,
my first blockchain,a20200a94c75010576e2d6a83e6fa69271901a9d805894b28bd91e6054fbfd10,0| <- 
|Thu, 15 Jul 2021 09:40:20 PM Central Standard Time,
second blockchain,a20200a94c75010576e2d6a83e6fa69271901a9d805894b28bd91e6054fbfd10,a20200a94c75010576e2d6a83e6fa69271901a9d805894b28bd91e6054fbfd10| <- 
|Thu, 15 Jul 2021 09:40:20 PM Central Standard Time,
third blockchain,a20200a94c75010576e2d6a83e6fa69271901a9d805894b28bd91e6054fbfd10,a20200a94c75010576e2d6a83e6fa69271901a9d805894b28bd91e6054fbfd10| <- 
|Thu, 15 Jul 2021 09:40:20 PM Central Standard Time,forth blockchain,a20200a94c75010576e2d6a83e6fa69271901a9d805894b28bd91e6054fbfd10,a20200a94c75010576e2d6a83e6fa69271901a9d805894b28bd91e6054fbfd10| <- 
Data is a required input to the block
'''