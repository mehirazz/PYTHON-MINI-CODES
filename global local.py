count = 0  # Global variable

def increase_count():
    global count  # Declare that we are using the global variable
    count += 1
    print("Inside function, count =", count)

increase_count()
print("Outside function, count =", count)
