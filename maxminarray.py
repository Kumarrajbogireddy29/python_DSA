def findMaxMin(arr):
    # Initialize both with the first element
    max_ele = arr[0]
    min_ele = arr[0]

    # Traverse the array
    for num in arr:
        if num > max_ele:
            max_ele = num
        elif num < min_ele:
            min_ele = num

    return max_ele, min_ele


# Driver code
n = int(input("Enter size of array: "))
arr = list(map(int, input("Enter array elements: ").split()))

max_val, min_val = findMaxMin(arr)

print("Maximum element:", max_val)
print("Minimum element:", min_val)
