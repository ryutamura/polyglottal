from tkinter import *

def press(*args):
    print('press')
    global pressed
    pressed = True
    master.after(0, loop)

def release(*args):
    print('release')
    global pressed
    pressed = False

def loop():
    if pressed:
        print('loop')
        # Infinite loop without delay is bad idea.
        master.after(250, loop)

master = Tk()
pressed = False

b = Button(master, text="OK")
b.bind("<Button-1>", press)
b.bind("<ButtonRelease-1>", release)
b.pack()
mainloop()