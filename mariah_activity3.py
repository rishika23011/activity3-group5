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

sorted_array = [5, 7, 8, 12, 23, 29, 32, 34, 40, 62]
target = 29
start = 0
end = len(sorted_array)

result = binary_search(sorted_array, target, start, end)
print(result)

