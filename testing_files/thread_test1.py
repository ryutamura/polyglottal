import tkinter as tk
from tkinter import ttk
from tkinter import font
import threading


class Application(tk.Frame):
    def __init__(self,master):
        super().__init__(master)
        self.pack()

        self.master.geometry("300x300")
        self.master.title("Tkinter GUI with Event")

        self.font_lbl_big = font.Font( family="Meiryo UI", size=30, weight="bold" )
        self.font_lbl_middle = font.Font( family="Meiryo UI", size=15, weight="bold" )
        self.font_lbl_small = font.Font( family="Meiryo UI", size=12, weight="normal" )

        self.create_widgets()
    #--------------------------------------------
    # Setup Threading Start
    #--------------------------------------------
        self.started = threading.Event() # Event Object
        self.alive = True # Loopの条件
        self._start_thread_main()


    def create_widgets(self):

        # Frame
        self.main_frame = tk.LabelFrame( self.master, text='', font=self.font_lbl_small )
        self.main_frame.place( x=25, y=25 )
        self.main_frame.configure( height=250, width=250 )
        self.main_frame.grid_propagate( 0 )
        self.main_frame.grid_columnconfigure( 0, weight=1 )

        #Start Button
        self.btn_Start = ttk.Button(self.main_frame)
        self.btn_Start.configure(text ='Start')
        self.btn_Start.configure(command = self._start_func)
        self.btn_Start.grid(column = 0, row = 0, padx=10, pady = 10,sticky='NESW' )

        # Stop Button
        self.btn_Stop = ttk.Button(self.main_frame)
        self.btn_Stop.configure(text = 'Stop')
        self.btn_Stop.configure(command = self._stop_func)
        self.btn_Stop.grid(column = 0, row = 1, padx=10, pady = 10,sticky='NESW')

        # Label
        self.lbl_result = ttk.Label(self.main_frame)
        self.lbl_result.configure(text = 'Threading Result Shown Here')
        self.lbl_result.grid(column = 0, row = 2, padx= 30, pady=10,sticky='NESW')

        # Kill Button
        self.btn_Kill = ttk.Button(self.main_frame)
        self.btn_Kill.configure(text = 'Kill Thread')
        self.btn_Kill.configure(command = self._kill_thread)
        self.btn_Kill.grid(column=0, row=3, padx = 10, pady=20,sticky='NESW')

    #--------------------------------------------------
    # Callback Function
    #--------------------------------------------------
    def _start_func(self):
        self.started.set()
        print("Threading Begin")
        print( 'Thread status', self.thread_main )


    def _stop_func(self):
        self.started.clear()
        print("\n Threading Stopped")
        print( 'Thread status', self.thread_main )


    def _start_thread_main(self):
        self.thread_main = threading.Thread(target=self._main_func)
        self.thread_main.start()
        print('main function Threading Started')
        print('Thread status', self.thread_main)

    def _kill_thread(self):
        if self.started.is_set() == False:
            self.started.set()
            self.alive = False
            self.thread_main.join()
        else:
            self._stop_func()
            self.started.set()
            self.alive = False
            #self.thread_main.join()
        print("Thread was killed.")
        print( 'Thread status', self.thread_main )



    def _main_func(self):
        i = 0
        self.started.wait()
        while self.alive:
            if self.started.is_set() == True:
                i = i + 1
                print( "{}\r".format( i ), end="" )
                self.lbl_result.configure( text=i ,font = self.font_lbl_big )

            else:
                self.lbl_result.configure( text= 'Stopped' ,font = self.font_lbl_big)
                self.started.wait()

        pass

def main():
    root = tk.Tk()
    app = Application(master=root)#Inherit
    app.mainloop()

if __name__ == "__main__":
    main()