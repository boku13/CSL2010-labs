class BinaryTreeNode:
    def __init__(self, departure_time=0, trip_node_ptr=None, parent_ptr=None):
        self.left_ptr = None
        self.right_ptr = None
        self.parent_ptr = parent_ptr
        self.departure_time = departure_time
        self.trip_node_ptr = trip_node_ptr

    def get_left_ptr(self):
        return self.left_ptr

    def set_left_ptr(self, new_left_ptr):
        self.left_ptr = new_left_ptr

    def get_right_ptr(self):
        return self.right_ptr

    def set_right_ptr(self, new_right_ptr):
        self.right_ptr = new_right_ptr

    def get_parent_ptr(self):
        return self.parent_ptr

    def set_parent_ptr(self, new_parent_ptr):
        self.parent_ptr = new_parent_ptr

    def get_departure_time(self):
        return self.departure_time

    def set_departure_time(self, new_departure_time):
        self.departure_time = new_departure_time

    def get_trip_node_ptr(self):
        return self.trip_node_ptr

    def set_trip_node_ptr(self, new_trip_node_ptr):
        self.trip_node_ptr = new_trip_node_ptr

class BinaryTree:
    def __init__(self):
        self.root = None

    def get_height(self):
        # Helper function to calculate the height of a binary tree
        def calculate_height(node):
            if node is None:
                return 0
            left_height = calculate_height(node.get_left_ptr())
            right_height = calculate_height(node.get_right_ptr())
            return max(left_height, right_height) + 1

        if self.root is None:
            return 0
        return calculate_height(self.root)

    def get_number_of_nodes(self):
        # Helper function to count the number of nodes in the binary tree
        def count_nodes(node):
            if node is None:
                return 0
            return 1 + count_nodes(node.get_left_ptr()) + count_nodes(node.get_right_ptr())

        return count_nodes(self.root)

class BinarySearchTree(BinaryTree):
    def __init__(self):
        super().__init__()

    def get_element_with_minimum_key(self):
        # Return the element with the minimum key (not implemented here)
        def find_element_with_minimum_key(node):
            # Loop down to find the leftmost leaf
            while(node.left_ptr is not None):
                node = node.left_ptr
            
            return node    

        if self.root is None:
            return None  # Return None for an empty tree
        return find_element_with_minimum_key(self.root)

    def get_element_with_maximum_key(self):
        # Return the element with the maximum key (not implemented here)
        def find_element_with_maximum_key(node):
            # Loop down to find the rightmost leaf
            while(node.right_ptr is not None):
                node = node.right_ptr
            
            return node    

        if self.root is None:
            return None  # Return None for an empty tree
        return find_element_with_maximum_key(self.root)

    def search_node_with_key(self, key, node=None):
        # Helper function to search for a node with a given key
        if node is None:
            node = self.root
        
        # Base Cases: root is null or key is present at root
        if node is None or node.key == key:
            return node

        # Key is greater than the current node's key
        if node.key < key:
            return self.search_node_with_key(key, node.right_ptr)

        # Key is smaller than the current node's key
        return self.search_node_with_key(key, node.left_ptr)

    def get_successor_node(self, node):
        # Find the in-order successor of the given node
        if node is None:
            return None

        # If the right subtree is not empty, the successor is the minimum node in the right subtree
        if node.right_ptr is not None:
            return self.find_element_with_minimum_key(node.right_ptr)

        # If the right subtree is empty, traverse up the tree to find the successor
        successor = None
        current = self.root

        while current is not None:
            if node.key < current.key:
                successor = current
                current = current.left_ptr
            elif node.key > current.key:
                current = current.right_ptr
            else:
                break  # Node with the same key found, no need to continue

        return successor

    def get_predecessor_node(self, node):
        # Find the in-order predecessor of the given node
        if node is None:
            return None

        # If the left subtree is not empty, the predecessor is the maximum node in the left subtree
        if node.left_ptr is not None:
            return self.find_element_with_maximum_key(node.left_ptr)

        # If the left subtree is empty, traverse up the tree to find the predecessor
        predecessor = None
        current = self.root

        while current is not None:
            if node.key > current.key:
                predecessor = current
                current = current.right_ptr
            elif node.key < current.key:
                current = current.left_ptr
            else:
                break  # Node with the same key found, no need to continue

        return predecessor

    def insert(self, key, trip=None):
        # Create a new node with the provided key and trip data
        new_node = BinaryTreeNode(key, trip)

        if self.bst_head is None:
            # If the BST is empty, make the new node the root
            self.bst_head = new_node
        else:
            # Otherwise, traverse the BST to find the insertion point
            current = self.bst_head
            while current:
                if key < current.key:
                    # If the key is smaller, move to the left subtree
                    if current.left_ptr is None:
                        # If there's no left child, insert the new node here
                        current.left_ptr = new_node
                        break
                    current = current.left_ptr
                elif key > current.key:
                    # If the key is larger, move to the right subtree
                    if current.right_ptr is None:
                        # If there's no right child, insert the new node here
                        current.right_ptr = new_node
                        break
                    current = current.right_ptr
                else:
                    # If the key already exists, you can handle it as needed
                    # For example, you can update the existing node or ignore it
                    break
 
    

# node_root = BinaryTreeNode()
# tree = BinaryTree()
# tree.root = node_root
root = BinaryTreeNode(1)
root.left_ptr = BinaryTreeNode(2)
root.right_ptr = BinaryTreeNode(3)
root.left_ptr.left_ptr = BinaryTreeNode(4)
root.left_ptr.right_ptr = BinaryTreeNode(5)

# Create the binary tree
binary_tree = BinaryTree()
binary_tree.root = root
print(binary_tree.get_height())
print(binary_tree.get_number_of_nodes())


# Create a BinarySearchTree and add nodes
bst = BinarySearchTree()
bst.insert(50)
bst.insert(30)
bst.insert(70)
bst.insert(20)
bst.insert(40)
bst.insert(60)
bst.insert(80)

# Find a node in the BST
node_to_find = bst.search(40)

# Test the get_successor_node function
successor = bst.get_successor_node(node_to_find)
if successor:
    print(f"Successor of {node_to_find.key} is {successor.key}")
else:
    print(f"No successor found for {node_to_find.key}")

# Test the get_predecessor_node function
predecessor = bst.get_predecessor_node(node_to_find)
if predecessor:
    print(f"Predecessor of {node_to_find.key} is {predecessor.key}")
else:
    print(f"No predecessor found for {node_to_find.key}")
