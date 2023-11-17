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
        for s in self.service_ptrs:
            if(s.location_ptr == droplocation): 
                return s
    def set_service_ptr(self, droplocation):
        pass
    def add_trip(self, trip):
        if trip.get_pick_up_location()!= self.name:
            return
        else:
            self.trips.append(trip)


class BinaryTreeNode:
    def __init__(self, departure_time=0, trip_node_ptr=None, parent_ptr=None):
        self.left_ptr= None
        self.right_ptr= None
       
        self.departure_time=departure_time

        self.trip_node_ptr=trip_node_ptr
        self.parent_ptr=parent_ptr

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
        self.root=None

    def get_height(self):
        # height of a binary tree

        def calculate_height(node):
            lheight=0
            rheight=0
            if node is None:
                return -1
            lheight= calculate_height(node.get_left_ptr())
            rheight= calculate_height(node.get_right_ptr())
            return max(lheight, rheight)+1

        #if self.root is None:
            #return 0
        return calculate_height(self.root)

    def get_number_of_nodes(self):

        #count the number of nodes in the binary tree
        def count_nodes(node):
            if node is None:
                return 0
            return 1 + count_nodes(node.get_left_ptr())+count_nodes(node.get_right_ptr())

        return count_nodes(self.root)

class BinarySearchTree(BinaryTree):
    def __init__(self):
        super().__init__()#inheritance

    def get_element_with_minimum_key(self):
        # Return the element with the minimum key (not implemented here)
        pass

    def get_element_with_maximum_key(self):
        # Return the element with the maximum key (not implemented here)
        pass

    def search_node_with_key(self, key, vehicle_number):
        # Search for a node with the given key (not implemented here)
        # node = self.root
        # if key < node.departure_time:  
        pass

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
        

    #def in_order_traversal(self, node):
        #if node:
            # Traverse the left subtree
            #self.in_order_traversal(node.left_ptr)
            #print(f"{node.departure_time} -> ", end="")
           # self.in_order_traversal(node.right_ptr)
         
    #def print_bst(self):   
        #def printTree(node, level=0):
            #if node != None:
                #printTree(node.left_ptr, level + 1)
                #print(' ' * 4 * level + '-> ' + str(node.departure_time))
                #printTree(node.right_ptr, level + 1)
        #printTree(self.bst_head)




    def add_trip(self, key, trip=None):
        # Create a new node with the provided key and trip data
        new_node = BinaryTreeNode(key, trip) #object instantition

        if self.bst_head is None:
            self.bst_head = new_node

        else:
            current = self.bst_head
            while current:
                if key < current.departure_time:
                    if current.left_ptr is None:
 
                        current.left_ptr = new_node
                        break
                    current = current.left_ptr
                elif key > current.departure_time:
                    if current.right_ptr is None:
                     
                        current.right_ptr = new_node
                        break
                    current = current.right_ptr
                else:
                    
                    break


class TravelDesk:
    def __init__(self):
        self.vehicles=[]
        self.locations=[]

    def add_trip(self, vehicle_number, seating_capacity, pick_up_location, drop_location, departure_time):
        vehicle = None
        vehicle_exists = False
        
        if not vehicle_exists:
            vehicle = Vehicle(vehicle_number, seating_capacity)
            self.vehicles.append(vehicle)


        for item in self.vehicles:
            if item.vehicle_number == vehicle_number and item.seating_capacity == seating_capacity:
                vehicle = item
                vehicle_exists = True
                break
        
        
        trip = Trip(vehicle=vehicle, pick_up_location=pick_up_location, drop_location=drop_location, departure_time=departure_time)
        vehicle.add_trip(trip)
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
                
                    def in_order_traversal(node):
                        if (node):                         
                            in_order_traversal(node.left_ptr)

                            if after_time <= node.departure_time < before_time:
                                trips_in_range.append(node.trip_node_ptr)

                          
                            in_order_traversal(node.right_ptr)
                    
                   
                    in_order_traversal(service.get_bst_head())
                   

        return trips_in_range

    
    def show_tripsbydestination(self, pick_up_location, destination,after_time, before_time):
        # Retrieve the relevant TransportService of specific destination first then iterate over the BST to find trips within a specified time range (not implemented here)
        return []

    def book_trip(self, pick_up_location, drop_location, vehicle_number, departure_time):
        
        required_trip = None
        for vehicle in self.vehicles:
            if vehicle.vehicle_number == vehicle_number:
                for trip in vehicle.trips:
                    if trip.pick_up_location == pick_up_location and trip.drop_location == drop_location and trip.departure_time == departure_time:
                        required_trip = trip
                        break
                    
                break
            
        if (required_trip.booked_seats <= required_trip.vehicle.seating_capacity):
            required_trip.booked_seats = required_trip.booked_seats + 1
            return required_trip
        
        else:
            print("Booking Failed")