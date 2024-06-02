f=open('samp.txt','a')#appending mode
f.write("i am appending")
f.close()

f=open('samp.txt','w')#writing mode
f.write("i am writing")
f.close()
#This will create a new file if file is not created
#f.write with w will remove everything from file