#!/usr/bin/python3
# Removes_c_and_C

def no_c(my_string):
    new_string = [char for char in my_string if char != 'c' and char != 'C']
    return "".join(new_string)
