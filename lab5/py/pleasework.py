class MetroStop:
    def __init__(self, name, metro_line, fare):
        self.stop_name = name
        self.next_stop = None
        self.prev_stop = None
        self.line = metro_line
        self.fare = fare

    def get_stop_name(self):
        return self.stop_name

    def get_next_stop(self):
        return self.next_stop

    def get_prev_stop(self):
        return self.prev_stop

    def get_line(self):
        return self.line

    def get_fare(self):
        return self.fare

    def set_next_stop(self, next_stop):
        self.next_stop = next_stop

    def set_prev_stop(self, prev_stop):
        self.prev_stop = prev_stop


class MetroLine:
    def __init__(self, name):
        self.line_name = name
        self.node = None

    # Getters and setters for MetroLine class
    def get_line_name(self):
        return self.line_name

    def get_node(self):
        return self.node

    def set_node(self, node):
        self.node = node

    def print_line(self):
        stop = self.node
        while stop is not None:
            print(stop.get_stop_name())
            stop = stop.get_next_stop()
            
    def get_total_stops(self):
        stop = self.node
        total_stops = 0
        while stop is not None:
            total_stops += 1
            stop = stop.get_next_stop()
        return total_stops

    def populateLine(self, filename):
        stops = []
        with open(filename) as f:
            lines = f.readlines()
            for line in lines:
                line = line.replace("\n", "")
                line = line.replace(",", "")
                words = line.split()
                stop_name = " ".join(words[:-1])
                stop_fare = words[-1]
                stops.append((stop_name, stop_fare))
                
        metroline = filename.split('.', 1)[0]
        metrostop_prev = None
        for stop_name, stop_fare in stops:
            metrostop = MetroStop(stop_name, metroline, stop_fare)
            if metrostop_prev is not None:
                metrostop_prev.set_next_stop(metrostop)
            metrostop.set_prev_stop(metrostop_prev)
            metrostop_prev = metrostop
        self.node = metrostop_prev  # set the node to the tail node, acts as iterator


class AVLNode:
    def __init__(self, name):
        self.stop_name = name
        self.stops = []
        self.left = None
        self.right = None
        self.parent = None

    def get_stop_name(self):
        return self.stop_name

    def get_stops(self):
        return self.stops

    def get_left(self):
        return self.left

    def get_right(self):
        return self.right

    def get_parent(self):
        return self.parent

    def add_metro_stop(self, metro_stop):
        self.stops.append(metro_stop)

    def set_left(self, left):
        self.left = left

    def set_right(self, right):
        self.right = right

    def set_parent(self, parent):
        self.parent = parent


class AVLTree:
    def __init__(self):
        self.root = None
    
    def get_root(self):
        return self.root

    def set_root(self, root):
        self.root = root

    def height(self, node):
        if node is None:
            return 0
        return 1 + max(self.height(node.right), self.height(node.left))

    def string_compare(self, s1, s2):
        if s1 > s2:
            return 1
        elif s1 == s2:
            return 0
        else:
            return -1

    def balance_factor(self, node):
        return (self.height(node.left) - self.height(node.right))

    def rotate_left(self, node):
        subtree_head = node.right
        x = subtree_head.left
        subtree_head.left = node
        node.right = x
        return subtree_head

    def rotate_right(self, node):
        subtree_head = node.left
        x = subtree_head.right
        subtree_head.right = node
        node.left = x
        return subtree_head

    def balance(self, node):
        bf = self.balance_factor(node)

        # Left Heavy
        if bf > 1:
            # Left-Right Case
            if self.balance_factor(node.left) < 0:
                node.left = self.rotate_left(node.left)
            # Left-Left Case
            return self.rotate_right(node)

        # Right Heavy
        if bf < -1:
            # Right-Left Case
            if self.balance_factor(node.right) > 0:
                node.right = self.rotate_right(node.right)
            # Right-Right Case
            return self.rotate_left(node)

        return node

    def insert(self, metroStop):
        new_node = AVLNode(metroStop.stop_name)
        new_node.stops.append(metroStop)
        if not self.root:
            self.root = new_node
            return

        current = self.root
        while current:
            parent = current
            comparison_factor = self.string_compare(current.stop_name, metroStop.stop_name)
            if comparison_factor == 1:
                current = current.left
            elif comparison_factor == -1:
                current = current.right
            else:  # comparison_factor == 0
                current.stops.append(metroStop)
                return

        comparison_factor = self.string_compare(parent.stop_name, metroStop.stop_name)
        if comparison_factor == 1:
            parent.left = new_node
        elif comparison_factor == -1:
            parent.right = new_node

        # Rebalance the tree
        self.root = self.balance(self.root)

    def inOrderTraversal(self, node):
        if node is None:
            return
        self.inOrderTraversal(node.left)
        print(node.stop_name)
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


def main():
    filenames = ["blue.txt", "green.txt", "magenta.txt", "orange.txt", "red.txt", "violet.txt", "yellow.txt"]

    metrolines = []
    tree = AVLTree()
    for line in filenames:
        metroline = MetroLine(line)
        metroline.populateLine(line)
        tree.populateTree(metroline)
        metrolines.append(metroline)
    
    print("Total Nodes:", tree.getTotalNodes())


if __name__ == "__main__":
    main()
