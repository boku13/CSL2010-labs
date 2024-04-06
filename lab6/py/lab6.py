class HybridNode:
    def __init__(self, key, element):
        self.key = key
        self.element = element
        self.parent = None
        self.left_child = None
        self.right_child = None
        self.next_node = None
        #color member needed
        self.color = 1 # 1 -> red, 0 -> black 
        
class HistogramBin:
    def __init__(self, chaptername):
        self.chapter_name = chaptername
        self.word_count = 1

class RedBlackTree:
    def __init__(self):
        self.root = None
        self.TNULL = HybridNode(0, None)
        self.TNULL.color = 0
        self.TNULL.left_child = None
        self.TNULL.right_child = None
        self.root = self.TNULL
        

    def insert(self, key, element):
        # Implement Red-Black Tree insertion
        node = HybridNode(key, element)
        node.parent = None
        node.key = key
        node.left_child = self.TNULL
        node.right_child = self.TNULL
        node.color = 1

        y = None
        x = self.root

        while x != self.TNULL:
            y = x
            if node.key < x.key:
                x = x.left_child
            else:
                x = x.right_child

        node.parent = y
        if y == None:
            self.root = node
        elif node.key < y.key:
            y.left_child = node
        else:
            y.right_child = node

        if node.parent == None:
            node.color = 0
            return

        if node.parent.parent == None:
            return

        self.fix_insert(node)
        

    def delete(self, key):
        # Implement Red-Black Tree deletion
        pass

    def traverse_up(self, node):
        # Traverse up the tree from the given node to the root
        pass

    def traverse_down(self, node, bit_sequence):
        # Traverse down the tree based on the bit sequence
        pass

    def preorder_traversal(self, node, depth, result):
        # Perform in-order traversal staying within specified depth
        pass

    def black_height(self, node):
        # Return the black height of the tree
        pass

    def search(self, key):
        # Search for a node with the given key
        current = self.root
        while current != self.TNULL:
            if key == current.key:
                return current
            elif key < current.key:
                current = current.left_child
            else:
                current = current.right_child

    def left_rotate(self, x):
        y = x.right_child
        x.right_child = y.left_child
        if y.left_child != self.TNULL:
            y.left_child.parent = x

        y.parent = x.parent
        if x.parent == None:
            self.root = y
        elif x == x.parent.left_child:
            x.parent.left_child = y
        else:
            x.parent.right_child = y
        y.left_child = x
        x.parent = y

    def right_rotate(self, x):
        y = x.left_child
        x.left_child = y.right_child
        if y.right_child != self.TNULL:
            y.right_child.parent = x

        y.parent = x.parent
        if x.parent == None:
            self.root = y
        elif x == x.parent.right_child:
            x.parent.right_child = y
        else:
            x.parent.left_child = y
        y.right_child = x
        x.parent = y
    
    # Balance the tree after insertion
    def fix_insert(self, k):
        while k.parent.color == 1:
            if k.parent == k.parent.parent.right_child:
                u = k.parent.parent.left_child
                if u.color == 1:
                    u.color = 0
                    k.parent.color = 0
                    k.parent.parent.color = 1
                    k = k.parent.parent
                else:
                    if k == k.parent.left_child:
                        k = k.parent
                        self.right_rotate(k)
                    k.parent.color = 0
                    k.parent.parent.color = 1
                    self.left_rotate(k.parent.parent)
            else:
                u = k.parent.parent.right_child

                if u.color == 1:
                    u.color = 0
                    k.parent.color = 0
                    k.parent.parent.color = 1
                    k = k.parent.parent
                else:
                    if k == k.parent.right_child:
                        k = k.parent
                        self.left_rotate(k)
                    k.parent.color = 0
                    k.parent.parent.color = 1
                    self.right_rotate(k.parent.parent)
            if k == self.root:
                break
        self.root.color = 0
        
    
    def print_formatted_tree(self, node, level=0):
        self.root.parent = HybridNode(0, 0)
        if node != self.TNULL:
            self.print_formatted_tree(node.left_child, level + 1)
            print(' ' * 8 * level + '-> ' + str(node.parent.key) + "p" + str(node.key) + "c" + str(node.color))
            self.print_formatted_tree(node.right_child, level + 1)


class Lexicon:
    def __init__(self):
        self.red_black_tree = RedBlackTree()

    def read_chapter(self, chapter_name, words):
        for word in words.split():
            cleaned_word = ''.join(e for e in word if e.isalnum()).lower()  # Remove punctuation
            if cleaned_word:  # Ignore empty strings
                node = self.red_black_tree.search(cleaned_word)
                if node:
                    # Word already in Red-Black Tree, update histogram
                    bin_node = node.element
                    if bin_node.chapter_name != chapter_name:
                        bin_node.chapter_name = chapter_name
                        bin_node.word_count += 1
                else:
                    # Word not in Red-Black Tree, insert new node
                    bin_node = HistogramBin(chapter_name)
                    self.red_black_tree.insert(cleaned_word, bin_node)


    def prune_red_black_tree(self):
        # Prune the Red-Black Tree by deleting common words
        pass

    def build_index(self):
        # Build the index using the remaining words in the Red-Black Tree
        pass


class IndexEntry:
    def __init__(self, word):
        self.word = word
        self.chapter_word_counts = []  # List of (chapter, word_count) tuples

    def add_occurrence(self, chapter, word_count):
        # Add a chapter's word count for this word
        pass

    def __str__(self):
        # Return a string representation of the IndexEntry
        pass
    

# GPT GENERATED TEST CASES. 
#     # Create a Red-Black Tree object
# tree = RedBlackTree()

# # Insert nodes into the tree
# nodes_to_insert = [14, 13, 10, 11, 7, 4, 3, 5, 8, 6, 12, 15, 17]

# for key in nodes_to_insert:
#     tree.insert(key, key)

# # Helper function to perform an in-order traversal of the Red-Black Tree
# def in_order_traversal(node):
#     if node != tree.TNULL:
#         in_order_traversal(node.left_child)
#         print(f"Key: {node.key}, Color: {'Red' if node.color == False else 'Black'}, Parent: {node.parent.key if node.parent else None}")
#         in_order_traversal(node.right_child)

# # Perform in-order traversal to check if the tree is constructed correctly
# print("In-order Traversal:")
# in_order_traversal(tree.root)

# tree.print_formatted_tree(tree.root)

# # Validate Red-Black Tree properties

# # Helper function to validate the black height of the tree
# def check_black_height(node):
#     if node == tree.TNULL:
#         return 1
#     left_height = check_black_height(node.left_child)
#     right_height = check_black_height(node.right_child)
#     # Validate Property 5: Both red and black nodes have the same black height
#     assert left_height == right_height, f"Invalid black height at node with key {node.key}"
#     # Validate Property 4: No two consecutive red nodes
#     assert not (node.color and node.parent and node.parent.color), f"Consecutive red nodes found at key {node.key}"
#     # Return black height of the subtree rooted at this node
#     return left_height + (1 if node.color else 0)

# # Validate Property 1: Root is black
# assert tree.root.color == False, "Root is not black"


# # Validate Property 2: Every red node must have two black children
# # Validate Property 3: Every path from a node to its descendant leaves must have the same black nodes count
# check_black_height(tree.root)


# print("Red-Black Tree properties are valid.")



chapters_list = ["Chapter1.txt", "Chapter2.txt", "Chapter3.txt"]