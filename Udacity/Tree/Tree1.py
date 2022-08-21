class Node(object):
    def __init__(self, key):
        self.val = key
        self.left = None
        self.right = None


if __name__ == '__main__':
    # Create root
    root = Node(1)
    ''' following is the Tree after above statement
            1
          /   \
         None  None'''
    root.left = Node(2)
    root.right = Node(3)
    ''' 2 and 3 become left and right children of 1
               1
             /   \
            2      3
         /    \    /  \
        None None None None'''
    root.left.left = Node(4)
    '''4 becomes left child of 2
                   1
               /       \
              2          3
            /   \       /  \
           4    None  None  None
          /  \
        None None'''
    print(root.right.val)
