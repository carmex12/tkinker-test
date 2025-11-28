from tkinter import *

count = 0

def click():
    global count
    count += 1
    text.config(text=count)

window = Tk()
window.title("Hello World!")
window.config(background="grey")

text = Label(window,text=count,font=("Arial",30,"bold"),bg = 'grey')
text.pack()

button = Button(window,text="Click me")
button.config(command=click)
button.pack()

window.mainloop()
