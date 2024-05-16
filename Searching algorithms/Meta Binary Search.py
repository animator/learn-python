import math
def bsearch(A, key_to_search):

	n = len(A)
	lg = int(math.log2(n-1)) + 1;

	pos = 0
	for i in range(lg - 1, -1, -1) :
		if (A[pos] == key_to_search):
			return pos


		new_pos = pos | (1 << i)


		if ((new_pos < n) and
			(A[new_pos] <= key_to_search)):
			pos = new_pos

	return (pos if(A[pos] == key_to_search) else -1)

if __name__ == "__main__":

	A = list(map(int,input("Enter the array elements: ").split()))
  key = int(input("enter the number to search: "))
	print( bsearch(A, key))

