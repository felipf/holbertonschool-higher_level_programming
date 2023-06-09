#!/usr/bin/python3
def search_replace(my_list, search, replace):
    newList = my_list.copy()
    for num in range(len(newList)):
        if newList[num] == search:
            newList[num] = replace
    return newList
