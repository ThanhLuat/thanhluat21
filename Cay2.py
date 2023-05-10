
class Node:
    def __init__(self, key):
        self.left = None
        self.middle = None
        self.right = None
        self.val = key

def print_tree(node):
    if node is None:
        return None
    queue = []
    queue.append(node)

    while queue:
        level_size = len(queue)

        for i in range(level_size):
            current_node = queue.pop(0)
            print(current_node.val, end=' ')

            if current_node.left:
                queue.append(current_node.left)
            if current_node.middle:
                queue.append(current_node.middle)
            if current_node.right:
                queue.append(current_node.right)
        print()

def print_tree_postorder(node):
    if node:
        print_tree_postorder(node.left)
        if node.middle:
            print_tree_postorder(node.middle)
        print_tree_postorder(node.right)
        print(node.val, end=' ')

root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(4)
root.left.right = Node(5)
root.right.right = Node(6)
root.left.left.left = Node(7)
root.left.left.right = Node(8)
root.right.right.left = Node(9)
root.right.right.right = Node(10)

print_tree(root)
print_tree_postorder(root)