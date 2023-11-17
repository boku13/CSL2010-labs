class redblacknode():
    def __init__(self, key):
        self.key = key
        self.color = False  
        self.parent = None
        self.left = None
        self.right = None

# red -> False
# black -> True

class redblacktree:
    def __init__(self):
        self.nil = redblacknode(None)
        self.nil.color = True
        self.nil.right = None
        self.nil.left = None
        self.root = self.nil
    
    #nil == leaf
    #root - obj of redblacknode 
    
    def insert(self, key):
        newnode = redblacknode(key)
        newnode.parent = None
        newnode.left = self.nil
        newnode.right = self.nil
        newnode.color = False #red
        
        self.root = self.bst_insert(self.root, newnode)
        self.fix_insert(newnode)
        
        
    def bst_insert(self, root, newnode):
        if root == self.nil:
            return newnode

        if newnode.key < root.key:
            if root.left == self.nil:
                root.left = newnode
                newnode.parent = root
            else:
                return self.bst_insert(root.left, newnode)
        else:
            if root.right == self.nil:
                root.right = newnode
                newnode.parent = root
            else:
                return self.bst_insert(root.right, newnode)
        
        return root  # Return root of the subtree

    def recolor(self, newnode, parent_sibling):
        newnode.parent.color = True
        parent_sibling.color = True
        newnode.parent.parent.color = False
        newnode = newnode.parent.parent  #grandparent needs correction
        
    def restructure(self, newnode, left_heavy = False, right_heavy = False):
        if left_heavy:
            if newnode == newnode.parent.right: #case 2 or left-right case (left heavy and then right heavy)
                newnode = newnode.parent
                self.left_rotate(newnode)
            newnode.parent.color = True   #case 3  or left-left case (change parent to black and grandparent to red)
            newnode.parent.parent.color = False
            self.right_rotate(newnode.parent.parent)
        
        if right_heavy:
            if newnode == newnode.parent.left:  #right-left case
                newnode = newnode.parent
                self.right_rotate(newnode)
            newnode.parent.color = True     #right-right case
            newnode.parent.parent.color = False
            self.left_rotate(newnode.parent.parent)
        
                
    # def fix_insert(self, newnode):
    #     while newnode.parent and newnode.parent.color == False:    #if parent is red
    #         if newnode.parent == newnode.parent.parent.left:    #left heavy
    #             parent_sibling = newnode.parent.parent.right
    #             if parent_sibling.color == False:   #if uncle is red then recolor to satisfy depth property
    #                 self.recolor(newnode, parent_sibling)
    #             else:   
    #                 self.restructure(newnode, True, False)  #restructure to satisfy depth property
    #         else:                                               #right heavy
    #             parent_sibling = newnode.parent.parent.left
    #             if parent_sibling.color == False:
    #                 self.recolor(newnode, parent_sibling)
    #             else:
    #                 self.restructure(newnode, False, True)
        
    #     self.root.color = True  #root is always black
    
    def fix_insert(self, newnode):
        while newnode.parent and newnode.parent.color == False:  # If parent is red
            if newnode.parent == newnode.parent.parent.left:  # Left heavy
                parent_sibling = newnode.parent.parent.right
                if parent_sibling.color == False:  # If uncle is red then recolor to satisfy depth property
                    self.recolor(newnode, parent_sibling)
                else:
                    if newnode == newnode.parent.right:  # Left-right case
                        newnode = newnode.parent
                        self.left_rotate(newnode)
                    newnode.parent.color = True  # Left-left case
                    newnode.parent.parent.color = False
                    self.right_rotate(newnode.parent.parent)
            else:  # Right heavy
                parent_sibling = newnode.parent.parent.left
                if parent_sibling.color == False:
                    self.recolor(newnode, parent_sibling)
                else:
                    if newnode == newnode.parent.left:  # Right-left case
                        newnode = newnode.parent
                        self.right_rotate(newnode)
                    newnode.parent.color = True  # Right-right case
                    newnode.parent.parent.color = False
                    self.left_rotate(newnode.parent.parent)

        self.root.color = True  # Root is always black

    
    # #gpt'd left and right rotates.
    
    def left_rotate(self, x):
        y = x.right
        x.right = y.left
        if y.left != self.nil:
            y.left.parent = x
        y.parent = x.parent
        if x.parent is not None:
            if x.parent == self.nil:
                self.root = y
            elif x == x.parent.left:
                x.parent.left = y
            else: 
                x.parent.right = y
        y.left = x
        x.parent = y
        
    def right_rotate(self, x):
        y = x.left
        x.left = y.right
        if y.right != self.nil:
            y.right.parent = x
        y.parent = x.parent
        if x.parent is not None:
            if x.parent == self.nil:
                self.root = y
            elif x == x.parent.right:
                x.parent.right = y
            else: 
                x.parent.left = y
        y.right = x
        x.parent = y
   
    def printTree(self, node):
        if node != self.nil:
            self.printTree(node.left)
            print(f"Key: {node.key}, Color: {'Red' if node.color == False else 'Black'}, Parent: {node.parent.key if node.parent else None}")
            self.printTree(node.right)
                        
                    
        
# Create a Red-Black Tree object
tree = redblacktree()

# Insert nodes into the tree
nodes_to_insert = [14, 13, 10, 11, 7, 4, 3, 5, 8, 6, 12, 15, 17]

for key in nodes_to_insert:
    tree.insert(key)

# Helper function to perform an in-order traversal of the Red-Black Tree
def in_order_traversal(node):
    if node != tree.nil:
        in_order_traversal(node.left)
        print(f"Key: {node.key}, Color: {'Red' if node.color == False else 'Black'}, Parent: {node.parent.key if node.parent else None}")
        in_order_traversal(node.right)

# Perform in-order traversal to check if the tree is constructed correctly
print("In-order Traversal:")
in_order_traversal(tree.root)

tree.printTree(tree.root)

# Validate Red-Black Tree properties

# Helper function to validate the black height of the tree
def check_black_height(node):
    if node == tree.nil:
        return 1
    left_height = check_black_height(node.left)
    right_height = check_black_height(node.right)
    # Validate Property 5: Both red and black nodes have the same black height
    assert left_height == right_height, f"Invalid black height at node with key {node.key}"
    # Validate Property 4: No two consecutive red nodes
    assert not (node.color == False and node.parent and node.parent.color == False), f"Consecutive red nodes found at key {node.key}"
    # Return black height of the subtree rooted at this node
    return left_height + (1 if node.color else 0)

# Validate Property 1: Root is black
assert tree.root.color == True, "Root is not black"


# Validate Property 2: Every red node must have two black children
# Validate Property 3: Every path from a node to its descendant leaves must have the same black nodes count
check_black_height(tree.root)


print("Red-Black Tree properties are valid.")

    
                
            
      
            
        


# node = redblacknode(1)
# tree = redblacktree(node)



         
        