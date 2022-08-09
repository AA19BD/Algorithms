class Node:
    def __init__(self, data = None):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None # None()

    def append(self, data): #Push at the end
        new_node = Node(data)

        if self.head is None:
            self.head = new_node
            return

        cur = self.head
        while (cur.next):
            cur = cur.next
        cur.next = new_node

    def length(self):
        total = 0
        cur = self.head
        while (cur.next):
            cur = cur.next
            total += 1
        return total

    def display(self):
        elems = []
        cur = self.head
        while (cur.next):
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

    def push(self, data): #Push at front
        # 1 & 2: Allocate the Node &
        #        Put in the data
        new_node = Node(data)
        # 3. Make next of new Node as head
        new_node.next = self.head

        # 4. Move the head to point to new Node
        self.head = new_node

    def insertAfter(self, prev_node, data):
        #1 Check if prev_node exists
        if prev_node is None:
            print('The prev node must in LinkedList')
            return
        #2 Create new node and put data in
        new_node = Node(data)
        #3 Make next of new Node as next of prev_node
        new_node.next = prev_node.next
        # make next of prev_node as new_node
        prev_node.next = new_node

    def printList(self):
        temp = self.head
        while (temp):
            print(temp.data, end=" ")
            temp = temp.next

if __name__=='__main__':
    llist = LinkedList()
    # Insert 6.  So linked list becomes 6->None
    llist.append(6)

    # Insert 7 at the beginning. So linked list becomes 7->6->None
    llist.push(7)

    # Insert 1 at the beginning. So linked list becomes 1->7->6->None
    llist.push(1)

    # Insert 4 at the end. So linked list becomes 1->7->6->4->None
    llist.append(4)

    # Insert 8, after 7. So linked list becomes 1 -> 7-> 8-> 6-> 4-> None
    llist.insertAfter(llist.head.next, 8)

    print(llist.head.next.data)
    print(llist.length())
    # print(llist.display())
    print(llist.printList())
    print(f"Cur_node.data == {llist.get_index(0)}")