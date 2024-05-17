from bisect import bisect_left

def fibMonaccianSearch(arr, x, n): 

	fibMMm2 = 0 
	fibMMm1 = 1 
	fibM = fibMMm2 + fibMMm1 

	while (fibM < n): 
		fibMMm2 = fibMMm1 
		fibMMm1 = fibM 
		fibM = fibMMm2 + fibMMm1 

	offset = -1

	while (fibM > 1): 

		i = min(offset+fibMMm2, n-1) 

 
		if (arr[i] < x): 
			fibM = fibMMm1 
			fibMMm1 = fibMMm2 
			fibMMm2 = fibM - fibMMm1 
			offset = i 


		elif (arr[i] > x): 
			fibM = fibMMm2 
			fibMMm1 = fibMMm1 - fibMMm2 
			fibMMm2 = fibM - fibMMm1 

		else: 
			return i 

	if(fibMMm1 and arr[n-1] == x): 
		return n-1

	return -1


arr = list(map(int,input("Enter the array elements: ").split())) 
n = len(arr) 
x = int(input("enter the number to search: "))
ind = fibMonaccianSearch(arr, x, n) 
if ind>=0: 
    print("Found at index:",ind) 
else: 
    print(x,"isn't present in the array"); 
