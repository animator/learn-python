#Sets
a={1,2,3,4,5,5,4,6}
print(type(a))
print(a) #sets don't print repitative value

b={} # this will creat empty dictonary
c=set() # this will creat empty sets

print(type(b))
print(type(c))

c.add(5,7,8,9)
c.add(4)#can't add list & dictonary in set but can add tupple
print(c)

print(len(c))

c.remove(5)
print(c)

print(c.pop())
print(c)