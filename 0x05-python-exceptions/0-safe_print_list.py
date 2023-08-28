#!/usr/bin/python3

def safe_print_list(my_list=[], x=0):
    increments = 0
    for p in range(x):
        try:
            print(f"{my_list[p]}", end="")
            increments += 1
        except IndexError:
            break
    print()
    return(increments)
