#!/usr/bin/python3
def no_c(my_string):
    result_string = ""
    for char in my_string:
        result_string += char if char.lower() not in {'c', 'C'} else ""
    return result_string
