"""
        1
    /       \
   2         3
  / \       / \  
 4   5     6   7 


Breadth-first-search algorithm:

Visit every level from top to buttom.
This can be achieved using a queue.

1- create an empty queue, add to it the root/the starting node.
2- pop the top of the queue, add its children to the queue.
3- perform the previous step until the queue is empty.

"""


from node import Node

class BFS:
    
    @classmethod
    def run(cls, start_node: Node):
        queue = list()
        # starts from the first row and col
        queue.append(start_node)
        # iterate over the queue
        while len(queue) != 0:
            # pop the top of the queue
            node = queue.pop(0)
            print(node.val)
            # add its children to the queue
            for i in node.children:
                queue.append(i)


if __name__ == '__main__':
    
    node4 = Node(4)
    node5 = Node(5)
    node6 = Node(6)
    node7 = Node(7)
    node2 = Node(2, [node4, node5])
    node3 = Node(3, [node6, node7])
    node1 = Node(1, [node3, node2])
    
    BFS.run(node1)
