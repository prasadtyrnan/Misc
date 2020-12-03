import numpy as np

def max_index(unsorted_list):
    if len(unsorted_list) > 0:
        max_val = unsorted_list[0]
        max_index = 0
        for i in range(1,len(unsorted_list)):
            if unsorted_list[i] > max_val:
                max_val = unsorted_list[i]
                max_index = i
        return max_index
    return -1

def stocks_problem(gain):
    list_1 = []
    list_2 = []
    list_3 = []
    for i in range(len(gain)):
        list_2.append(0)
        list_3.append(0)
        if i == 0:
            list_1.append(1 * (1 + gain[i]))
        else:
            list_1.append(list_1[i-1]*(1 + gain[i]))
    max_seen_price = 0
    for i in range(len(gain)-1,0,-1):
        list_2[i] = max_seen_price - list_1[i]
        if list_1[i] > max_seen_price:
            max_seen_price = list_1[i]
    min_seen_price = np.inf
    for i in range(len(gain)):
        list_3[i] = list_1[i] - min_seen_price
        if list_1[i] < min_seen_price:
            min_seen_price = list_1[i]
    return max_index(list_2), max_index(list_3)

print(stocks_problem([.1, .3, -.4, .2, -.1, 1, -.7]))