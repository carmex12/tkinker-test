from tkinter import *
import random
colors = ['red','yellow','blue','green']

size = 30

def click():
    global size
    size += 30
    text.config(font = ("Arial",size,"bold"),fg=random.choice(colors))

window = Tk()
window.title("Hello World!")
window.config(background="grey")

text = Label(window,text='67',font=("Arial",30,"bold"),fg = 'red',bg = 'grey')
text.pack()

button = Button(window,text="Click me")
button.config(command=click)
button.pack()

window.mainloop()