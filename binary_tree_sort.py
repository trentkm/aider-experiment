class TreeNode:
    def __init__(self, key):
        self.left = None
        self.right = None
        self.val = key

def insert(root, key):
    if root is None:
        return TreeNode(key)
    else:
        if root.val < key:
            root.right = insert(root.right, key)
        else:
            root.left = insert(root.left, key)
    return root

def inorder_traversal(root):
    elements = []
    if root:
        elements += inorder_traversal(root.left)
        elements.append(root.val)
        elements += inorder_traversal(root.right)
    return elements

# Example usage:
if __name__ == "__main__":
    r = TreeNode(50)
    r = insert(r, 30)
    r = insert(r, 20)
    r = insert(r, 40)
    r = insert(r, 70)
    r = insert(r, 60)
    r = insert(r, 80)

    print("In-order traversal of the binary tree:")
    print(inorder_traversal(r))
