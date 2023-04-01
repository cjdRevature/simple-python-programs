from Queue import Queue

# create the Queue and add some items
num_queue = Queue()

# test the add method
num_queue.enqueue(99)   # Add 99 - 99
num_queue.enqueue(44)   # Add 44 - 44 99
num_queue.enqueue(42)   # Add 42 - 42 44 99
num_queue.enqueue(66)   # Add 66 - 66 42 44 99
num_queue.enqueue(17)   # Add 17 - 17 42 44 99 66
num_queue.enqueue(23)   # Add 23 - 23 42 44 99 66 17
num_queue.enqueue(13)   # Add 13 - 13 42 44 23 99 66 17

# show the current queue
print("Current queue after adding items:", num_queue.get_queue())

# test the get methods
print( "\nlength:", num_queue.get_length() )
print( "is_empty:", num_queue.is_empty() )
print( "peek:", num_queue.peek() )

# show the current queue
print("\nDequeuing some items...")

# test the dequeue method
for i in range(5):
    print( "dequeue:", num_queue.dequeue() )
    
# show the current queue
print("\nCurrent queue after dequeuing some items:", num_queue.get_queue())
print("Current length of the queue:", num_queue.get_length())
print("is_empty:", num_queue.is_empty())

# test the dequeue method and dequeue off too many
print( "\nDequeuing too many items..." )
for i in range(5):
    print( "dequeue:", num_queue.dequeue() )

# show the current queue
print("\nCurrent queue after dequeuing more items:", num_queue.get_queue())
print("Current length of the queue:", num_queue.get_length())
print("is_empty:", num_queue.is_empty())