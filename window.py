from tkinter import *

import time


root = Tk()


def open_window(title, message, color):
    pyr = Tk()
    pyr.geometry('300x300')
    pyr.title(title)
    pyr.configure(background = color)
    lbl = Label(pyr, text=message, bg=color)
    lbl.grid(column=3, row=3)
    pyr.mainloop()
    time.sleep(5)
    pyr.destroy()


#schedule.every(1).minutes.do(open_window("Window","Message","white")) 

open_window("Window","Message","black")

win1 = Tk()
win1.title('???')
win1.eval('tk::PlaceWindow . center')

text1 = Label(win1, text="There are empty files in your Desktop. Want them to be deleted?")
text1.grid(row=1, column=1, padx=10, pady=10)
text1.pack()


root.title("File Manager")

root.eval("tk::PlaceWindow . center")

time.sleep(400)

print("Window has loaded")


#win1.mainloop()
#root.mainloop()

root.destroy()
