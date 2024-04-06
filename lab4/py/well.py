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
        self.service_ptrs = []
        self.trips = []

    def get_name(self):
        return self.name

    def set_name(self, new_name):
        self.name = new_name

    def get_service_ptr(self, droplocation):
        for service in self.service_ptrs:
            if(service.location_ptr == droplocation): 
                return service

    def set_service_ptr(self, droplocation):
        pass

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

    def find_element_with_minimum_key(self, node):
        # Loop down to find the leftmost leaf
        while(node.left_ptr is not None):
            node = node.left_ptr
        
        return node    
        
    def get_element_with_minimum_key(self):
        # Return the element with the minimum key (not implemented here)

        if self.root is None:
            return None  # Return None for an empty tree
        return self.find_element_with_minimum_key(self.root)

    def find_element_with_maximum_key(self, node):
        # Loop down to find the rightmost leaf
        # print(node.departure_time)
        while(node.right_ptr is not None):
            node = node.right_ptr 
        return node    

    def get_element_with_maximum_key(self):
        # Return the element with the maximum key (not implemented here)
        if self.root is None:
            return None  # Return None for an empty tree
        return self.find_element_with_maximum_key(self.root)
        
    def search_node_with_key(self, key, node=None):
        def search_helper(key, node):
             
            if node is None or node.departure_time== key:
                return node

            elif key > node.departure_time:
                return search_helper(key, node.right_ptr)

            elif key < node.departure_time:
                return search_helper(key, node.left_ptr)
            
            
        return search_helper(key, self.root)
        

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
            if node.departure_time < current.departure_time:
                successor = current
                current = current.left_ptr
            elif node.departure_time > current.departure_time:
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
            if node.departure_time > current.departure_time:
                predecessor = current
                current = current.right_ptr
            elif node.departure_time < current.departure_time:
                current = current.left_ptr
            else:
                break  # Node with the same key found, no need to continue

        return predecessor


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
        
    #functions to print and debug
        
    def printTree(self, node, level=0):
        node = self.bst_head
        if node != None:
            self.printTree(node.left_ptr, level + 1)
            print(' ' * 4 * level + '-> ' + str(node.departure_time))
            self.printTree(node.right_ptr, level + 1)

    def in_order_traversal(self, node):
        if node:
            # Traverse the left subtree
            self.in_order_traversal(node.left_ptr)
            
            # Print the current node's departure_time
            print(f"{node.departure_time} -> ", end="")
            
            # Traverse the right subtree
            self.in_order_traversal(node.right_ptr)

    def print_tree(self):
        if self.bst_head:
            print("Printing Binary Search Tree:")
            self.in_order_traversal(self.bst_head)
            print("None")  # Print None to indicate the end of the tree
        else:
            print("BST is empty.")
         
    def print_bst(self):   
        def printTree(node, level=0):
            if node != None:
                printTree(node.left_ptr, level + 1)
                print(' ' * 4 * level + '-> ' + str(node.departure_time))
                printTree(node.right_ptr, level + 1)
        printTree(self.bst_head)
        
    #functions to print and debug ...end.

    def add_trip(self, key, trip=None):
        # Create a new node with the provided key and trip data
        new_node = BinaryTreeNode(key, trip)

        if self.bst_head is None:
            # If the BST is empty, make the new node the root
            #just in case, not necessary since i'm handling this outside
            self.bst_head = new_node
        else:
            # Otherwise, traverse the BST to find the insertion point
            current = self.bst_head
            while current:
                if key < current.departure_time:
                    # If the key is smaller, move to the left subtree
                    if current.left_ptr is None:
                        # If there's no left child, insert the new node here
                        current.left_ptr = new_node
                        break
                    current = current.left_ptr
                elif key > current.departure_time:
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

class TravelDesk:
    def __init__(self):
        self.vehicles = []
        self.locations = []

    def add_trip(self, vehicle_number, seating_capacity, pick_up_location, drop_location, departure_time):
        # Check if the vehicle already exists, if not, create a new one with the seating capacity (not implemented here)
        
        vehicle = None
        vehicle_exists = False
        
        for item in self.vehicles:
            if item.vehicle_number == vehicle_number and item.seating_capacity == seating_capacity:
                vehicle = item
                vehicle_exists = True
                break
        
        if not vehicle_exists:
            vehicle = Vehicle(vehicle_number, seating_capacity)
            self.vehicles.append(vehicle)

        # Create a new trip and add it to the appropriate objects (not implemented here)
        
        trip = Trip(vehicle=vehicle, pick_up_location=pick_up_location, drop_location=drop_location, departure_time=departure_time)
        vehicle.add_trip(trip)

        # Create or retrieve the Location object and associated pick-up location (not implemented here)
        
        location = None
        location_exists = False
        
        for item in self.locations:
            if item.name == pick_up_location:
                location = item
                location_exists = True
                break
        
        if not location_exists:
            location = Location(pick_up_location)
            self.locations.append(location)
        
        location.add_trip(trip)

        # Add the trip to the TransportService's BST (not implemented here)
        
        service_exists = False
        for service in location.service_ptrs:
            # service.printTree()
            if service.location_ptr == drop_location:
                service.add_trip(departure_time, trip)
                service_exists = True
                break
            
        if not service_exists:
            bst_head = BinaryTreeNode(departure_time=departure_time, trip_node_ptr=trip)
            service = TransportService(drop_location, bst_head=bst_head)
            location.service_ptrs.append(service)


    def show_trips(self, pick_up_location, after_time, before_time):
        # Retrieve the relevant TransportService first
        
        trips_in_range = []
        
        for location in self.locations:
            if location.name == pick_up_location:
                for service in location.service_ptrs:
                    # Perform an in-order traversal of the BST to find trips within the time range
                    def in_order_traversal(node):
                        if node:
                            # Traverse the left subtree
                            in_order_traversal(node.left_ptr)

                            # Check if the node's departure_time is within the specified range
                            if after_time <= node.departure_time < before_time:
                                trips_in_range.append(node.trip_node_ptr)

                            # Traverse the right subtree
                            in_order_traversal(node.right_ptr)
                    
                    # Start the traversal from the BST's head 
                    in_order_traversal(service.get_bst_head())
                   
        
        # if not relevant_service:
        #     # No relevant service found
        #     return []

        return trips_in_range

    
    def show_tripsbydestination(self, pick_up_location, destination,after_time, before_time):
        # Retrieve the relevant TransportService of specific destination first then iterate over the BST to find trips within a specified time range (not implemented here)

        trips_in_range = []
        
        for location in self.locations:
            if location.name == pick_up_location:
                for service in location.service_ptrs:
                    # Perform an in-order traversal of the BST to find trips within the time range
                    def in_order_traversal(node):
                        if node:
                            # Traverse the left subtree
                            in_order_traversal(node.left_ptr)

                            # Check if the node's departure_time is within the specified range
                            if after_time <= node.departure_time < before_time and node.trip_node_ptr.drop_location == destination :
                                trips_in_range.append(node.trip_node_ptr)

                            # Traverse the right subtree
                            in_order_traversal(node.right_ptr)
                    
                    # Start the traversal from the BST's head 
                    in_order_traversal(service.get_bst_head())
                   
        
        # if not relevant_service:
        #     # No relevant service found
        #     return []

        return trips_in_range

    def book_trip(self, pick_up_location, drop_location, vehicle_number, departure_time):
        # Find the corresponding trip to book the seat and have proper validation (not implemented here)
                
        required_trip = None
        for vehicle in self.vehicles:
            if vehicle.vehicle_number == vehicle_number:
                for trip in vehicle.trips:
                    if trip.pick_up_location == pick_up_location and trip.drop_location == drop_location and trip.departure_time == departure_time:
                        required_trip = trip
                        break
                    
                break
            
        if required_trip is not None:
            if required_trip.booked_seats <= required_trip.vehicle.seating_capacity:
                required_trip.booked_seats = required_trip.booked_seats + 1
                return required_trip
        
        else:
            print("Booking Failed")
            
            
         
        
    
# bst = TransportService()
# bst.add_trip(50)
# bst.add_trip(30)
# bst.add_trip(70)
# bst.add_trip(20)
# bst.add_trip(40)
# bst.add_trip(60)
# bst.add_trip(80)
# bst.printTree()


# bst = TransportService()
# bst.add_trip(50)
# bst.add_trip(30)
# bst.add_trip(70)
# bst.add_trip(20)
# bst.add_trip(40)
# bst.add_trip(60)
# bst.add_trip(80)

# # Print the BST with slashes to represent links
# bst.print_bst()



# travel_desk = TravelDesk()

# # Add trips
# for i in range(10):
#     vehicle_number = "A" + str(i)
#     travel_desk.add_trip(vehicle_number, 4, "LocationA", "LocationB", 1000 + i * 100)

# # Add trips for LocationX
# for i in range(10):
#     vehicle_number = "X" + str(i)
#     travel_desk.add_trip(vehicle_number, 3, "LocationX", "LocationY", 1500 + i * 100)

# # Verify that the tree is a proper BST
# locationA = None
# locationX = None

# print(travel_desk.locations)
# for i in travel_desk.locations:
#     print(i.name)
    
    
# print(travel_desk.vehicles)
# for i in travel_desk.vehicles:
#     print(i.vehicle_number)
    
# for i in travel_desk.locations:
#     if i.name == "LocationA":
#         locationA = i
# for i in travel_desk.locations:
#     if i.name == "LocationX":
#         locationX = i
    
# for loc in travel_desk.locations:
#     for service in loc.service_ptrs:
#         service.print_bst()
