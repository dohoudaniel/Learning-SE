#!/usr/bin/python3
def list_division(my_list_1, my_list_2, list_length):
    
    # Initializing an empty variable and an empty list
    dan = 0
    final_list = []
    
    while dan < list_length:
        dan_list = 0
        try:
            dan_list = float(my_list_1[dan] // my_list_2[dan])
        
        # This block runs when a division by zero occurs.
        except ZeroDivisionError:
            print("division by 0")
        
        # This block runs when a division occurs with a wrong type 
        except TypeError:
            print("wrong type")
        
        # This block runs when either the first or second list is short of the the other list
        except IndexError:
            print("out of range")
        
        finally:
            final_list.append(dan_list)
            dan = dan + 1
    
    return final_list

