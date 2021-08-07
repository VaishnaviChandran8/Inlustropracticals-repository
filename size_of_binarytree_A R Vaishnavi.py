class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None
def size(root_node):
    if root_node is None:
        return 0
    q = []
    q.append(root_node)
    height = 0
    while(True):
        n = len(q)
        if n == 0 :
            return height
        height += 1
        while(n > 0):
            node = q[0]
            q.pop(0)
            if node.left is not None:
                q.append(node.left)
            if node.right is not None:
                q.append(node.right)
                    
            n -= 1
root_node = Node(6)
root_node.left = Node(3)
root_node.right = Node(9)
root_node.left.left = Node(1)
root_node.left.right = Node(5)
root_node.right.left = Node(7)
root_node.right.right = Node(11)
print(size(root_node))
                    
                    
                    
