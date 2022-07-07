class Node:
    def __init__(self, data = None):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None # None()

    def append(self, data):
        new_node = Node(data)
        cur = self.head
        while cur.next != None:
            cur = cur.next
        cur.next = new_node

    def length(self):
        total = 0
        cur = self.head
        while cur.next != None:
            cur = cur.next
            total += 1
        return total

    def display(self):
        elems = []
        cur = self.head
        while cur.next != None:
            cur = cur.next
            elems.append(cur.data)
        return elems

    def get_index(self, index):
        if index >= self.length():
            raise IndexError
            return None
        cur_node = self.head
        cur_idx = 0
        while True:
            cur_node = cur_node.next
            if cur_idx == index:
                return cur_node.data
            cur_idx += 1


llist = LinkedList()
llist.head = Node(0)
llist.append(1)
llist.append(2)
llist.append(3)

print(llist.head.next.data)
print(llist.length())
print(llist.display())
print(f"Cur_node.data == {llist.get_index(0)}")