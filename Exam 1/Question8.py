# Create a function name is_even that take and integer as a parameter and return true if the number is even otherwise False.
# Demonstrate the usage of the function by checking the number 22 is even or odd

x1 =22

def is_even (x):
    if x%2==0:
        print(f"{x} is an even number")
    elif x%2 !=0:
        print(f"{x} is an odd number")
    else:
        print("enter the integer")

is_even(x1)