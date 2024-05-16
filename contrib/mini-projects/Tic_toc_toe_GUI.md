``` python
#install tkinter before running the program using "pip install tkinter" command

import tkinter as tk
from tkinter import *
from tkinter import ttk

root=Tk()
root.title("Tic-Tac-Toe")

j=0;b1=0;b2=0;b3=0;b4=0;b5=0;b6=0;b7=0;b8=0;b9=0;l=0
nl = ttk.Label(root,text=" ")

def click(num):
    
    global b1,b2,b3,b4,b5,b6,b7,b8,b9,j,l,nl
    i=j%2
    
    if i==0:
        if num==1 and b1==0:
            btn_1.config(text="X")
            b1=1;j+=1
            
        elif num==2 and b2==0:
            btn_2.config(text="X")
            b2=1;j+=1
            
        elif num==3 and b3==0:
            btn_3.config(text="X")
            b3=1;j+=1
            
        elif num==4 and b4==0:
            btn_4.config(text="X")
            b4=1;j+=1
            
        elif num==5 and b5==0:
            btn_5.config(text="X")
            b5=1;j+=1
            
        elif num==6 and b6==0:
            btn_6.config(text="X")
            b6=1;j+=1
            
        elif num==7 and b7==0:
            btn_7.config(text="X")
            b7=1;j+=1
            
        elif num==8 and b8==0:
            btn_8.config(text="X")
            b8=1;j+=1
            
        elif num==9 and b9==0:
            btn_9.config(text="X")
            b9=1;j+=1
            
        if  (b1==b2==b3==1) or (b1==b4==b7==1) or (b2==b5==b8==1) or \
            (b3==b6==b9==1) or (b4==b5==b6==1) or (b7==b8==b9==1) or \
            (b1==b5==b9==1) or (b3==b5==b7==1):
            nl = ttk.Label(root,text='Congratulations',width=15)
            nl.grid(row=5,column=2)
            l=ttk.Label(root,text="X won!",width=10)
            l.grid(row=6,column=2)
        
    elif i==1:
        
        if num==1 and b1==0:
            btn_1.config(text="O")
            b1=2;j+=1
            
        elif num==2 and b2==0:
            btn_2.config(text="O")
            b2=2;j+=1
            
        elif num==3 and b3==0:
            btn_3.config(text="O")
            b3=2;j+=1
            
        elif num==4 and b4==0:
            btn_4.config(text="O")
            b4=2;j+=1
            
        elif num==5 and b5==0:
            btn_5.config(text="O")
            b5=2;j+=1
            
        elif num==6 and b6==0:
            btn_6.config(text="O")
            b6=2;j+=1
            
        elif num==7 and b7==0:
            btn_7.config(text="O")
            b7=2;j+=1
            
        elif num==8 and b8==0:
            btn_8.config(text="O")
            b8=2;j+=1
            
        elif num==9 and b9==0:
            btn_9.config(text="O")
            b9=2;j+=1
            
        if  (b1==b2==b3==2) or (b1==b4==b7==2) or (b2==b5==b8==2) or \
            (b3==b6==b9==2) or (b4==b5==b6==2) or (b7==b8==b9==2) or \
            (b1==b5==b9==2) or (b3==b5==b7==2) or (b3==b5==b7==2):
            nl = ttk.Label(root,text='Congratulations',width=15)
            nl.grid(row=5,column=2)
            l=ttk.Label(root,text="O won!",width=10)
            l.grid(row=6,column=2)
                
def reset():

    global b1,b2,b3,b4,b5,b6,b7,b8,b9,j,nl
    b1=0;b2=0;b3=0;b4=0;b5=0;b6=0;b7=0;b8=0;b9=0;j=0
    btn_1.config(text=" ")
    btn_2.config(text=" ")
    btn_3.config(text=" ")
    btn_4.config(text=" ")
    btn_5.config(text=" ")
    btn_6.config(text=" ")
    btn_7.config(text=" ")
    btn_8.config(text=" ")
    btn_9.config(text=" ")
    l.config(text=" ")
    nl.config(text=" ")

btn_1=ttk.Button(root,text=" ",padding=20,command= lambda: click(1))
btn_1.grid(row=1,column=1)

btn_2=ttk.Button(root,text=" ",padding=20,command= lambda: click(2))
btn_2.grid(row=1,column=2)

btn_3=ttk.Button(root,text=" ",padding=20,command= lambda: click(3))
btn_3.grid(row=1,column=3)

btn_4=ttk.Button(root,text=" ",padding=20,command= lambda: click(4))
btn_4.grid(row=2,column=1)

btn_5=ttk.Button(root,text=" ",padding=20,command= lambda: click(5))
btn_5.grid(row=2,column=2)

btn_6=ttk.Button(root,text=" ",padding=20,command= lambda: click(6))
btn_6.grid(row=2,column=3)

btn_7=ttk.Button(root,text=" ",padding=20,command= lambda: click(7))
btn_7.grid(row=3,column=1)

btn_8=ttk.Button(root,text=" ",padding=20,command= lambda: click(8))
btn_8.grid(row=3,column=2)

btn_9=ttk.Button(root,text=" ",padding=20,command= lambda: click(9))
btn_9.grid(row=3,column=3)

reset_btn=ttk.Button(root,text="Reset",padding=20,command=reset)
reset_btn.grid(row=4,column=2)

root.mainloop()

```


