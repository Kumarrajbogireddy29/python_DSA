def second_largest(arr):
    arr = list(set(arr))
    arr.sort()
    if len(arr) <2:
        return None 
    return arr[-2]

arr=[34,56,8989,56,34,454,809,672]
print("second largest elemnet in array is ",second_largest(arr))