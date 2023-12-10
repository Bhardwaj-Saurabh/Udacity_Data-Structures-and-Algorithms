
class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

    def __repr__(self):
        return str(self.value)

class LinkedList:
    def __init__(self):
        self.head = None
        self.end = None  # End pointer for efficient appending

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
            self.end = self.head
            return

        self.end.next = Node(value)
        self.end = self.end.next

    def size(self):
        size = 0
        node = self.head
        while node:
            size += 1
            node = node.next
        return size

    def to_set(self):
        result = set()
        node = self.head
        while node:
            result.add(node.value)
            node = node.next
        return result

def union(llist_1, llist_2):
    union_set = llist_1.to_set().union(llist_2.to_set())
    union_list = LinkedList()
    for value in union_set:
        union_list.append(value)
    return union_list

def intersection(llist_1, llist_2):
    intersection_set = llist_1.to_set().intersection(llist_2.to_set())
    if not intersection_set:
        return None
    intersection_list = LinkedList()
    for value in intersection_set:
        intersection_list.append(value)
    return intersection_list


## Test case 1

linked_list_1 = LinkedList()
linked_list_2 = LinkedList()

element_1 = [3,2,4,35,6,65,6,4,3,21]
element_2 = [6,32,4,9,6,1,11,21,1]

for i in element_1:
    linked_list_1.append(i)

for i in element_2:
    linked_list_2.append(i)

print (union(linked_list_1,linked_list_2))
print (intersection(linked_list_1,linked_list_2))

## Test case 2

linked_list_3 = LinkedList()
linked_list_4 = LinkedList()

element_1 = [3,2,4,35,6,65,6,4,3,23]
element_2 = [1,7,8,9,11,21,1]

for i in element_1:
    linked_list_3.append(i)

for i in element_2:
    linked_list_4.append(i)

print (union(linked_list_3,linked_list_4))
print (intersection(linked_list_3,linked_list_4))

## Add your own test cases: include at least three test cases
## and two of them must include edge cases, such as null, empty or very large values

## Test Case 3
linked_list_5 = LinkedList()
linked_list_6 = LinkedList()

print(union(linked_list_5, linked_list_6))
print(intersection(linked_list_5, linked_list_6))

## Test Case 4
linked_list_7 = LinkedList()
linked_list_8 = LinkedList()

for i in range(10000):  # Large list
    linked_list_7.append(i)
for i in range(5000, 15000):
    linked_list_8.append(i)

print(union(linked_list_7, linked_list_8).size())
print(intersection(linked_list_7, linked_list_8).size())

## Test Case 5
linked_list_9 = LinkedList()
linked_list_10 = LinkedList()

element_3 = [1, 2, 3]
for i in element_3:
    linked_list_9.append(i)

print(union(linked_list_9, linked_list_10))
print(intersection(linked_list_9, linked_list_10))