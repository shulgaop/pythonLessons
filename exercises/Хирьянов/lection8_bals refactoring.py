import tkinter as tk
from random import randint
WIDTH = 300
HEIGHT = 200

class Ball:
    def __init__(self):
        self.R = randint(20, 50)
        self.x = randint(self.R, WIDTH - self.R)
        self.y = randint(self.R, HEIGHT - self.R)
        self.dx, self.dy = (+3, +3)
        self.ball_id = canvas.create_oval(self.x - self.R,
                                     self.y - self.R,
                                     self.x + self.R,
                                     self.y + self.R,
                                     fill='green')
        tick()
        pass

    def move(self):
        global x, y, dx, dy
        self.x += self.dx
        self.y += self.dy
        if self.x + self.R > WIDTH or self.x - self.R <= 0:
            self.dx = -self.dx
        if self.y + self.R > HEIGHT or self.x - self.R <= 0:
            self.dy = -self.dy

    def show(self):
        canvas.move(self.ball_id, self.dx, self.dy)
        root.after(50, tick)



def canvas_click_handler(event):
    print('HI x = ', event.x, 'y=', event.y)

def tick():
    root.after(50, tick)

def main():
    global root, canvas
    global ball_id, x, y, dx, dy, R # TODO: сделать рефакторинг

    root = tk.Tk()
    root.geometry(str(WIDTH) + "x" + str(HEIGHT))
    canvas = tk.Canvas(root)
    canvas.pack(anchor="nw", fill=tk.BOTH)
    canvas.bind('<Button-1>', canvas_click_handler)

    tick()
    root.mainloop()
if __name__ == "__main__":

    main()



