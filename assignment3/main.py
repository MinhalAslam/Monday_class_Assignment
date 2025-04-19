# Control Flow (if, elif, else)
x = 10

if x > 0:
    print("x is positive")
elif x == 0:
    print("x is zero")
else:
    print("x is negative")

# Loop (for loop)
fruits = ["apple", "banana", "cherry"]

for fruit in fruits:
    print(f"I like {fruit}")

# While Loop
count = 0

while count < 5:
    print("Count is:", count)
    count += 1
# break and continue
for i in range(10):
    if i == 5:
        break  # exits the loop
    if i % 2 == 0:
        continue  # skips even numbers
    print(i)

# Lists (Mutable, ordered)
# Can be changed (add/remove/modify items)
# Create a list
fruits = ["apple", "banana", "cherry"]

# Access
print(fruits[0])  # Output: apple

# Modify
fruits[1] = "blueberry"

# Add
fruits.append("orange")

# Remove
fruits.remove("apple")

print(fruits)  # ['blueberry', 'cherry', 'orange']

# Tuples (Immutable, ordered)
# Cannot be changed after creation
# Create a tuple
coordinates = (10, 20)

# Access
print(coordinates[0])  # Output: 10

# Tuple unpacking
x, y = coordinates
print(x, y)  # Output: 10 20

# Trying to modify a tuple will raise an error
# coordinates[0] = 15  ❌ TypeError

# Dictionaries (Key-value pairs, unordered)
# Keys must be unique and immutable

# Create a dictionary
person = {
    "name": "Alice",
    "age": 25,
    "city": "New York"
}

# Access
print(person["name"])  # Output: Alice

# Modify
person["age"] = 26

# Add
person["job"] = "Engineer"

# Remove
del person["city"]

# Loop through
for key, value in person.items():
    print(f"{key} -> {value}")

# Output:
# name -> Alice
# age -> 26
# job -> Engineer

# Set and Frozen Set
# Create a set of fruits
fruits = {"apple", "banana", "cherry", "apple"}

print(fruits)  # Output: {'apple', 'banana', 'cherry'} (no duplicates)

# Add a fruit
fruits.add("orange")

# Remove a fruit
fruits.remove("banana")

# Check if an item exists
print("cherry" in fruits)  # True

# Final set
print(fruits)  # {'apple', 'cherry', 'orange'}

# Frozen Set
# Create a frozenset of colors
colors = frozenset(["red", "green", "blue", "red"])

print(colors)  # Output: frozenset({'green', 'blue', 'red'})

# Can't add or remove
# colors.add("yellow")  ❌ Error
# colors.remove("green") ❌ Error

# You can still do set-like operations
primary = frozenset(["red", "blue", "yellow"])
print(colors & primary)  # frozenset({'red', 'blue'})



