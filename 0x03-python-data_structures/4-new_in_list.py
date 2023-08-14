#!/usr/bin/python3
# Replaces_element

def new_in_list(my_list, idx, element):
    new_list = [x for x in my_list]
    if 0 <= idx < len(new_list):
        new_list[idx] = element
        return new_list
