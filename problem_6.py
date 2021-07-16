class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

    def __repr__(self):
        return str(self.value)


class LinkedList:
    def __init__(self):
        self.head = None

    def __str__(self):
        cur_head = self.head
        out_string = ""
        while cur_head:
            out_string += str(cur_head.value) + " -> "
            cur_head = cur_head.next
        return out_string

    def append(self, value):

        if self.head is None:
            self.head = Node(value)
            return

        node = self.head
        while node.next:
            node = node.next

        node.next = Node(value)

    def size(self):
        size = 0
        node = self.head
        while node:
            size += 1
            node = node.next
        return size


def union(llist_1, llist_2):
    # Your Solution Here
    # final result list
    res = LinkedList()

    if llist_1.head is None and llist_2 is None:
        return None

    # stored in set1()
    set1 = set()
    head1 = llist_1.head
    while head1:
        set1.add(head1.value)
        head1 = head1.next

    # stored in set2()
    set2 = set()
    head2 = llist_2.head
    while head2:
        set2.add(head2.value)
        head2 = head2.next

    head_f = Node(None)
    # MERGE unique item to set1
    set1.update(set2)

    # convert set to list
    updated_list = list(set1)

    # convert list to Linked_list
    for i in range(len(updated_list)):
        res.append(updated_list[i])
    return res


def intersection(llist_1, llist_2):
    res = LinkedList()

    # Check if list1 and list2 is empty
    if llist_1.head is None and llist_2 is None:
        return None
    # create hash_map for incoming data
    set_1 = set()
    temp_1 = llist_1.head
    while temp_1:
        set_1.add(temp_1.value)
        temp_1 = temp_1.next

    set_2 = set()
    temp_2 = llist_2.head
    while temp_2:
        set_2.add(temp_2.value)
        temp_2 = temp_2.next

        temp_list = set_1.intersection(set_2)
        if len(temp_list) == 0:
            return None
    for item in temp_list:
        res.append(item)
    return res


# Test case 1

linked_list_1 = LinkedList()
linked_list_2 = LinkedList()

element_1 = [3, 2, 4, 35, 6, 65, 6, 4, 3, 21]
element_2 = [6, 32, 4, 9, 6, 1, 11, 21, 1]

for i in element_1:
    linked_list_1.append(i)

for i in element_2:
    linked_list_2.append(i)

print("\nTest case 1\n")
print("Union\t\t", union(linked_list_1, linked_list_2))
print("Intersection\t", intersection(linked_list_1, linked_list_2))

# Test case 2

linked_list_3 = LinkedList()
linked_list_4 = LinkedList()

element_1 = [3, 2, 4, 35, 6, 65, 6, 4, 3, 23]
element_2 = [1, 7, 8, 9, 11, 21, 1]

for i in element_1:
    linked_list_3.append(i)

for i in element_2:
    linked_list_4.append(i)
print("\nTest case 2\n")
print("Union\t\t", union(linked_list_3, linked_list_4))
print("Intersection\t\t", intersection(linked_list_3, linked_list_4))

'''

Test case 1

Union		 32 -> 65 -> 2 -> 35 -> 3 -> 4 -> 6 -> 1 -> 9 -> 11 -> 21 -> 
Intersection	 4 -> 21 -> 6 -> 

Test case 2

Union		 65 -> 2 -> 35 -> 3 -> 4 -> 6 -> 1 -> 7 -> 8 -> 9 -> 11 -> 21 -> 23 -> 
Intersection		 None

'''
