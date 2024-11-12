def binary_search(sorted_array, target, start, end):
  
    if start > end:
        return None
    else:
        mid = (start + end) // 2
        if target == sorted_array[mid]:
            return mid
        elif target > sorted_array[mid]:
            return binary_search(sorted_array, target, mid + 1, end) 
        else:
            return binary_search(sorted_array, target, start, mid-1)
        


def generated_sorted_data1(arr):
   
    if(len(arr)<=1): 
        return arr
    mid=len(arr)//2  
    left_arr=generated_sorted_data1(arr[:mid])  
    right_arr=generated_sorted_data1(arr[mid:])
    
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