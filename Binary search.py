
def binary_search(arr, target):
    low = 0
    high = len(arr) - 1

    while low <= high:
        mid = (low + high) // 2
        mid_val = arr[mid]

        if mid_val == target:
            return mid
        elif mid_val < target:
            low = mid + 1
        else:
            high = mid - 1

    return -1

def main():
    arr = list(map(int, input("Enter the array elements: ").split()))
    arr.sort()
    target = int(input("Enter the number to search for: "))

    index = binary_search(arr, target)
    if index != -1:
        print(f"{target} found at index {index}.")
    else:
        print(f"{target} not found.")

if __name__ == "__main__":
    main()
