#!/usr/bin/python3
# Reverse_integer order

def print_reversed_list_integer(my_list=[]):
    for value in range(len(my_list) - 1, -1, -1):
        print("{:d}".format(my_list[value]))
