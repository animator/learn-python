import math as mt

def ternarySearch(l, r, key, ar):

    if (r >= l):

        mid1 = l + (r - l) //3
        mid2 = r - (r - l) //3

        if (ar[mid1] == key): 
            return mid1
        
        if (ar[mid2] == key): 
            return mid2

        if (key < ar[mid1]): 

            return ternarySearch(l, mid1 - 1, key, ar)
        
        elif (key > ar[mid2]): 

            return ternarySearch(mid2 + 1, r, key, ar)
        
        else: 

            return ternarySearch(mid1 + 1, 
                                 mid2 - 1, key, ar)
        
    return -1

l, r, p = 0, 9, 5


ar = [ 1, 2, 3, 4, 5, 6, 7, 8, 9, 10 ]

l = 0

r = 9

key = 5

p = ternarySearch(l, r, key, ar)

print("Index of", key, "is", p)

key = 50

p = ternarySearch(l, r, key, ar)

print("Index of", key, "is", p)
