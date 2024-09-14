#!/usr/bin/python3
def search_replace(my_list, search, replace):
    if not my_list:
        return my_list
    
    dan = search
    return [dan if dan != search else replace for dan in my_list]
    # The code below returns a var 'dan' id dan != search
    # but then 'dan' is equal to 'search' so it will return 'replace'
    # in the place of 'dan' in 'my_list'. 
    
    
    """
    for dan in range(len(my_list)):
        if my_list[dan] == search:
            my_list[dan] = replace
            return my_list
    """

