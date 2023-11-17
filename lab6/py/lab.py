class HybridNode:
    def __init__(self, key, element, chapters_list):
        self.key = key  # Key
        self.element = element  # Element
        self.parent = None  # Parent node
        self.left_child = None  # Left child node
        self.right_child = None  # Right child node
        self.next_node = None  # Next node in the linked list
        self.color = "black"  # "red" or "black"
        #histogram where?
        self.histogram = MRU(key, chapters_list)    #key is word right_child?

class HistogramBin:
    def __init__(self, chaptername):
        self.chapter_name = chaptername
        self.word_count = 0
        self.next = None
        # self.prev = None
        
class MRU:
    def __init__(self, word, chapters_list):
        self.chapters_list = chapters_list
        self.word = word
        self.recent = None
        if chapters_list is not None:
            self.recent = HistogramBin(chapters_list[0])  # Most recently used node
        # self.least = None  # Least recently used node
        temp = self.recent
        if chapters_list is not None and self.recent is not None:
            for i in range(1, len(chapters_list)):
                temp.next = HistogramBin(chapters_list[i])
                temp.next.prev = temp
                temp = temp.next
            
    def retrieve(self):
        return self.recent.chapter_name
    
    def search(self, chapter_name):
        curr = self.recent
        
        while curr != None:
            if curr.chapter_name == chapter_name:
                return curr
            curr = curr.next
            
        return None
        
    def print_chapter_counts(self):
        curr = self.recent
        while curr is not None:
            print(f"Chapter '{curr.chapter_name}': {curr.word_count} words")
            curr = curr.next
                
    def chapterwise_chapter_counts(self):
        counts = []
        curr = self.recent
        while curr is not None:
            freq_tuple = (curr.chapter_name, curr.word_count)
            counts.append(freq_tuple)
            curr = curr.next
        return counts
    
    # def insert(self, histogram_bin):
    #     curr = self.recent
        
    #     while curr.next != None:
    #         curr = curr.next
        
    #     curr.next = histogram_bin
    #     histogram_bin.next = None    
        
    #     return histogram_bin
         

class RedBlackTree:
    def __init__(self):
        self.root = None  # Root node
        self.root = None
        self.TNULL = HybridNode(0, None, None)
        self.TNULL.color = 0
        self.TNULL.left_child = None
        self.TNULL.right_child = None
        self.root = self.TNULL

    def insert(self, key, element, histogram):  
        # Implement Red-Black Tree insertion
        # Implement Red-Black Tree insertion
        node = HybridNode(key, element, histogram)
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
        self.delete_node_helper(self.root, key)
        
    def delete_node_helper(self, node, key):
        z = self.TNULL
        while node != self.TNULL:
            if node.key == key:
                z = node

            if node.key <= key:
                node = node.right_child
            else:
                node = node.left_child

        if z == self.TNULL:
            print("Cannot find key in the tree")
            return

        y = z
        y_original_color = y.color
        if z.left_child == self.TNULL:
            x = z.right_child
            self.__rb_transplant(z, z.right_child)
        elif (z.right_child == self.TNULL):
            x = z.left_child
            self.__rb_transplant(z, z.left_child)
        else:
            y = self.minimum(z.right_child)
            y_original_color = y.color
            x = y.right_child
            if y.parent == z:
                x.parent = y
            else:
                self.__rb_transplant(y, y.right_child)
                y.right_child = z.right_child
                y.right_child.parent = y

            self.__rb_transplant(z, y)
            y.left_child = z.left_child
            y.left_child.parent = y
            y.color = z.color
        if y_original_color == 0:
            self.delete_fix(x)
            
    def __rb_transplant(self, u, v):
        if u.parent == None:
            self.root = v
        elif u == u.parent.left_child:
            u.parent.left_child = v
        else:
            u.parent.right_child = v
        v.parent = u.parent

    def delete_fix(self, x):
        while x != self.root and x.color == 0:
            if x == x.parent.left_child:
                s = x.parent.right_child
                if s.color == 1:
                    s.color = 0
                    x.parent.color = 1
                    self.left_rotate(x.parent)
                    s = x.parent.right_child

                if s.left_child.color == 0 and s.right_child.color == 0:
                    s.color = 1
                    x = x.parent
                else:
                    if s.right_child.color == 0:
                        s.left_child.color = 0
                        s.color = 1
                        self.right_rotate(s)
                        s = x.parent.right_child

                    s.color = x.parent.color
                    x.parent.color = 0
                    s.right_child.color = 0
                    self.left_rotate(x.parent)
                    x = self.root
            else:
                s = x.parent.left_child
                if s.color == 1:
                    s.color = 0
                    x.parent.color = 1
                    self.right_rotate(x.parent)
                    s = x.parent.left_child

                if s.right_child.color == 0 and s.right_child.color == 0:
                    s.color = 1
                    x = x.parent
                else:
                    if s.left_child.color == 0:
                        s.right_child.color = 0
                        s.color = 1
                        self.left_rotate(s)
                        s = x.parent.left_child

                    s.color = x.parent.color
                    x.parent.color = 0
                    s.left_child.color = 0
                    self.right_rotate(x.parent)
                    x = self.root
        x.color = 0

    def traverse_up(self, node):
        # Traverse up the tree from the given node to the root
        # return the list of the nodes in the path
        curr = node
        path = []
        while curr.parent != None:
            path.append(curr)
            curr = curr.parent
        path.append(self.root)
        return path

    def traverse_down(self, node, bit_sequence):
        # Traverse down the tree based on the bit sequence
        # return the list of nodes in the path
        path = []
        current_node = node
        path.append(current_node)
        for bit in bit_sequence:
            if bit == "1" and current_node.left_child:
                current_node = current_node.left_child
            elif bit == "0" and current_node.right_child:
                current_node = current_node.right_child
            else:
                print("Invalid path :(")
                return None
            path.append(current_node)
        return path

    def preorder_traversal(self, node, depth, result):
        # Perform in-order traversal staying within specified depth
        # return the list of nodes in the path
        if node != self.TNULL and depth >= 0:
            result.append(node)
            self.preorder_traversal(node.left_child, depth-1, result) 
            self.preorder_traversal(node.right_child, depth-1, result)
        return result
        

    def black_height(self, node):  
        # Return the black height of the node
        curr = node
        height = 0
        while curr != self.TNULL:
            if curr.color == 0:
                height += 1
            curr = curr.left_child
        return height

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

    def minimum(self, node):
        while node.left_child != self.TNULL:
            node = node.left_child
        return node

    def maximum(self, node):
        while node.right_child != self.TNULL:
            node = node.right_child
        return node

    def total_nodes(self, root):
        if root == self.TNULL:
            return 0
        return self.total_nodes(root.left_child) + self.total_nodes(root.right_child) + 1

    def print_formatted_tree(self, node, level=0):
        # self.root.parent = HybridNode(0, 0)
        if node != self.TNULL:
            self.print_formatted_tree(node.left_child, level + 1)
            # print(' ' * 8 * level + '-> ' + str(node.parent.key) + "p" + str(node.key) + "c" + str(node.color))
            print(' ' * 8 * level + '-> '+ str(node.key)) 
            self.print_formatted_tree(node.right_child, level + 1)
    
    #citation: gfg, debugging code borrowed to make debugging quicker
    # Function to print flattened binary tree
    def print_flattened_tree(self, parent):
        flattened = []
        count = 0
        curr = parent
        while curr is not None:
            print(curr.key)
            flattened.append(curr.key)
            count+=1
            curr = curr.right
        print(count)
        return flattened
            
    def inorder_traversal(self, traversal, parent):
        # Base Case
        if parent == self.TNULL:
            return
        
        self.inorder_traversal(traversal, parent.left_child)
        # Storing the values in the list
        traversal.append(parent.key)
        self.inorder_traversal(traversal, parent.right_child)
        
    def flatten(self, root):
        # Dummy node
        dummy = HybridNode(-1, None, None)
        
        # Pointer to previous element
        prev = [dummy]
        
        # List to store the inorder traversal of the binary tree
        traversal = []
        self.inorder_traversal(traversal, root)
        
        # forming the sorted list from the list obtained
        self.form(0, traversal, prev)
        
        prev[0].left = None
        prev[0].right = None
        ret = dummy.right
        
        # Delete dummy node
        dummy = None
        return ret
    
    def form(self, pos, traversal, prev):
        # Base Case
        if pos == len(traversal):
            return
        
        prev[0].right = HybridNode(traversal[pos], None, None)
        prev[0].left = None
        
        prev[0] = prev[0].right
        
        # Calling for the next element of the list
        self.form(pos + 1, traversal, prev)


class Lexicon:
    def __init__(self):
        self.red_black_tree = RedBlackTree()  # Red-Black Tree

    def read_chapters(self, chapter_names):
        # Process words from a chapters and build the tree
        # chapter_names is the chapter names list
        # This function should do the pruning fo the Red-Black Tree
        # You can design your own function and call it for the pruning strategy
        for chapter in chapter_names:
            with open(chapter, "r") as file: #what was r again?
                for line in file:
                    each_line = line.lower().split()
                    for word in each_line:
                        node = self.red_black_tree.search(word)
                        if node is not None:
                            bin = node.histogram.search(chapter)
                            bin.word_count += 1
                            # if word == "time":
                            #     print("time", chapter, bin.word_count) 
                        else:
                            self.red_black_tree.insert(word, chapter, chapter_names)
                            node = self.red_black_tree.search(word)
                            bin = node.histogram.search(chapter)
                            bin.word_count += 1
                              
                              
        self.prune_tree(self.red_black_tree.root, chapter_names)

    def build_index(self):
        # Build the index using the remaining words in the Red-Black Tree
        index_entries = []
        nodes = self.red_black_tree.preorder_traversal(self.red_black_tree.root, 99999999, [])
        for node in nodes:
            entry = IndexEntry(node.key)
            entry.chapter_word_counts = node.histogram.chapterwise_chapter_counts()
            index_entries.append(entry)
        return index_entries
            
    def prune_tree(self, root, chapter_names):
        delete_these = []
        self.traverse_to_delete(root, delete_these, chapter_names)
        # print(delete_these)
        for node in delete_these:
            self.red_black_tree.delete(node)
        
        
    def occurence_check(self, node, chapter_names):
        count = 0
        for chapter in chapter_names:
            if node is not None:
                bin = node.histogram.search(chapter)
                if bin is not None and bin.word_count > 0:
                    count += 1
        if count == len(chapter_names):
            return True #it exists in all chapters
        else:
            return False
        
    def traverse_to_delete(self, root, delete_these, chapter_names):
        if root == self.red_black_tree.TNULL:
            return delete_these
        self.traverse_to_delete(root.left_child, delete_these, chapter_names)
        check = self.occurence_check(root, chapter_names)
        if check == True:
            # print(root.key, check)
            delete_these.append(root.key)
        self.traverse_to_delete(root.right_child, delete_these, chapter_names)
    
class IndexEntry:
    def __init__(self, word):
        self.word = word  # Word
        self.chapter_word_counts = []  # List of (chapter, word_count) tuples
        
        
# lexicon = Lexicon()
# chapter_names = ["chapter1.txt", "chapter2.txt", "chapter3.txt"]
# lexicon.read_chapters(["chapter1.txt", "chapter2.txt", "chapter3.txt"])
# print(lexicon.red_black_tree.total_nodes(lexicon.red_black_tree.root))
# print(lexicon.occurence_check(lexicon.red_black_tree.search("a"),chapter_names))
# # lexicon.red_black_tree.print_formatted_tree(lexicon.red_black_tree.root)
# print(lexicon.red_black_tree.black_height(lexicon.red_black_tree.root))

# print(lexicon.occurence_check(lexicon.red_black_tree.search("there"),chapter_names))
# print(lexicon.occurence_check(lexicon.red_black_tree.search("once"),chapter_names))
# print(lexicon.occurence_check(lexicon.red_black_tree.search("lived"),chapter_names))
# print(lexicon.occurence_check(lexicon.red_black_tree.search("time"),chapter_names))
# print(lexicon.occurence_check(lexicon.red_black_tree.search("their"),chapter_names))

# node = lexicon.red_black_tree.search("forever")
# print(node.histogram)
# node.histogram.print_chapter_counts()
# print(node.histogram.search("chapter1.txt"))



# print(lexicon.occurence_check(lexicon.red_black_tree.search("about"),chapter_names))

# bruh2 = lexicon.red_black_tree.print_flattened_tree(lexicon.red_black_tree.flatten(lexicon.red_black_tree.root))

# chapters_list = [] #list of chapters

# path = "chapterNames.txt"  #path to the chapter names file
# with open(path, "r") as f:
#     for line in f:
#         chapters_list = line.split(" ")  #split the line into a list of chapters
        
# # lexicon = Lexicon()  #create a Lexicon object
# # lexicon.read_chapters(chapters_list) #implement all the functions in python_template.py
# # print(lexicon.red_black_tree.total_nodes(lexicon.red_black_tree.root))
# # index = lexicon.build_index()
# # for entry in index:
# #     print("Entry", entry.word, ":", entry.chapter_word_counts)

# lexicon = Lexicon()  #create a Lexicon object
# lexicon.read_chapters(chapters_list) #implement all the functions in python_template.py
# # print(lexicon.red_black_tree.total_nodes(lexicon.red_black_tree.root))
# # index = lexicon.build_index()
# # for entry in index:
# #     print("Entry", entry.word, ":", entry.chapter_word_counts)
    
# lexicon.red_black_tree.print_formatted_tree(lexicon.red_black_tree.root)
# # # node = lexicon.red_black_tree.search("wonder")
# # # path = lexicon.red_black_tree.traverse_up(node)
# # path = lexicon.red_black_tree.traverse_down(lexicon.red_black_tree.root, "1111111")
# # print(path)
# # for nodes in path:
# #     print(nodes.key)