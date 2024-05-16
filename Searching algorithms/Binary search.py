def binarySearch(arr, low, high, x):

    if high >= low:

        mid = low + (high - low) // 2

        if arr[mid] == x:
            return mid

        elif arr[mid] > x:
            return binarySearch(arr, low, mid-1, x)

        else:
            return binarySearch(arr, mid + 1, high, x)

    else:
        return -1


if __name__ == '__main__':
    arr = list(map(int,input("Enter the array elements: ").split()))
    x = int(input("enter the number to search: "))
    
    # Function call
    result = binarySearch(arr, 0, len(arr)-1, x)
    
    if result != -1:
        print("Element is present at index", result)
    else:
        print("Element is not present in array")
