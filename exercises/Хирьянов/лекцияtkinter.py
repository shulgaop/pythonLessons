
from tkinter import *
def handler1(event):
    print('Hi x=', event.x, 'y=', event.y)


def handler2(event):
    exit()


# init инициализация 
root = Tk()
hello_label = Label (root, text = 'Hi', font = 'Times 80')
hello_label.pack()
#widjet:
#widjet .bind(event, handler)
hello_label.bind('<Button-1>', handler1)
hello_label.bind('<Button-3>', handler2)

# main cicle
root.mainloop()

