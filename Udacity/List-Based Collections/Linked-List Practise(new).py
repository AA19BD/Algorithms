"""The LinkedList code from before is provided below.
Add three functions to the LinkedList.
"get_position" returns the element at a certain position.
The "insert" function will add an element to a particular
spot in the list.
"delete" will delete the first element with that
particular value.
Then, use "Test Run" and "Submit" to run the test cases
at the bottom."""


class Element(object):
    def __init__(self, value):
        self.value = value
        self.next = None


class LinkedList(object):
    def __init__(self, head=None):
        self.head = head

    def append(self, new_element):
        current = self.head
        if self.head:
            while current.next:
                current = current.next
            current.next = new_element
        else:
            self.head = new_element

    def get_position(self, position):
        """Get an element from a particular position.
        Assume the first position is "1".
        Return "None" if position is not in the list."""
        if position < 1:
            return None

        cur_node = self.head
        cur_idx = 1
        while cur_node and cur_idx <= position:
            if cur_idx == position:
                return cur_node
            cur_node = cur_node.next
            cur_idx += 1
        return None

    def insert(self, new_element, position):
        """Insert a new node at the given position.
        Assume the first position is "1".
        Inserting at position 3 means between
        the 2nd and 3rd elements."""
        if position < 1:
            return None

        if position == 1:
            new_element.next == self.head
            self.head == new_element

        cur = self.head
        cur_index = 1
        while cur and cur_index <= position:
            if cur_index == position:
                break
            prev = cur
            cur = cur.next
            cur_index += 1

        prev.next = new_element
        new_element.next = cur

    def delete(self, value):
        """Delete the first node with a given value."""
        # Store head node
        cur = self.head

        # If head node itself holds the key to be deleted
        if cur is not None:
            if cur.value == value:
                self.head = cur.next
                cur = None
                return
                # Search for the key to be deleted, keep track of the
        # previous node as we need to change 'prev.next'
        while cur:
            if cur.value == value:
                break
            prev = cur
            cur = cur.next
        # if key was not present in linked list
        if cur == None:
            return
            # Unlink the node from linked list
        prev.next = cur.next

        cur = None


# Test cases
# Set up some Elements
e1 = Element(1)
e2 = Element(2)
e3 = Element(3)
e4 = Element(4)

# Start setting up a LinkedList
ll = LinkedList(e1)
ll.append(e2)
ll.append(e3)

# Test get_position
# Should print 3
print(ll.head.next.next.value)
# Should also print 3
print(ll.get_position(3).value)

# Test insert
ll.insert(e4, 3)
# Should print 4 now
print(ll.get_position(3).value)

# Test delete
ll.delete(1)
# Should print 2 now
print(ll.get_position(1).value)
# Should print 4 now
print(ll.get_position(2).value)
# Should print 3 now
print(ll.get_position(3).value)