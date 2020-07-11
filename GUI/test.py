from tkinter import *
root = Tk()
root.title('GUI Test')
root.geometry('644x434')
root.maxsize(644,434)
root.minsize(644, 434)

frame = Frame(root, bg = "silver")
frame.pack(fill = 'x')

def label(String):
    return Label(root, text = String)

def textBox(Size, Var):
    return Entry(frame, width = Size, textvariable = Var)

def button(String, cmnd):
    return Button(text = String, command = cmnd)

Text_var = StringVar()
txt_Text = textBox(18, Text_var)
txt_Text.pack()





root.mainloop()