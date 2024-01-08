#!/usr/bin/python3

def print_matrix_integer(matrix=[[]]):
    for row in matrix:
        for item in range(len(row)):
            end_space = ' ' if item != len(row) - 1 else ''
            print("{:d}".format(row[item]), end=end_space)
        print()
