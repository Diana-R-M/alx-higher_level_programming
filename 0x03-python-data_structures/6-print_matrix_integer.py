#!/usr/bin/python3
# print_matrix

def print_matrix_integer(matrix=[[]]):
    for row in matrix:
        for column in row:
            print("{:d}".format(column), end=" ")
            print()
