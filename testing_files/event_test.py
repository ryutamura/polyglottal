from tkinter import *

root = Tk()
root.geometry('400x400')

def hitkey(event):
    if event.char == 'a':
        my_label = Label(root, text='You clicked this button' + event.char)
        my_label.pack()


myButton = Button(root, text="Click me")
myButton.bind_all("<Key>", hitkey)
myButton.pack(pady=20)

root.mainloop()