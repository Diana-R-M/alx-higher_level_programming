#!/usr/bin/python3
# Replace_Element

def replace_in_list(my_list, idx, element):
    if 0 <= idx < len(my_list):
        my_list[idx] = element
        return my_list
