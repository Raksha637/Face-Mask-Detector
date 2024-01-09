import sys
import os
import tkinter
import tkinter.messagebox
top=tkinter.Tk()

def helloCallBack():
    os.system('python detect_mask_video.py')
    top.destroy()

B=tkinter.Button(top,text="Start",command= helloCallBack)
B.pack()
top.mainloop()

