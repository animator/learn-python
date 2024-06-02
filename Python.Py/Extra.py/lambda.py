#lambda function

square=lambda z:z*z
print(square(2))

#lambda function takes another function
high_order=lambda x,y:x*y(x)

#The inner lambda function is defined when calling the high_order
print( high_order(2,lambda x:x*x))

#lambda function with filter fuction
###filter -> map with a condition is called filter fuction
#using lambda inside filter function
mylist=[2,3,4,5,6,7,8]
print(mylist)


