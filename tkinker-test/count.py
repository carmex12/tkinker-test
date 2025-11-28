from tkinter import *

class Counter:
    def __init__(self, label):
        self.num = 0
        self.label = label
    
    def increment(self):
        self.num += 1
        self.label.config(text=self.num)

    def reset(self):
        self.num =0
        self.label.config(text=self.num)

window = Tk()
window.title("Hello World!")
window.config(background="grey")

text = Label(window, text="0", font=("Arial", 30, "bold"), bg='grey')
text.pack()

counter = Counter(text)

button = Button(window, text="Click me", command=counter.increment)
button.pack()

button2 = Button(window, text="Reset", command=counter.reset)
button2.pack()

window.mainloop()