#!/usr/bin/python3
def divisible_by_2(my_list=[]):
    boolist = my_list[:]
    for count, num in enumerate(my_list):
        is_divisible_by_2 = (num % 2 == 0)
        if is_divisible_by_2:
            boolist[count] = True
        else:
            boolist[count] = False
    return boolist
