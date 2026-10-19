from collections import deque

# Create a queue
queue = deque(["Zero", "One", "Two"])

print("Initial Queue:", queue)

# Remove an element from the right
print("Removed:", queue.pop())

# Add elements to the right
queue.append("Three")
queue.append("Four")
queue.append("Five")

print("After Append:", queue)

# Add an element to the left
queue.appendleft("Minus One")

print("After Append Left:", queue)

# Remove an element from the right
print("Pop:", queue.pop())

# Remove an element from the left
print("Pop Left:", queue.popleft())

print("Final Queue:", queue)