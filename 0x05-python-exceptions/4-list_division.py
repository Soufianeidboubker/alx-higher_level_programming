#!/usr/bin/python3
def list_division(my_list_1, my_list_2, list_length):
    "Divides two lists element by element."
    nw_list = []
    for s in range(0, list_length):
        try:
            div = my_list_1[s] / my_list_2[s]
        except TypeError:
            print("wrong type")
            div = 0
        except ZeroDivisionError:
            print("division by 0")
            div = 0
        except IndexError:
            print("out of range")
            div = 0
        finally:
            nw_list.append(div)
    return (nw_list)
