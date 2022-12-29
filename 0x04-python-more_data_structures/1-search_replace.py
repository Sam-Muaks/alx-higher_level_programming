#!/usr/bin/python3


def search_replace(my_list, search, replace):
    new_list = my_list[:]
    for i in range(my_list.count(search)):
        j = new_list.index(search)
        new_list[j] = replace
    return new_list
