'''
    Provided implementation. Do not modify any of the functions below
    You should aquaint yourself with how to initialize and access data from
    Node objects but you do not need to fully understand how this class works internally
'''

class Node:
    def __init__(self, value, left_child=None, right_child=None):
        '''
        Constructs an instance of Node
        Inputs:
            value: An object, the value held by this node
            left_child: A Node object if this node has a left child, None otherwise
            right_child: A Node object if this node has a right child, None otherwise
        '''
        if isinstance(left_child, Node):
            self.left = left_child
        elif left_child == None:
            self.left = None
        else:
            raise TypeError("Left child not an instance of Node")

        if isinstance(right_child, Node):
            self.right = right_child
        elif right_child == None:
            self.right = None
        else:
            raise TypeError("Right child not an instance of Node")

        self.value = value

    def get_left_child(self):
        '''
        Returns this node's left child if present. None otherwise
        '''
        return self.left

    def get_right_child(self):
        '''
        Returns this node's right child if present. None otherwise
        '''
        return self.right

    def get_value(self):
        '''
        Returns the object held by this node
        '''
        return self.value

    def __eq__(self, tree):
        '''
        Overloads the == operator
        Example usage: Node(6, Node(1)) == Node(6, Node(1)) evaluates to True
        Output:
            True or False if the tree is equal or not
        '''
        if not isinstance(tree, Node):
            return False
        return (self.value == tree.value and
                self.left == tree.left and
                self.right == tree.right)

    def __str__(self):
        '''
        Output:
            A well formated string representing the tree
        '''
        output = []
        buffer = [self]
        i=0
        while True in [True if isinstance(node, Node) else False for node in buffer]:
            output.append([str(node.value) if isinstance(node, Node) else ' ' for node in buffer])
            nb = []
            for node in buffer:
                if node != None:
                    nb.extend([node.left, node.right])
                else:
                    nb.extend([None, None])
            buffer = nb
            i+=1

        bottom_len = len(output[-1])*4-1
        string = ''
        for i, row in enumerate(output):
            spacing = int((bottom_len - len(row))/(len(row)+1))
            string += ' '*spacing
            for elem in row:
                string += elem + ' '*spacing
            string += '\n'
        return string[:-1]
