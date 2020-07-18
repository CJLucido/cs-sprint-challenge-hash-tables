import math

#  Hint:  You may not need all of these.  Remove the unused functions.
class Ticket:
    def __init__(self, source, destination): #, next=None
        self.source = source
        self.destination = destination
        # self.next = None


def reconstruct_trip(tickets, length):
    """
    YOUR CODE HERE
    """
    # Your code here
    
    
    cache = {}
    route = []*length

    for ticket in tickets:

        if cache.get(ticket.source):
            pass
        else:
            cache[ticket.source] = ticket.destination
        

    route.append(cache["NONE"])
    i= 0
    while route[-1] != "NONE":

        next_destination = route[i]
        route.append(cache[next_destination])
        i +=1

    return route



# class LinkedList:
#     def __init__(self):
#         self.head = None
    
#     def find_by_key(self, key):
#         current = self.head

#         while current is not None:
#             if current.source == key:
#                 return current
#             current = current.next
    
#     def insert_at_tail(self, key, value):
#         node = Ticket(key, value)

#         if self.head is None:
#             self.head = node
#         else:
#             current = self.head
#             print("adding to tail")
#             while current.next is not None:
#                 current = current.next
#             current.next = node
    
#     def get_next(self):
#         current = self.head

#         while current is not None:
#             return current.next


#     def delete(self, key):
#         current = self.head

#         if current is None:
#             return None

#         if current.key == key:
#             self.head = current.next
#             return current #it will just be garbage collected eventually (repointing to next in line)

#         else:
#             previous = current
#             current = current.next

#             while current is not None:
#                 if current.key == key: # found it
#                     previous.next = current.next
#                     return current #what was deleted
                
#                 else:
#                     previous = current
#                     current = current.next
            
#             return None

# class HashTable:
#     """
#     A hash table that with `capacity` buckets
#     that accepts string keys

#     Implement this.
#     """

#     def __init__(self, capacity):
#         # Your code here
#         # LL = LinkedList()
#         self.capacity = []
#         for _ in range(0, capacity):
#             self.capacity.append(LinkedList())
#         self.capacity_entered = capacity
#         self.entry_counter = 0
#         self.load_factor = self.entry_counter / self.capacity_entered
#         # print(self.capacity)

#         if self.load_factor > .7:
#             self.resize(len(self.capacity) * 2)
#         elif self.load_factor < .2:
#             self.resize(math.floor(len(self.capacity) / 2))

#     def get_num_slots(self):
#         return len(self.capacity)

#     def get_load_factor(self):

#         return self.load_factor

#     def fnv1(self, key):
        
#         hash_offset_basis = 14695981039346656037
#         hash = hash_offset_basis
#         fnv_prime = 1099511628211
#         # for byte in key:
#         hash = hash * fnv_prime
#         hash = hash ^ int.from_bytes(bytes(key, 'utf-8'), 'big')

#         return hash


#     def djb2(self, key):
#         """
#         DJB2 hash, 32-bit

#         Implement this, and/or FNV-1.
#         """
#         # Your code here
#         hash = 5381

#         for char in key:
#             hash = ((hash << 5) + hash) + ord(char)
#         return hash

#     def hash_index(self, key):
#         return self.fnv1(key) % self.capacity_entered

#     def put(self, key, value):

#         new_key = self.hash_index(key)
        
#         if self.capacity[new_key] != None:
#             print("warning about to overwrite with PUT")

#         chain_in_arr = self.capacity[new_key]

#         if chain_in_arr.find_by_key(key) != None:
#              print("That key already exists!")
#              if chain_in_arr.find_by_key(key).destination == value:
#                  print("That key AND value pair already exists!")
#             #  else: # OVERWRITE THE VALUE
#             #      chain_in_arr.find_by_key(key).destination = value
#         else:
#             chain_in_arr.insert_at_tail(key, value)
#             self.entry_counter += 1



#     def delete(self, key):

#         new_key = self.hash_index(key)
#         chain_in_arr = self.capacity[new_key]
#         if chain_in_arr.find_by_key(key) == None:
#              print("That key value pair doesn't exist!")
#         else:
#             chain_in_arr.delete(key)
#         self.entry_counter -= 1
#         print("successful delete")


#     def get(self, key):

#         new_key = self.hash_index(key)

#         chain_in_arr = self.capacity[new_key]
#         if chain_in_arr.find_by_key(key) != None:
#              print("Found", chain_in_arr.find_by_key(key))
#              return chain_in_arr.find_by_key(key)
#         else:
#             print("Couldn't find the droid you're looking for, even combed the desert")
#             return 0

#     def resize(self, new_capacity):

#         replacement = []
        
#         if new_capacity >= self.capacity_entered:
#           addToList = [None] * (new_capacity - self.capacity_entered)
        
#           for i in addToList:
#             self.capacity.append(i)

#           for i in range(0, len(self.capacity)):
#             if self.capacity[i] != None:
#               if self.capacity[i].head != None:
#                     current = self.capacity[i].head
#                     print("current next", current)
#                     if current.next == None:
#                         replacement.append(current) # do the first one
#                         # print("being done")
                    
#                     while current.next != None:
#                         replacement.append(current) #do everything inbetween
#                         print("NOT being done")
#                         current = current.next
#                     replacement.append(current) # has to do the last one
#                     print("did it", replacement)

#           for i in range(0, len(self.capacity)):
#                         self.capacity[i] = LinkedList()   

#           for i in replacement:
#                         self.put(i.key, i.value)

#           print("should exist", len(replacement))
#           print("should exist", self.capacity)
#         else:
#           replacement = self.capacity[:new_capacity]

#           return replacement


# def reconstruct_trip(tickets, length):
#     """
#     YOUR CODE HERE
#     """
#     # Your code here

#     ht = HashTable(length)

#     unused_tickets = []

#     route = []

#     for i in range(0, len(tickets)) :
#         # new_ticket = list(ticket.items())
#         # print(ht.get(tickets[i].source))
#         test = ht.get(tickets[i].source)
#         if test == 0 and ht.get("NONE") != 0:  
#             for j in range(0, len(tickets)):
                
#                 if ht.get('NONE').destination == tickets[j].source:
#                     print("hit4")
#                     ht.put(tickets[j].source, tickets[j].destination)
#                     print(ht.get(tickets[j].source).destination)
#                     for k in range(0, len(tickets)): 
#                         print("hit3")
#                         if ht.get('NONE').destination != tickets[k].source and ht.fnv1(tickets[k-1].destination) == ht.fnv1(tickets[k].source) and tickets[k].source != "NONE":
#                             ht.put(tickets[k].source, tickets[k].destination)
#                         elif ht.get('NONE').destination != tickets[k].source and tickets[k].source != "NONE" and ht.get(tickets[k].source) != 0:
#                             unused_tickets.append(i)
#                             print("appending", unused_tickets)


#                 # else:
#                 #     continue
#             # pass
#         elif test == 0 and tickets[i].source == "NONE" and ht.get("NONE") == 0:
#             ht.put(tickets[i].source, tickets[i].destination)
#             print("DO THIS ONCE")
#         else:
#             continue

#     print(unused_tickets)
#     while unused_tickets != []:
#         for i in unused_tickets:
#             if tickets[i].source != "NONE" and ht.get('NONE').destination != tickets[i].source and ht.fnv1(tickets[i-1].source) == ht.fnv1(tickets[i].destination):
#                 ht.put(tickets[i].source, tickets[i].destination)
#                 print("I", i)
#                 unused_tickets.remove(i)
                                     
#     start_point = ht.get("NONE")
#     # print("startpoint", start_point.get_next())
#     route.append(start_point.destination)
#     current = start_point
#     print("start", start_point.destination)
#     while current != 0 and current.destination != 'NONE':
#         route.append(current.destination)
#         print(route)
#         current = ht.get(current.destination)
#         print("current", current.destination)

#     return route

# I have a hash table, every ticket in the table has a key
# the hash table is taking the tickets and adding them to a linked list
#I need to ensure that the first ticket is NONE for the source
# then I need to check for a match of the source's destination