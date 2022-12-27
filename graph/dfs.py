"""
        1
    /       \
   2         3
  / \       / \  
 4   5     6   7 


Depth-first-search algorithm:

Visit every level from top to buttom.
This can be achieved using a queue.

1- create an empty queue, add to it the root/the starting node.
2- pop the top of the queue, add its children to the queue.
3- perform the previous step until the queue is empty.

"""

from node import Node

class DFS:

    @staticmethod
    def run(start_node: Node):
        visited_nodes = set()
        DFS._dfs(start_node, visited_nodes)
    
    @staticmethod
    def _dfs(node: Node, visisted_nodes):
        if node:
            visisted_nodes.add(node)
            print(node.val)
            for i in node.children:
                if i not in visisted_nodes:
                    DFS._dfs(i, visisted_nodes)


if __name__ == '__main__':
    
    node4 = Node(4)
    node5 = Node(5)
    node6 = Node(6)
    node7 = Node(7)
    node2 = Node(2, [node4, node5])
    node3 = Node(3, [node6, node7])
    node1 = Node(1, [node3, node2])
    
    DFS.run(node1)
