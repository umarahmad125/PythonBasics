from tkinter import *
from tkinter import tmsg as msg
root = Tk()
root.title('Untitled - Notepad')
root.geometry('788x644')


# =========== Functions  Start==============

def Cut():
    TextArea.event_generate(('<<Cut>>'))

def Copy():
    TextArea.event_generate(('<<Copy>>'))

def Paste():
    TextArea.event_generate(('<<Paste>>'))

def Quit():
    root.destroy()

# def Help():
    


def Save_File():
    with open('Untitled.txt','a') as nf:
        nf.write(TextArea.get())



# =========== Menu  Start==============

myMenu = Menu(root)

# ========== File Menu ==============
fileMenu = Menu(myMenu, tearoff = 0)
fileMenu.add_command(label = 'New file')
fileMenu.add_command(label = 'Open file')
fileMenu.add_command(label = 'Save file',command = 'Save_File')
fileMenu.add_command(label = 'Save As')
fileMenu.add_command(label = 'Exit', command = Quit)

myMenu.add_cascade(label = 'File', menu = fileMenu)

# ========== Edit Menu ==============
editMenu = Menu(myMenu, tearoff = 0)
editMenu.add_command(label = 'Cut', command = Cut)
editMenu.add_command(label = 'Copy', command = Copy)
editMenu.add_command(label = 'Paste', command = Paste)

myMenu.add_cascade(label = 'Edit', menu = editMenu)

# ========== Help Menu ==============
helpMenu = Menu(myMenu, tearoff = 0)
helpMenu.add_command(label = 'About Us')

myMenu.add_cascade(label = 'Help', menu = helpMenu)

root.config(menu = myMenu)

# =========== Menu  End==============


# Text Area Start

TextArea = Text(root, font = 'lucdia 13')
TextArea.pack(expand = TRUE, fill = BOTH)

# Text Area End

root.mainloop()