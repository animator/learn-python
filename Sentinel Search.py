def sentinelSearch(arr, n, key):

	last = arr[n - 1]

	arr[n - 1] = key
	i = 0

	while (arr[i] != key):
		i += 1

	arr[n - 1] = last

	if ((i < n - 1) or (arr[n - 1] == key)):
		print(key, "is present at index", i)
	else:
		print("Element Not found")

arr = list(map(int,input("Enter the array elements: ").split()))
n = len(arr)
key = int(input("enter the number to search: "))

sentinelSearch(arr, n, key)
