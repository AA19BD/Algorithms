class Node:
    def __init__(self, key):
        self.left = None
        self.right = None
        self.key = key

# A function to do inorder Tree traversal
def print_inorder(root): # left.child -> root -> right.child
    if root:
        print_inorder(root.left)
        print(root.key, end= " ")
        print_inorder(root.right)


# A function to do preorder Tree traversal
def print_preorder(root): # root -> left.child -> right.child
    if root:
        print(root.key, end=" ")
        print_preorder(root.left)
        print_preorder(root.right)


# A function to do postorder Tree traversal
def print_postorder(root): # left.child -> right.child -> root
    if root:
        print_postorder(root.left)
        print_postorder(root.right)
        print(root.key, end=" ")


root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(4)
root.left.right = Node(5)
root.right.left = Node(6)
root.right.right = Node(7)

print('In-order')
print_inorder(root)
print(" ")
print('Pre-order')
print_preorder(root)
print(" ")
print('Post-order')
print_postorder(root)