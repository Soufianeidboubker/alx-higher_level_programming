#!/usr/bin/python3
def weight_average(my_list=[]):
    if not my_list:
        return 0

    sum = 0
    weight = 0

    for score in my_list:
        sum += score[0] * score[1]
        weight += score[1]

    return (sum / weight)
