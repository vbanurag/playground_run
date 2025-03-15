'''
Given an array of positive integers, the task is to find the maximum possible sum of 
elements such that no two elements are adjacent in the array2. 
This means if you pick an element at index i, you cannot pick elements at indices i-1 or i+1.
'''

def max_sum_no_adjacent(arr):
    n = len(arr)
    
    if n == 0:
        return 0
    if n == 1:
        return arr[0]
    
    prev = arr[0]
    prev2 = 0
    
    for i in range(1, n):
        temp = prev
        prev = max(prev, prev2 + arr[i])
        prev2 = temp
        
    return prev


# test the function
arr = [5, 5, 10, 100, 10, 5]
print(max_sum_no_adjacent(arr)) # 110    
        
arr2 = [3, 2, 7, 10]
print(max_sum_no_adjacent(arr2)) # 13        