arr = list(map(int, input("Enter the array elements : ").split()))

import math

def jump_search(arr, target):
    n = len(arr)
    arr.sort()  # Ensure array is sorted
    step = int(math.sqrt(n))
    prev = 0

    while arr[min(step, n)-1] < target:
        prev = step
        step += int(math.sqrt(n))
        if prev >= n:
            return -1

    while arr[prev] < target:
        prev += 1
        if prev == min(step, n):
            return -1

    if arr[prev] == target:
        return prev

    return -1

target = int(input("Enter the number to search for: "))

index = jump_search(arr, target)
if index != -1:
    print(f"{target} found at index {index}.")
else:
    print(f"{target} not found in the array.")
