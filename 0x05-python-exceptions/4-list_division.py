#!/usr/bin/python3


def list_division(my_list_1, my_list_2, list_length):
    """Divides two lists element by element.

    Args:
        my_list_1 (list): The first list.
        my_list_2 (list): The second list.
        list_length (int): The number of elements to divide.

    Returns:
        A new list of length list_length containing all the divisions.
    """
    new_list = []
    div_result = 0
    for i in range(0, list_length):
        try:
            div_result = my_list_1[i] / my_list_2[i]
        except TypeError:
            div_result = 0
            print("wrong type")
        except ZeroDivisionError:
            div_result = 0
            print("division by 0")
        except IndexError:
            div_result = 0
            print("out of range")
        finally:
            new_list.append(div_result)
    return (new_list)
