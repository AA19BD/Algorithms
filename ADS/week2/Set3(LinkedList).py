class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None

    def push(self, new_data):
        new_node = Node(new_data)
        new_node.next = self.head
        self.head = new_node

    def deleteNode(self, key):
        # Store head node
        cur = self.head

        # If head node itself holds the key to be deleted
        if cur is not None:
            if cur.data == key:
                self.head = cur.next
                cur = None
                return

        # Search for the key to be deleted, keep track of the
        # previous node as we need to change 'prev.next'
        while cur is not None:
            if cur.data == key:
                break
            prev = cur
            cur = cur.next
        # if key was not present in linked list
        if cur == None:
            return

        # Unlink the node from linked list
        prev.next = cur.next

        cur = None


    def print_list(self):
        cur = self.head
        while cur:
            print(" %d" %(cur.data))
            cur = cur.next


llist = LinkedList()
llist.push(7)
llist.push(1)
llist.push(3)
llist.push(2)

print("Created Linked List: ")
llist.print_list()
llist.deleteNode(1)
print("\nLinked List after Deletion of 1:")
llist.print_list()
