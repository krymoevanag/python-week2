# Initial list
my_list = []

# Append elements to the list
my_list.append(10)
my_list.append(20)
my_list.append(30)
my_list.append(40)

# Print the initial list
print("Initial list:", my_list)

# Insert the value 15 at the second position
my_list.insert(1, 15)

# Extend the list with another list
my_list.extend([50, 60, 70])

# Print the extended list
print("Extended list:", my_list)

# Remove the last element
my_list.pop()

# Sort the list in ascending order
my_list.sort()

# Print the sorted list
print("Sorted list:", my_list)

# Find and print the index of the value 30
index_of_30 = my_list.index(30)
print("The index of 30 in the sorted list is:", index_of_30)
