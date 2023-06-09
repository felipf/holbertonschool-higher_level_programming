#!/usr/bin/python3
def search_replace(my_list, search, replace):
    newList = []
    for num in my_list:
        if num == search:
            newList.append(replace)
        else:
            newlist.append(num)
    return newList
