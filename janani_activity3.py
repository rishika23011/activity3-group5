"""
phase 3 and 4

"""
import random
import time
from rishika_activity3 import linear
from janani_activity3 import binary_search 


def generated_sorted_data(arr):
    
    if(len(arr)<=1): #if lenght of array is one then its already sorted 
        return arr
    mid=len(arr)//2  #divide the array into two and get the middle elememt
    left_arr=generated_sorted_data(arr[:mid])  #recursion to divide the sub arrays again to be sorted
    right_arr=generated_sorted_data(arr[mid:])
    
    sorted_arr=[]
    i=j=0
    while i <len(left_arr) and j< len(right_arr):
        if left_arr[i]<=right_arr[j]:
            sorted_arr.append(left_arr[i])
            i+=1
        else:
            sorted_arr.append(right_arr[j])
            j+=1
    sorted_arr+=left_arr[i:]
    sorted_arr+=right_arr[j:]
    return sorted_arr
 

def time_counter():
    
    large_data = [55, 22, 89, 34, 67, 90, 15, 72, 39, 44]+[random.randint(1, 100) for _ in range(1000)]
    sorted_data = generated_sorted_data(large_data)

    target = 72
    l_total=0
    b_total=0

    # linear search
    l_start = time.perf_counter() 
    l_result = linear(large_data, target) 
    l_end = time.perf_counter()
    l_total+= (l_end - l_start)
    l_average = l_total *1000000
    
    # binary search
    b_start = time.perf_counter()
    b_result = binary_search(sorted_data, target, 0, len(sorted_data) - 1) 
    b_end = time.perf_counter() 
    b_total += (b_end - b_start)
    b_average = b_total *1000000
    print(f"Linear search target position: {l_result}   time taken:{l_average} seconds")
    print(f"Binary search target position: {b_result}   time taken:{b_average} seconds")

time_counter()