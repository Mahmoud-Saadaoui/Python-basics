# Creating dictionaries in Python

# Method 1: Using curly braces
task = {'id': 1, 'title': 'Go to the store', 'done': True}
print(task)
# Output: {'id': 1, 'title': 'Go to the store', 'done': True}

# Method 2: Using dict() constructor with list of tuples
task2 = dict([('id', 1), ('title', 'Go to the store'), ('done', True)])
print(task2)
# Output: {'id': 1, 'title': 'Go to the store', 'done': True}

# Accessing dictionary values
print(task['id'])      # Output: 1
print(task2['title'])  # Output: Go to the store

# Trying to access a non-existent key raises KeyError
# print(task['due_date'])  # Would raise: KeyError: 'due_date'

# Another dictionary example with numeric keys
Employees = {1:'Saeed', 2:'Rasha', 3:'Marwa', 4:'Hela'}
print(Employees)
# Output: {1: 'Saeed', 2: 'Rasha', 3: 'Marwa', 4: 'Hela'}

# Accessing value by key
print(Employees[1])  # Output: Saeed

# Dictionary order doesn't matter for access
Employees = {4: 'Hela', 3: 'Marwa', 2: 'Rasha', 1: 'Saeed'}
print(Employees[1])  # Still outputs: Saeed

# Modifying dictionary values
task['title'] = 'Finish the homework'
task['done'] = False
print(task)
# Output: {'id': 1, 'title': 'Finish the homework', 'done': False}

# Adding new key-value pairs
task['due_date'] = 'today'
print(task)
# Output: {'id': 1, 'title': 'Finish the homework', 'done': False, 'due_date': 'today'}

# Creating an empty dictionary and adding items
task = {}
task['id'] = 0
task['title'] = 'Write a lesson about python dictionaries'
task['done'] = False
print(task)
# Output: {'id': 0, 'title': 'Write a lesson about python dictionaries', 'done': False}

# Checking if a key exists in dictionary
print('id' in task)      # Output: True
print('comment' in task)  # Output: False

# Getting dictionary length
print(len(task))  # Output: 3

# Removing a key-value pair
del task['done']
print(task)
# Output: {'id': 0, 'title': 'Write a lesson about python dictionaries'}