import random
small_data=[5,6,1,2,3,8,95]
# random.seed(0)
large_data = [55, 22, 89, 34, 67, 90, 15, 72, 39, 44] + [random.randint(1, 100) for _ in range(990)]
size=len(small_data)
def linear(size): 
    
    for j in range(size-1):
        for i in range(size-1):
            if small_data[i]>small_data[i+1]:
                small_data[i],small_data[i+1]=small_data[i+1],small_data[i]

            elif small_data[i]<small_data[i+1]:
                pass
                
            else:
                pass
    return small_data
    
def generate_sorted_data(small_data, size): 
  
    for j in range(size-1):
        for i in range(size-1):
            if small_data[i]>small_data[i+1]:
                small_data[i],small_data[i+1]=small_data[i+1],small_data[i]

            elif small_data[i]<small_data[i+1]:
                pass
                
            else:
                pass
    return small_data

# result1=linear(size)
# result2=generate_sorted_data(small_data, size)
# print(result1)
# print(result2)