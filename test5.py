from datetime import datetime
from tkinter import *
from tkinter import filedialog
import os

root = Tk()
root.state('zoomed')
lst = list()
label_lst = list()


def save(event):
    lst.append(entryWidget.get().capitalize())
    entryWidget.delete(0, END)


def display():
    label_lst.extend([Label(root, text=item, font=25) for item in sorted(lst)])
    for item in label_lst:
        item.pack()
    write_to_file(lst, 'Game.txt')


def write_to_file(input_list, file_name):
    with open(file_name, 'a') as file:
        file.write('{}'.format(datetime.now()))
        file.write('\n')
        for word in input_list:
            file.write(word)
            file.write('\n')


def reset():
    for item in label_lst:
        item.destroy()
    lst.clear()
    label_lst.clear()


def open_history(file_name):
    os.system(file_name)


title = Label(root, text="GAME", font=45)
title.pack(pady=(250, 10))

entryWidget = Entry(root, font=30)
entryWidget.bind('<Return>', save)
entryWidget.pack(ipadx=100, ipady=10, pady=(0, 10))

displayButton = Button(root, text="DISPLAY", command=display)
displayButton.pack(ipadx=20, ipady=10, pady=(0, 20))

resetButton = Button(root, text="RESET", command=reset)
resetButton.pack(ipadx=20, ipady=10, pady=(0, 20))

historyButton = Button(root, text="HISTORY", command=lambda: open_history("Game.txt"))
historyButton.pack(ipadx=20, ipady=10, pady=(0, 20))

root.mainloop()
