# Defualt parameter ValueError
# 1. create a python function name print_message that parameter message and parameter repeat_count, where repeat_count has default value of 1.
# the function should print the message the number of
# call the function wuth user provided value or using defualt ValueError


repeat_count=5
message = "Hello I am from Afghanistan"

def print_massage(m,r):
    for x in range(r):
        if r > 1:
            print(m)
        else:
            print("Hello is repeat one time only")

print_massage(message,repeat_count)