class Vehicle:
    def __init__(self, vehicle_number, seating_capacity):
        self.vehicle_number = vehicle_number
        self.seating_capacity = seating_capacity
        self.trips = []

    def get_vehicle_number(self):
        return self.vehicle_number

    def set_vehicle_number(self, new_vehicle_number):
        self.vehicle_number = new_vehicle_number

    def get_seating_capacity(self):
        return self.seating_capacity

    def set_seating_capacity(self, new_seating_capacity):
        self.seating_capacity = new_seating_capacity

    def get_trips(self):
        return self.trips

    def add_trip(self, trip):
        self.trips.append(trip)


class Trip:
    def __init__(self, vehicle, pick_up_location, drop_location, departure_time):
        self.vehicle = vehicle
        self.pick_up_location = pick_up_location
        self.drop_location = drop_location
        self.departure_time = departure_time
        self.booked_seats = 0

    def get_vehicle(self):
        return self.vehicle

    def get_pick_up_location(self):
        return self.pick_up_location

    def set_pick_up_location(self, new_pick_up_location):
        self.pick_up_location = new_pick_up_location

    def get_drop_location(self):
        return self.drop_location

    def set_drop_location(self, new_drop_location):
        self.drop_location = new_drop_location

    def get_departure_time(self):
        return self.departure_time

    def set_departure_time(self, new_departure_time):
        self.departure_time = new_departure_time

    def get_booked_seats(self):
        return self.booked_seats

    def set_booked_seats(self, new_booked_seats):
        self.booked_seats = new_booked_seats


class Location:
    def __init__(self, name, service_ptr=None):
        self.name = name
        self.service_ptr = service_ptr
        self.trips = []

    def get_name(self):
        return self.name

    def set_name(self, new_name):
        self.name = new_name

    def get_service_ptr(self):
        return self.service_ptr

    def set_service_ptr(self, new_service_ptr):
        self.service_ptr = new_service_ptr

    def add_trip(self, trip):
        if trip.get_pick_up_location() != self.name:
            return
        else:
            self.trips.append(trip)


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
            # loop down to find the leftmost leaf
            while(node.left_ptr is not None):
                node = node.left_ptr
            
            return node    

        if self.root is None:
            return 0
        return find_element_with_minimum_key(self.root)

    def get_element_with_maximum_key(self):
        # Return the element with the maximum key (not implemented here)
        def find_element_with_maximum_key(node):
            # loop down to find the leftmost leaf
            while(node.right_ptr is not None):
                node = node.right_ptr
            
            return node    

        if self.root is None:
            return 0
        return find_element_with_maximum_key(self.root)


    def search_node_with_key(self, key):
        # Base Cases: root is null or key is present at root
        if root is None or self.root.key == key:
            return root
    
        # Key is greater than root's key
        if self.root.key < key:
            return search_node_with_key(key)
    
        # Key is smaller than root's key
        return search_node_with_key(key)

    def get_successor_node(self, node):
        # Find the successor node of the given node (not implemented here)
        pass

    def get_predecessor_node(self, node):
        # Find the predecessor node of the given node (not implemented here)
        pass


class TransportService:
    def __init__(self, location_ptr=None, bst_head=None):
        self.location_ptr = location_ptr
        self.bst_head = bst_head

    def get_location_ptr(self):
        return self.location_ptr

    def set_location_ptr(self, new_location_ptr):
        self.location_ptr = new_location_ptr

    def get_bst_head(self):
        return self.bst_head

    def set_bst_head(self, new_bst_head):
        self.bst_head = new_bst_head

    def add_trip(self, key, trip):
        # Add the trip to the BST (not implemented here)
        pass


class TravelDesk:
    def __init__(self):
        self.vehicles = []
        self.locations = []

    def add_trip(self, vehicle_number, seating_capacity, pick_up_location, drop_location, departure_time):
        # Check if the vehicle already exists, if not, create a new one with the seating capacity (not implemented here)
        
        vehicle = None
        vehicle_exists = False
        
        if not self.vehicles:
            for item in self.vehicles:
                if(item.vehicle_number == vehicle_number and item.seating_capacity == seating_capacity):
                    vehicle = item
                    vehicle_exists = True
                    break
        if not vehicle_exists:
            vehicle = Vehicle(vehicle_number, seating_capacity)    

        # Create a new trip and add it to the appropriate objects (not implemented here)
        
        trip = Trip(vehicle=vehicle, pick_up_location=pick_up_location, drop_location=drop_location, departure_time=departure_time)
        vehicle.add_trip(trip)
        
        # Create or retrieve the Location object and associated pick up location (not implemented here)
        location = None
        location_exists = False
        
        if not self.locations:
            for item in self.locations:
                if(item.name == pick_up_location):
                    location = item
                    location_exists = True
                    break
        if not location_exists:
            location = Location(pick_up_location)   
        
        location.add_trip(trip)
        
        # Add the trip to the TransportService's BST (not implemented here)
        
        for services in location.get_service_ptr
        
        
        
        
        

    def show_trips(self, pick_up_location, after_time, before_time):
        # Retrieve the relevant TransportService first then iterate over the BST to find trips within a specified time range (not implemented here)
        return []

    def book_trip(self, pick_up_location, drop_location, vehicle_number, departure_time):
        # Find the corresponding trip to book the seat and have proper validation (not implemented here)
        return None

# Create nodes
root = BinaryTreeNode(1)
root.left_ptr = BinaryTreeNode(2)
root.right_ptr = BinaryTreeNode(3)
root.left_ptr.left_ptr = BinaryTreeNode(4)
root.left_ptr.right_ptr = BinaryTreeNode(5)

# Create the binary tree
binary_tree = BinaryTree()
binary_tree.root = root
print(binary_tree.get_height())