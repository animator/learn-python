from tkinter import *
import random

W,H=600,400
B=20

class Snake(Tk) :
    def __init__(self):
        super().__init__()
        self.title("Snake Game")
        self.geometry(f"{W}x{H}")
        self.canvas =Canvas(self,bg="black")
        self.canvas.pack(fill="both",expand=True)
        self.Points=0
        self.snake = [(100, 100), (80, 100), (60, 100)]
        self.direction ="Right"
        self.food=self.create_food()

        self.bind("<KeyPress>", self.key_press)
        self.update_snake()

    
    def create_food(self):
    
        
        x = random.randint(0, (W - B) // B) * B
        y = random.randint(0, (H - B) // B) * B
        
        
        
          
        self.food=self.canvas.create_oval(x, y, x + B, y + B, fill="white")
        return x,y
       

    
    def move_snake(self):
        x,y = self.snake[0]
        if self.direction == "Right":
            x+=B
        elif self.direction == "Left" :
            x-=B
        elif self.direction == "Up":
            y-=B
        elif self.direction == "Down":
            y+=B
        self.snake= [(x,y)] + self.snake[:-1]
        
        if (x, y) == self.food  :
            
            self.canvas.delete(self.food)  
            self.Points+=1
            self.food = self.create_food() 
        
            
        
        
    
    def draw_snake(self):
        for x,y in self.snake :
            self.canvas.create_rectangle(x,y,x+B,y+B,fill="green")
        
    def collision(self):
        x, y = self.snake[0]
        
    
        if x < 0 or x >= W or y < 0 or y >= H:
            return True

        
        for segment in self.snake[1:]:
            
            if (x, y) == segment:
                return True

        return False

    
    def key_press(self,event):
        key=event.keysym
        if key == "Right" and self.direction != "Left":
            self.direction="Right"
        elif key=="Left" and self.direction !="Right":
            self.direction ="Left"
        elif key =="Up" and self.direction!="Down":
            self.direction = "Up"
        elif key =="Down" and self.direction!="Up":
            self.direction = "Down"
               
    def update_snake(self):
        self.draw_snake()
        self.move_snake()
        if self.collision():
            self.gameover()
            return 
        self.after(150,self.update_snake)
    def gameover(self):
        self.canvas.create_text(W/2,H/2,text=f"Game Over!  Won {self.Points}",fill="white",font=("Arial",24))
        

        





    





if __name__ == "__main__":
    game=Snake()
    game.mainloop()
