a=open('samp.txt','r')# by default mode is in read
game_code=a.read()
print(game_code)
a.close()

'''game_code=a.read(5)#read 5 character
print(game_code)
game_code=a.readline()#read 1 line 
print(game_code)'''

if 'writing' in game_code :
    print("It is Present")
else:
    print("It is not Present")

