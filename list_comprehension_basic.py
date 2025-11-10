# list_comprehension_basic.py

# Using a normal for loop
numbers = []
for i in range(5):
    numbers.append(i)
print("Using for loop:", numbers)

# Using list comprehension
numbers_comp = [i for i in range(5)]
print("Using list comprehension:", numbers_comp)
