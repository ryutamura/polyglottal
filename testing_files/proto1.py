from ast import get_source_segment
from tkinter import *
from tkmacosx import Button
from PIL import ImageTk, Image
from test_pydub import play_audio
from test_pydub2 import play_audio2
from test_pydub3 import play_preset1
from test7 import record
import threading
import sys
import signal
import os

root = Tk()
root.title('proto1')

# Creating a label widget (title)
title = Label(root, text='Prototype player')
title.pack(padx=20, pady=20)
blank = Label(root)
blank.pack()

#Defining images
preset_img = ImageTk.PhotoImage(Image.open('./images/preset.png'))
loop_img = ImageTk.PhotoImage(Image.open('./images/loop.png'))
play_img = ImageTk.PhotoImage(Image.open('./images/play.png'))
stop_img = ImageTk.PhotoImage(Image.open('./images/stop.png'))
rec_img = ImageTk.PhotoImage(Image.open('./images/rec.png'))

#testing
thread_event = threading.Event()
def play_preset():
    if thread_event.is_set() == False:
        print(thread_event.is_set())
        thread_event.set()
        print(thread_event.is_set())
        print('Preset1 playing...')
        thread1 = threading.Thread(target=play_preset1)
        thread1.start()
    elif thread_event.is_set() == True:
        sys.exit()


        # print(threading.active_count())
        # print(threading.current_thread())
        # print(threading.get_native_id())
        # print(thread_event.is_set())
        # thread_event.clear()
        # print(thread_event.is_set())

        # root.destroy()
        # print(threading.active_count())
        # print(threading.current_thread())
        # print(threading.get_native_id())




#Frame1 functionality
def play(event):
    if event.char == 'z':
        play_audio()
    elif event.char == 'x':
        play_audio2()
    elif event.char == 'c':
        play_audio3()
    elif event.char == 'v':
        play_audio4()
    elif event.char == 'b':
        play_audio5()

# def rec(event):
#     if event.char == 'a':
        
def pressed(event):
    print(f'you have pressed the {event.char} key')
# def press(*args):
#     print('press')
#     global pressed
#     pressed = True
#     root.after(0, startrec)

# def release(*args):
#     print('release')
#     global pressed
#     pressed = False
#     global pid
#     print(pid)
#     os.kill(pid, signal.SIGINT)



def startrec():
    record()
    # if pressed:
        # print('recording..')
        # global pid
        # pid = os.getpid()
        # print(pid)
        # import test5
        # pid = os.getpid()
        # print(pid)


# def startrec():
#     # import test5
#     print('started recording')
#     import test5
    
    
    

# my_label = Label(image=my_img)

# Creating Frame1
frame1 = LabelFrame(blank, text='Channel 1', padx=5, pady=5)
#Creating Buttons for Frame1
button_1 = Button(frame1, text='Preset', relief=GROOVE, borderwidth=5, padx=30, pady=20, command=play_preset)
button_2 = Button(frame1, text='Loop', relief=GROOVE, borderwidth=5, padx=30, pady=20)
button_3 = Button(frame1, text='Stop Rec', relief=GROOVE, borderwidth=5, padx=30, pady=20)
button_4 = Button(frame1, text='Start Rec', relief=GROOVE, borderwidth=5, padx=30, pady=20)
button_5 = Button(frame1, text='Play', relief=GROOVE, borderwidth=5, padx=30, pady=20, background = 'blue', activebackground = 'green')

# button_26 = Button(frame1, text='Pause Preset', relief=GROOVE, borderwidth=5, padx=30, pady=20, command=)
# button_27 = Button(frame1, text='Stop Preset', relief=GROOVE, borderwidth=5, padx=30, pady=20, command=)
#showing frame1
frame1.grid(row=0, column=0, padx=20)
#showing buttons for frame1
button_1.pack(pady=10)
button_2.pack(pady=10)
button_3.pack(pady=10)
button_4.pack(pady=10)
button_5.pack(pady=10)
# button_26.pack(pady=10)
# button_27.pack(pady=10)


button_3.bind("<Key>", pressed)
# pressed = False
# button_5.bind("<Button-1>", play)
# button_5.bind_all("<Key>", play)
# button_4.bind("<Button-1>", press)
# button_4.bind("<ButtonRelease-1>", release)
# button_4.bind_all("<Key>", play)
# button_1.bind_all("<Key>", threading.Thread(target=play).start())


# def hitkey(event):
#     my_label = Label(root, text='You clicked this button' + event.char)
#     my_label.pack()

# myButton = Button(root, text="Click me")
# myButton.bind_all("<Key>", hitkey)
# myButton.pack(pady=20)

# Creating Frame2
frame2 = LabelFrame(blank, text='Channel 2', padx=5, pady=5)
#Creating Buttons for Frame2
button_6 = Button(frame2, text='Preset', relief=GROOVE, borderwidth=5, padx=30, pady=20) 
button_7 = Button(frame2, text='Loop', relief=GROOVE, borderwidth=5, padx=30, pady=20)
button_8 = Button(frame2, text='Stop Rec', relief=GROOVE, borderwidth=5, padx=30, pady=20)
button_9 = Button(frame2, text='Start Rec', relief=GROOVE, borderwidth=5, padx=30, pady=20)
button_10 = Button(frame2, text='Play', relief=GROOVE, borderwidth=5, padx=30, pady=20)
#showing frame2
frame2.grid(row=0, column=1, padx=20)
#showing buttons for frame2
button_6.pack(pady=10)
button_7.pack(pady=10)
button_8.pack(pady=10)
button_9.pack(pady=10)
button_10.pack(pady=10)

button_10.bind_all("<Key>", play)


# Creating Frame3
frame3 = LabelFrame(blank, text='Channel 3', padx=5, pady=5)
#Creating Buttons for Frame3
button_11 = Button(frame3, text='Preset', relief=GROOVE, borderwidth=5, padx=30, pady=20)
button_12 = Button(frame3, text='Loop', relief=GROOVE, borderwidth=5, padx=30, pady=20)
button_13 = Button(frame3, text='Stop Rec', relief=GROOVE, borderwidth=5, padx=30, pady=20)
button_14 = Button(frame3, text='Start Rec', relief=GROOVE, borderwidth=5, padx=30, pady=20)
button_15 = Button(frame3, text='Play', relief=GROOVE, borderwidth=5, padx=30, pady=20)
#showing frame3
frame3.grid(row=0, column=2, padx=20)
#showing buttons for frame3
button_11.pack(pady=10)
button_12.pack(pady=10)
button_13.pack(pady=10)
button_14.pack(pady=10)
button_15.pack(pady=10)

# Creating Frame4
frame4 = LabelFrame(blank, text='Channel 4', padx=5, pady=5)
#Creating Buttons for Frame4
button_16 = Button(frame4, text='Preset', relief=GROOVE, borderwidth=5, padx=30, pady=20)
button_17 = Button(frame4, text='Loop', relief=GROOVE, borderwidth=5, padx=30, pady=20)
button_18 = Button(frame4, text='Stop Rec', relief=GROOVE, borderwidth=5, padx=30, pady=20)
button_19 = Button(frame4, text='Start Rec', relief=GROOVE, borderwidth=5, padx=30, pady=20)
button_20 = Button(frame4, text='Play', relief=GROOVE, borderwidth=5, padx=30, pady=20)
#showing frame4
frame4.grid(row=0, column=3, padx=20)
#showing buttons for frame4
button_16.pack(pady=10)
button_17.pack(pady=10)
button_18.pack(pady=10)
button_19.pack(pady=10)
button_20.pack(pady=10)

# Creating Frame5
frame5 = LabelFrame(blank, text='Channel 5', padx=5, pady=5)
#Creating Buttons for Frame5
button_21 = Button(frame5, text='Preset', relief=GROOVE, borderwidth=5, padx=30, pady=20)
button_22 = Button(frame5, text='Loop', relief=GROOVE, borderwidth=5, padx=30, pady=20)
button_23 = Button(frame5, text='Stop Rec', relief=GROOVE, borderwidth=5, padx=30, pady=20)
button_24 = Button(frame5, text='Start Rec', relief=GROOVE, borderwidth=5, padx=30, pady=20)
button_25 = Button(frame5, text='Play', relief=GROOVE, borderwidth=5, padx=30, pady=20)
#showing frame5
frame5.grid(row=0, column=4, padx=20)
#showing buttons for frame5
button_21.pack(pady=10)
button_22.pack(pady=10)
button_23.pack(pady=10)
button_24.pack(pady=10)
button_25.pack(pady=10)

#Create quit button
button_quit = Button(blank, text='Quit', command=root.quit)
button_quit.grid(row=1, column=0, columnspan=10, pady=10)

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

# myLabel1 = Label(root, text='This is a prototype', borderwidth=1, relief=GROOVE)
# myLabel2= Label(root, text='My name is Ryu Tamura', borderwidth=1, relief=GROOVE)
# myLabel3= Label(root, text='wuzz up', borderwidth=1, relief=GROOVE)
# myLabel4= Label(root, text='yoyoyo', borderwidth=1, relief=GROOVE)
# myLabel5= Label(root)

# myLabel1.grid(row=0, column=0, columnspan=3, padx=10, pady=30)
# myLabel5.grid(row=1, column=0, columnspan=3, padx=10, pady=10)
# myLabel2.grid(row=2, column=0, padx=10, pady=10)
# myLabel3.grid(row=2, column=1, padx=10, pady=10)
# myLabel4.grid(row=2, column=2, padx=10, pady=10)

# button_1 = Button(root, text=' ')


# frame1 = LabelFrame(root, text='This is my Frame...', padx=5, pady=5, relief=GROOVE, borderwidth=3)
# b = Button(frame1, text="Don't Click here")
# b.pack()

# frame2 = LabelFrame(master=root, text='2nd frame', padx=5, pady=5)
# label_b = Label(master=frame2, text='I am in 2nd frame')
# label_b.pack()

# frame1.grid(row=0, column=0, padx=10, pady=10)
# frame2.grid(row=0, column=1, padx=10, pady=10)







# Make a eventloop
root.mainloop()