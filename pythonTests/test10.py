# Define the function named say_hello
# DEFINE FUNCTION say_hello
#   PRINT "Hello, world!"

def say_hello():
    print("Hello, world!")

# Define the function named add_two_numbers
# DEFINE FUNCTION add_two_numbers(a, b)
#    RETURN a + b

def add_two_numbers(a, b):
    return a + b


# Main part of the script
# CALL say_hello

say_hello()

# SET result TO add_two_numbers(2, 3)

result = add_two_numbers(2, 3)

# PRINT "The sum of 2 and 3 is" + result

print("The sum of 2 and 3 is " + str(result))