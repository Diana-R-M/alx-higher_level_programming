#!/usr/bin/python3
# adds_two_tuples

def add_tuple(tuple_a=(), tuple_b=()):
    x = tuple_a + (0, 0)
    y = tuple_b + (0, 0)


addition = (x[0] + y[0], x[1] + y[1])
return addition
