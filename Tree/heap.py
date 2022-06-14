from tree_taversal import inorder


class Node:
    def __init__(self, val):
        self.value = val
        self.left = None
        self.right = None


class Heap:
    """
    Heaps should be complete binary trees. Complete means
    that all levels of the tree should be filled except the last level.
    The last level should be filled from left to right.
    """
    def __init__(self):
        self.root = None

    def insert(self, val):
        new_node = Node(val)
        if self.root is None:
            self.root = new_node
        else:
            self.insert_to_heap(new_node)

    def insert_to_heap(self, node):
        # finds the last position and add the new node from left to right
        # this is done using BFS
        nodes = [self.root]
        while len(nodes) != 0:
            parent: Node = nodes.pop(0)
            if parent.left:
                nodes.append(parent.left)
            if parent.right:
                nodes.append(parent.right)

            if parent.left is None or parent.right is None:
                if parent.left is None:
                    parent.left = node
                elif parent.right is None:
                    parent.right = node
                return parent


if __name__ == '__main__':
    heap = Heap()
    heap.insert(10)
    heap.insert(4)
    heap.insert(6)
    heap.insert(3)
    heap.insert(5)
    heap.insert(8)
    print(inorder(heap.root))