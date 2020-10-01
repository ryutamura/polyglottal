from tkinter import *
from tkmacosx import Button
from PIL import ImageTk, Image

root = Tk()
root.title('mfDOOM')

# Creating a label widget
# myLabel1 = Label(root, text='Hello World')
# myLabel2= Label(root, text='My name is Ryu Tamura')
# myLabel3= Label(root, text='wuzz up')
# Shoving it onto the screen

# myLabel1.grid(row=0, column=0)
# myLabel2.grid(row=1, column=5)
# myLabel3.grid(row=2, column=2)

# def my_click():
#     myLabel = Label(root, text='Look! I clicked a Button!')
#     myLabel.pack()

# myButton = Button(root, text='Click Me!', command=my_click, fg='#496920', bg='#f8c55e', borderless=1, width=100, height=50)
# myButton.pack()

# my_img = ImageTk.PhotoImage(Image.open('react-removebg-preview.png'))
# my_label = Label(image=my_img)
# my_label.pack()




frame1 = LabelFrame(root, text='This is my Frame...', padx=5, pady=5, relief=GROOVE, borderwidth=3)
b = Button(frame1, text="Don't Click here")
b.pack()

frame2 = LabelFrame(master=root, text='2nd frame', padx=5, pady=5)
label_b = Label(master=frame2, text='I am in 2nd frame')
label_b.pack()

frame1.grid(row=0, column=0, padx=10, pady=10)
frame2.grid(row=0, column=1, padx=10, pady=10)

# Make a eventloop
root.mainloop()