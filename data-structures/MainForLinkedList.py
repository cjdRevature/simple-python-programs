from LinkedList import LinkedList

# create the LinkedList and add some items to front, back, middle
num_list = LinkedList()

# test the add methods
num_list.add_first(99)   # Add 99
num_list.add_first(44)   # Add 44 to the front - 44 99
num_list.add_first(42)   # Add 42 to the front - 42 44 99
num_list.add_last(66)    # Add 66 to the BACK - 42 44 99 66
num_list.add_last(17)    # Add 17 to the BACK - 42 44 99 66 17
num_list.add_at(2, 23)   # Add 23 at index 2 - 42 44 23 99 66 17
num_list.add_at(4, 13)   # Add 13 at index 4 - 42 44 23 99 13 66 17

# show the current list
print("Current list after adding items:", num_list.get_list())

# test the get methods
print( "first:", num_list.get_first() )
print( "last:", num_list.get_last() )
print( "index 2:", num_list.get_at(2) )

# show the current list
print("\nCurrent list after getting items:", num_list.get_list())

# test the remove methods
num_list.remove_first()   # Remove 42 - 44 23 99 13 66 17
num_list.remove_last()    # Remove 17 - 44 23 99 13 66
num_list.remove_at(2)     # Remove 99 - 44 23 13 66

# show the current list
print("\nCurrent list after removing items:", num_list.get_list())

# test some methods in the LinkedList
print( "\nTesting some methods..." )
print( "contains(99):", num_list.contains(99) )
print( "is_empty():", num_list.is_empty() )
print( "get_length():", num_list.get_length() )