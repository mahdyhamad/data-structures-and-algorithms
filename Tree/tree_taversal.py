class Node:
    def __init__(self, val):
        self.value = val
        self.left = None
        self.right = None


class Tree:
    def __init__(self, root):
        self.root = root


def inorder_traversal(root: Node):
    if root is None:
        return []
    p = inorder_traversal(root.left)
    p.append(root.value)
    return p + inorder_traversal(root.right)
def inorder(root: Node):
    # left -> parent -> right
    return inorder_traversal(root)


def preorder_traversal(root: Node):
    if root is None:
        return []
    else:
        # Root first
        p = [root.value]
        # Left values follows the root
        p = p + preorder_traversal(root.left)
        # Right values is last
        return p + preorder_traversal(root.right)
def preorder(root: Node):
    # root -> left -> right
    return preorder_traversal(root)


def postorder_traversal(root: Node):
    if root is None:
        return []
    else:
        # right -> left -> parent
        p = postorder_traversal(root.right)
        p = p + postorder_traversal(root.left)
        p.append(root.value)
        return p
def postorder(root: Node):
    return postorder_traversal(root)


def get_binary_tree() -> Node:
    #      10
    #     /  \
    #    5    6
    #   / \
    #  3   2
    root = Node(10)
    root.left = Node(5)
    root.right = Node(6)
    root.left.left = Node(3)
    root.left.right = Node(2)
    return root


def test():
        root = get_binary_tree()
        print("Inorder traversal -> ", inorder(root))
        print("Preorder traversal -> ", preorder(root))
        print("Postorder traversal -> ", postorder(root))


if __name__ == '__main__':
    test()


