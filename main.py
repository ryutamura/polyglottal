from tkinter import *
from tkmacosx import Button
from PIL import ImageTk, Image
from presets import preset_funcs
from recorded_files import loop_funcs, record_funcs, play_funcs
# import presets.preset_funcs
# import recorded_files.loop_funcs, recorded_files.record_funcs, recorded_files.play_funcs
import threading
import sys

root = Tk()
root.title('TamuPC-2000')

# Creating a label widget (title)
title = Label(root, text='TamuPC 2000', font='TKHeadingFont 24 bold', fg='red')
title.pack(padx=20, pady=20)
blank = Label(root)
blank.pack()

#Defining images
preset_img = ImageTk.PhotoImage(Image.open('./images/preset.png'))
loop_img = ImageTk.PhotoImage(Image.open('./images/loop.png'))
play_img = ImageTk.PhotoImage(Image.open('./images/play.png'))
stop_img = ImageTk.PhotoImage(Image.open('./images/stop.png'))
rec_img = ImageTk.PhotoImage(Image.open('./images/rec.png'))

#Defining functions for playing presets
thread_event = threading.Event()
def preset1():
    if thread_event.is_set() == False:
        thread_event.set()
        print('Preset1 playing...')
        thread1 = threading.Thread(target=preset_funcs.play_preset1)
        thread1.start()
    elif thread_event.is_set() == True:
        sys.exit()

def preset2():
    # if thread_event.is_set() == False:
    #     thread_event.set()
        print('Preset2 playing...')
        thread2 = threading.Thread(target=preset_funcs.play_preset2)
        thread2.start()
    # elif thread_event.is_set() == True:
    #     sys.exit()

def preset3():
    # if thread_event.is_set() == False:
    #     thread_event.set()
        print('Preset3 playing...')
        thread3 = threading.Thread(target=preset_funcs.play_preset3)
        thread3.start()
    # elif thread_event.is_set() == True:
    #     sys.exit()

def preset4():
    # if thread_event.is_set() == False:
    #     thread_event.set()
        print('Preset4 playing...')
        thread4 = threading.Thread(target=preset_funcs.play_preset4)
        thread4.start()
    # elif thread_event.is_set() == True:
    #     sys.exit()

def preset5():
    # if thread_event.is_set() == False:
    #     thread_event.set()
        print('Preset5 playing...')
        thread5 = threading.Thread(target=preset_funcs.play_preset5)
        thread5.start()
    # elif thread_event.is_set() == True:
    #     sys.exit()


#Functions for playing recorded file
def key_bind_func(event):
    if event.char == 'z':
        print('audio1 is playing...')
        thread6 = threading.Thread(target=play_funcs.play_audio1)
        thread6.start()
    elif event.char == 'x':
        print('audio2 is playing...')
        thread7 = threading.Thread(target=play_funcs.play_audio2)
        thread7.start()
    elif event.char == 'c':
        print('audio3 is playing...')
        thread8 = threading.Thread(target=play_funcs.play_audio3)
        thread8.start()
    elif event.char == 'v':
        print('audio4 is playing...')
        thread9 = threading.Thread(target=play_funcs.play_audio4)
        thread9.start()
    elif event.char == 'b':
        print('audio5 is playing...')
        thread10 = threading.Thread(target=play_funcs.play_audio5)
        thread10.start()
    elif event.char == 'a':
        record_funcs.record1()
    elif event.char == 's':
        record_funcs.record2()
    elif event.char == 'd':
        record_funcs.record3()
    elif event.char == 'f':
        record_funcs.record4()
    elif event.char == 'g':
        record_funcs.record5()
    elif event.char == 'q':
        loop_funcs.loop1()
    elif event.char == 'w':
        loop_funcs.loop2()
    elif event.char == 'e':
        loop_funcs.loop3()
    elif event.char == 'r':
        loop_funcs.loop4()
    elif event.char == 't':
        loop_funcs.loop5()

#functions for recording with gui rec button
def gui_record1():
    record_funcs.record1()

def gui_record2():
    record_funcs.record2()

def gui_record3():
    record_funcs.record3()

def gui_record4():
    record_funcs.record4()

def gui_record5():
    record_funcs.record5()

def gui_play1():
    play_funcs.play_audio1()

def gui_play2():
    play_funcs.play_audio2()

def gui_play3():
    play_funcs.play_audio3()

def gui_play4():
    play_funcs.play_audio4()

def gui_play5():
    play_funcs.play_audio5()






# Creating Frame1
frame1 = LabelFrame(blank, text='Channel 1', padx=5, pady=5)
#Creating Buttons for Frame1
button_1 = Button(frame1, text='Preset', relief=GROOVE, borderwidth=5, padx=30, pady=20, command=preset1)
button_2 = Button(frame1, text='Loop', relief=GROOVE, borderwidth=5, padx=30, pady=20)
button_3 = Button(frame1, text='Rec', relief=GROOVE, borderwidth=5, padx=30, pady=20, command=gui_record1) 
button_4 = Button(frame1, text='Play', relief=GROOVE, borderwidth=5, padx=30, pady=20, command=gui_play1)
#showing frame1
frame1.grid(row=0, column=0, padx=20)
#Packing buttons for frame1
button_1.pack(pady=10)
button_2.pack(pady=10)
button_3.pack(pady=10)
button_4.pack(pady=10)
#Binding buttons for frame1
button_2.bind_all("<Key>", key_bind_func)
button_3.bind_all("<Key>", key_bind_func)
button_4.bind_all("<Key>", key_bind_func)


# Creating Frame2
frame2 = LabelFrame(blank, text='Channel 2', padx=5, pady=5)
#Creating Buttons for Frame2
button_5 = Button(frame2, text='Preset', relief=GROOVE, borderwidth=5, padx=30, pady=20, command=preset2) 
button_6 = Button(frame2, text='Loop', relief=GROOVE, borderwidth=5, padx=30, pady=20)
button_7 = Button(frame2, text='Rec', relief=GROOVE, borderwidth=5, padx=30, pady=20, command=gui_record2)
button_8 = Button(frame2, text='Play', relief=GROOVE, borderwidth=5, padx=30, pady=20, command=gui_play2)
#showing frame2
frame2.grid(row=0, column=1, padx=20)
#showing buttons for frame2
button_5.pack(pady=10)
button_6.pack(pady=10)
button_7.pack(pady=10)
button_8.pack(pady=10)
#Binding buttons for frame2
button_6.bind_all("<Key>", key_bind_func)
button_7.bind_all("<Key>", key_bind_func)
button_8.bind_all("<Key>", key_bind_func)



# Creating Frame3
frame3 = LabelFrame(blank, text='Channel 3', padx=5, pady=5)
#Creating Buttons for Frame3
button_9 = Button(frame3, text='Preset', relief=GROOVE, borderwidth=5, padx=30, pady=20, command=preset3)
button_10 = Button(frame3, text='Loop', relief=GROOVE, borderwidth=5, padx=30, pady=20)
button_11 = Button(frame3, text='Rec', relief=GROOVE, borderwidth=5, padx=30, pady=20, command=gui_record3)
button_12 = Button(frame3, text='Play', relief=GROOVE, borderwidth=5, padx=30, pady=20, command=gui_play3)
#showing frame3
frame3.grid(row=0, column=2, padx=20)
#showing buttons for frame3
button_9.pack(pady=10)
button_10.pack(pady=10)
button_11.pack(pady=10)
button_12.pack(pady=10)
#Binding buttons for frame3
button_10.bind_all("<Key>", key_bind_func)
button_11.bind_all("<Key>", key_bind_func)
button_12.bind_all("<Key>", key_bind_func)

# Creating Frame4
frame4 = LabelFrame(blank, text='Channel 4', padx=5, pady=5)
#Creating Buttons for Frame4
button_13 = Button(frame4, text='Preset', relief=GROOVE, borderwidth=5, padx=30, pady=20, command=preset4)
button_14 = Button(frame4, text='Loop', relief=GROOVE, borderwidth=5, padx=30, pady=20)
button_15 = Button(frame4, text='Rec', relief=GROOVE, borderwidth=5, padx=30, pady=20, command=gui_record4)
button_16 = Button(frame4, text='Play', relief=GROOVE, borderwidth=5, padx=30, pady=20, command=gui_play4)
#showing frame4
frame4.grid(row=0, column=3, padx=20)
#showing buttons for frame4
button_13.pack(pady=10)
button_14.pack(pady=10)
button_15.pack(pady=10)
button_16.pack(pady=10)
#Binding buttons for frame4
button_14.bind_all("<Key>", key_bind_func)
button_15.bind_all("<Key>", key_bind_func)
button_16.bind_all("<Key>", key_bind_func)

# Creating Frame5
frame5 = LabelFrame(blank, text='Channel 5', padx=5, pady=5)
#Creating Buttons for Frame5
button_17 = Button(frame5, text='Preset', relief=GROOVE, borderwidth=5, padx=30, pady=20, command=preset5)
button_18 = Button(frame5, text='Loop', relief=GROOVE, borderwidth=5, padx=30, pady=20)
button_19 = Button(frame5, text='Rec', relief=GROOVE, borderwidth=5, padx=30, pady=20, command=gui_record5)
button_20 = Button(frame5, text='Play', relief=GROOVE, borderwidth=5, padx=30, pady=20, command=gui_play5)
#showing frame5
frame5.grid(row=0, column=4, padx=20)
#showing buttons for frame5
button_17.pack(pady=10)
button_18.pack(pady=10)
button_19.pack(pady=10)
button_20.pack(pady=10)
#Binding buttons for frame4
button_18.bind_all("<Key>", key_bind_func)
button_19.bind_all("<Key>", key_bind_func)
button_20.bind_all("<Key>", key_bind_func)

#Create quit button
button_quit = Button(blank, text='Quit', command=root.quit)
button_quit.grid(row=1, column=0, columnspan=10, pady=10)


# Make a eventloop
root.mainloop()