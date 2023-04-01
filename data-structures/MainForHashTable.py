from HashTable import HashTable
from Client import Client

# main program to demonstrate HashTable using Client objects
client1 = Client(123, "Jack", "Jones", "555-1111", "jjones@gmail.com")
client2 = Client(234, "Maria", "Jimenez", "555-2222", "mjimenez@hotmail.com")
client3 = Client(345, "Tyler", "Baker", "555-3333", "tbaker@ymail.com")
client4 = Client(456, "Jim", "Long", "555-4444", "jlong@outlook.com")
client5 = Client(333, "Beth", "Wilson", "555-5555", "bwilson@gmail.com")

# create a HashTable to store our data and add some data
hash_table = HashTable()

hash_table.insert(client1)
hash_table.insert(client2)
hash_table.insert(client3)
hash_table.insert(client4)
hash_table.insert(client5)  # hash collision takes place and handled perfectly!

# find a client based on the client id -- create object using just the key
id = int( input("Enter client id: ") )
client = hash_table.search( Client(id) )
if client is not None:
    print("Phone: ", client.get_phone())
else:
    print("Client not found.")

# test the remove function
hash_table.remove( Client(234) )

# look for client that was removed
print("\nSearch for removed client:")
client = hash_table.search( Client(234) )
if client is not None:
    print("Phone: ", client.get_phone())
else:
    print("Client not found.")

print("\nShow the hash table structure. Notice the collision:")
print( hash_table )    