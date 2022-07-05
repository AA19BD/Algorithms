class Node:
    def __init__(self, data):
        self.data = data
        self.next = None



node1 = Node(10)
node2 = Node(20)
node3 = Node(30)

print(node1)#0x0000021BE84753C0
print(node1.next)#None
print(node1.data)#10

node1.next = node2
node2.next = node3

print(node1.next, node2)