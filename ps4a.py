# Problem Set 4A
# Name: Mai Nguyen
# Collaborators: None 
# Time Spent: 2:00
# Late Days Used: 0

from tree import Node # Imports the Node object used to construct trees

# Part A0: Data representation
# Fill out the following variables correctly.
# If correct, the tests named data_representation should pass.
tree1 = Node(9, Node(3, Node(1), Node(6)), Node(11)) # TODO: change this assignment
tree2 = Node(8, Node(3, Node(1), Node(6, Node(4), Node(7))), Node(10, Node(14), Node(13))) # TODO: change this assignment
tree3 = Node(5, Node(2, Node(1), Node(3)), Node(12, Node(9), Node(21, Node(19), Node(25)))) # TODO: change this assignment

def find_height(tree):
    '''
    Find the height of the given tree
    Input:
        tree: An element of type Node constructing a tree
    Output:
        The integer depth of the tree
    '''
    # TODO: Remove pass and write your code here
    
    # base case 
    # if there are no left and right subtree -> it's a leaf 
    if tree.get_left_child() is None and tree.get_right_child() is None: 
        return 0
    # if there are both a left and right subtree -> find height of both and return the taller +1 
    elif tree.get_left_child() is not None and tree.get_right_child()is not None:
        max_height=max(find_height(tree.get_left_child()),find_height(tree.get_right_child()))
        return max_height+1 
    # if there are no left subtree -> return height of the right +1 
    elif tree.get_left_child() is None:
        max_height=find_height(tree.get_right_child())
        return max_height+1 
    # if there are no right subtree -> return height of the left +1 
    else: 
        max_height=find_height(tree.get_left_child())
        return max_height+1      
def element_in_tree(num, tree):
    '''
    Determines if the binary search tree contains the specified number
    Inputs:
        num: A float or int number
        tree: An element of type Node constructing a binary search tree
    Output:
        False if the tree does not contain the specified number, True otherwise
    '''
    # TODO: Remove pass and write your code here
    
    # base case leaf (height = 0)
    if find_height(tree)==0:
        # if the leaf has the same value as num 
        if tree.get_value()==num:
            return True 
        else:
            return False   
    # if value of the tree is num 
    elif tree.get_value()==num:
        return True 
    
    # if value of tree is larger than num -> num might be in left subtree 
    elif tree.get_value()>num: 
        # check if left subtree exist 
         if tree.get_left_child() is not None: 
             # check if num is in left subtree
             return element_in_tree(num, tree.get_left_child()) 
         # if there is no left subtree
         else: 
             return False
    # if value of tree is smaller or equal to num -> num might be in right subtree
    elif tree.get_value()<=num:
        # check if right subtree exist
         if tree.get_right_child() is not None: 
             # check if num is in right subtree
             return element_in_tree(num, tree.get_right_child())
         # if there is no right subtree
         else: 
             return False             
     
      
if __name__ == '__main__':
    # You can use this part for your own testing and debugging purposes.
    # IMPORTANT: Do not erase the pass statement below if you do not add your own code

    pass
