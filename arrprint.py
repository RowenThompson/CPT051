arr = (1, 2, 3)
arr2 = (4, 5, 6, 4, 5, 6, 4, 5, 6, 4, 5, 6.5)
import math

def print_arr(my_arr):
    my_sum = 0
        
    for i in my_arr:
        print(i)
        x = math.floor(i)
        my_sum += x
        print("sum:" + str(my_sum))
    return my_sum
#main

#print("my sum:" + str(print_arr(arr)))
#print("my sum:" + str(print_arr(arr2)))
#calcsum_arr(arr)
print(sum(arr2))
