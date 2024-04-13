import os

import shutil

from datetime import datetime

import random

import tkinter as tk 
#from tkinter import *

current_time = datetime.now()

print("----Current Time-----")
print(current_time)

current_dir = os.getcwd()

print("----Current Directory-----")
print(current_dir)

changed_dir = os.chdir("/Users/timtudosa/Desktop/")

print("----Changed Directory-----")
print(changed_dir)

data = os.listdir()

print("----Data-----")
print(data)

files = []

folder_creation_date = current_time.strftime('%m/%d/%Y')

new_directory_path = "/Users/timtudosa/Desktop/Folder_" + str(random.randint(1,6000))

non_files = []

number_of_files = 0

#get all the folders in desktop

for item in data:
    if "." in item[-4:]:
        number_of_files += 1
        files.append(item)
    else:
        non_files.append(item)

def show_file_window(title):
    pyr = tk.Tk()
    pyr.geometry("300x300")
    pyr.title(title)
    var = tk.StringVar()
    text_box = tk.Label(pyr,textvariable="There are files in the Desktop. Do you want them to be moved to a folder?",fg="black")
    text_box.pack()
    var.set("There are files in the Desktop. Do you want them to be moved to a folder?")
    #text_box.grid(column=1,row=1)
    yes_button = tk.Button(pyr,text="YES")
    no_button = tk.Button(pyr,text="NO")
    #yes_button.pack()
    #no_button.pack()
    pyr.mainloop()


try:
    print("----Number of Files----\n"+str(number_of_files))
    if number_of_files > 0:
        show_file_window("Files in Desktop")
        os.mkdir(new_directory_path)
except OSError:
    print ("Creation of the directory %s failed" % new_directory_path)
else:
    print ("Successfully created the directory %s " % new_directory_path)

print("Changed dir: " + "" + str(changed_dir))

print("New Directory Path:" + "" + new_directory_path)


for file in files:
   shutil.move(os.getcwd() + "/" + file,new_directory_path)

print("---Current Working Directory----")

print(os.getcwd())

print("---New Directory Path----")

print(new_directory_path)



print("Directories" + str(os.listdir()))

#print(os.listdir("Users/timtudosa/Desktop/"))

# if len(os.listdir("C:/Users/timtudosa/Desktop/Folder_5843")) :
#     print("There are no files in the directory")
# else:
#    print("There are files in this directory") 