
# def populateLine(filename):
#     #for each line in the file, make a node and set the next to the next node:
#     with open(filename) as f:
#         lines = f.readlines()
#         stops = {}
#         for line in lines:
#             line = line.replace("\n", "")
#             line = line.replace(",", "")
#             words = line.split()
#             stop_name = words[0]
#             for word in words[1:-1]:
#                 stop_name = stop_name + " " + word
#             # print(stop_name)
#             stop_fare = words[-1]
#             # print(stop_fare)
#             stops[stop_name] = stop_fare      
#         # print(stops)
        

# # populateLine("magenta.txt")
# # text = "magenta.txt"
# # sep = '.'
# # metroline = text.split('.', 1)[0]
# # print(metroline)\
    
# # s1 = "bruh"
# # s2 = "bruh2"
# # print(max(s1,s2))

class MetroStop:
    def __init__(self, name, metroLine, fare):
        self.stopName = name
        self.nextStop = None
        self.prevStop = None
        self.line = metroLine
        self.fare = fare

    def getStopName(self):
        return self.stopName

    def getNextStop(self):
        return self.nextStop

    def getPrevStop(self):
        return self.prevStop

    def getLine(self):
        return self.line

    def getFare(self):
        return self.fare

    def setNextStop(self, next):
        self.nextStop = next

    def setPrevStop(self, prev):
        self.prevStop = prev


class MetroLine:
    def __init__(self, name):
        self.lineName = name
        self.node = None

    def getLineName(self):
        return self.lineName

    def getNode(self):
        return self.node

    def setNode(self, node):
        self.node = node

    def printLine(self):
        stop = self.node
        while stop is not None:
            print(stop.getStopName())
            stop = stop.getNextStop()

    def getTotalStops(self):
        pass

    def populateLine(self, filename):
        #for each line in the file, make a node and set the next to the next node:
        stops = read_file(filename)
        metroline = filename.split('.', 1)[0]
        metrostop_prev = None
        for stop_name, stop_fare in stops:
            metrostop = MetroStop(stop_name, metroline, stop_fare)
            if metrostop_prev is not None:
                metrostop_prev.setNextStop(metrostop)
            metrostop.setPrevStop(metrostop_prev)
            metrostop_prev = metrostop
        self.node = metrostop_prev #set the node to the tail node, acts as iterator
        
class AVLNode:
    def __init__(self, name):
        self.stopName = name
        self.stops = []
        self.left = None
        self.right = None
        self.parent = None

    def getStopName(self):
        return self.stopName

    def getStops(self):
        return self.stops

    def getLeft(self):
        return self.left

    def getRight(self):
        return self.right

    def getParent(self):
        return self.parent

    def addMetroStop(self, metroStop):
        self.stops.append(metroStop)
        
class AVLNode:
    def __init__(self, stop_name):
        self.stopName = stop_name
        self.left = None
        self.right = None
        self.stops = []

class AVLTree:
    def __init__(self):
        self.root = None

    def stringCompare(self, s1, s2):
        if s1 > s2:
            return 1
        elif s1 == s2:
            return 0
        else:
            return -1

    def height(self, node):
        if node is None:
            return 0
        return 1 + max(self.height(node.right), self.height(node.left))

    def balanceFactor(self, node):
        return (self.height(node.left) - self.height(node.right))

    def rotateLeft(self, node):
        subtree_head = node.right
        x = subtree_head.left
        subtree_head.left = node
        node.right = x
        return subtree_head

    def rotateRight(self, node):
        subtree_head = node.left
        x = subtree_head.right
        subtree_head.right = node
        node.left = x
        return subtree_head

    def balance(self, node):
        bf = self.balanceFactor(node)

        # Left Heavy
        if bf > 1:
            # Left-Right Case
            if self.balanceFactor(node.left) < 0:
                node.left = self.rotateLeft(node.left)
            # Left-Left Case
            return self.rotateRight(node)

        # Right Heavy
        if bf < -1:
            # Right-Left Case
            if self.balanceFactor(node.right) > 0:
                node.right = self.rotateRight(node.right)
            # Right-Right Case
            return self.rotateLeft(node)

        return node

    def insert(self, metroStop):
        new_node = AVLNode(metroStop.stopName)
        new_node.stops.append(metroStop)
        if not self.root:
            self.root = new_node
            return

        current = self.root
        while current:
            parent = current
            comparison_factor = self.stringCompare(current.stopName, metroStop.stopName)
            if comparison_factor == 1:
                current = current.left
            elif comparison_factor == -1:
                current = current.right
            else:  # comparison_factor == 0
                current.stops.append(metroStop)
                return

        comparison_factor = self.stringCompare(parent.stopName, metroStop.stopName)
        if comparison_factor == 1:
            parent.left = new_node
        elif comparison_factor == -1:
            parent.right = new_node

        # Rebalance the tree
        self.root = self.balance(self.root)

    def populateTree(self, metroLine):
        tail = metroLine.node
        while tail.getPrevStop() is not None:
            self.insert(tail)
            tail = tail.getPrevStop()

    def inOrderTraversal(self, node):
        if node is None:
            return
        self.inOrderTraversal(node.left)
        print(node.stopName)
        self.inOrderTraversal(node.right)

    def getTotalNodes(self, node):
        total = 0
        queue = []
        root = self.root
        queue.append(root)

        while queue:
            current_node = queue.pop(0)
            total += 1
            if current_node.left is not None:
                queue.append(current_node.left)
            if current_node.right is not None:
                queue.append(current_node.right)

        return total


def read_file(filename):
    with open(filename) as f:
        lines = f.readlines()
        stops = {}
        for line in lines:
            line = line.replace("\n", "")
            line = line.replace(",", "")
            words = line.split()
            stop_name = words[0]
            for word in words[1:-1]:
                stop_name = stop_name + " " + word
            # print(stop_name)
            stop_fare = words[-1]
            # print(stop_fare)
            stops[stop_name] = stop_fare      
        # print(stops)
    return stops
    
    

filenames = []
filenames.append("blue.txt")
filenames.append("green.txt")
filenames.append("magenta.txt")
filenames.append("orange.txt")
filenames.append("red.txt")
filenames.append("violet.txt")
filenames.append("yellow.txt")

metrolines = []
tree = AVLTree()
for line in filenames:
    metroline = MetroLine(line)
    metroline.populateLine(line)
    tree.populateTree(metroline)
    metrolines.append(metroline)
    
print(AVLTree.height())