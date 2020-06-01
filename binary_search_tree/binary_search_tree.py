"""
Binary search trees are a data structure that enforce an ordering over 
the data they store. That ordering in turn makes it a lot more efficient 
at searching for a particular piece of data in the tree. 

This part of the project comprises two days:
1. Implement the methods `insert`, `contains`, `get_max`, and `for_each`
   on the BSTNode class.
2. Implement the `in_order_print`, `bft_print`, and `dft_print` methods
   on the BSTNode class.
"""
from dumb_queue.dumb_queue import Queue
from stack.stack import Stack



class BSTNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

    # Insert the given value into the tree
    def insert(self, value):
        new_node = BSTNode(value)
        if self.value > value:
            if self.left:
                return self.left.insert(value)
            # check if dot right exists.
            else:
                self.left = new_node
        else:
            if self.right:
                return self.right.insert(value)
            else:
                self.right = new_node

    # Return True if the tree contains the value
    # False if it does not
    def contains(self, target):
        if target == self.value:
            return True


        elif target < self.value:
            if self.left:
                return self.left.contains(target)
            else:
                return False
        else:
            if self.right:
                return self.right.contains(target)
            else:
                return False

    # Return the maximum value found in the tree
    def get_max(self):
        current_node = self
        while current_node.right is not None:
            current_node = current_node.right

        return current_node.value

    # Call the function `fn` on the value of each node
    def for_each(self, fn):
        fn(self.value)

        if self.left:
            self.left.for_each(fn)
        if self.right:
            self.right.for_each(fn)

    # Part 2 -----------------------

    # Print all the values in order from low to high
    # Hint:  Use a recursive, depth first traversal
    def in_order_print(self, node):
        if node.left is not None:
            node.in_order_print(node.left)

        print(node.value)

        if node.right is not None:
            node.in_order_print(node.right)

    # Print the value of every node, starting with the given node,
    # in an iterative breadth first traversal
    def bft_print(self, node):
        queue = Queue()
        queue.enqueue(node)

        while len(queue) != 0:
            # dequeue has the power to add and remove
            node = queue.dequeue()
            if node.left:
                queue.enqueue(node.left)
            if node.right:
                queue.enqueue(node.right)
            print(node.value)

    # Print the value of every node, starting with the given node,
    # in an iterative depth first traversal
    def dft_print(self, node):
        stack = Stack()
        # .push will add new elements
        stack.push(node)

        while len(stack) > 0:
            # pop is used to return nth element of list
            node = stack.pop()

            if node.left is not None:
                stack.push(node.left)
            if node.right is not None:
                stack.push(node.right)
            print(node.value)

    # Stretch Goals -------------------------
    # Note: Research may be required
    # Root Left Right
    # Print Pre-order recursive DFT
    def pre_order_dft(self, node):
        print(node.value)

        if node.left is not None:
            node.pre_order_dft(node.left)

        if node.right is not None:
            node.pre_order_dft(node.right)

    # Print Post-order recursive DFT
    def post_order_dft(self, node):

        if node.left is not None:
            node.post_order_dft(node.left)
        # RIGHT
        if node.right is not None:
            node.post_order_dft(node.right)
        # ROOT
        print(node.value)
