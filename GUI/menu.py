from tkinter import *

root = Tk()
root.title('Menu')
root.geometry('800x600')


myMenu = Menu(root)
m1 = Menu(myMenu)
m1.add_command(label = 'New File', command = 'myfun')
m1.add_command(label = 'Save', command = 'myfun')
m1.add_command(label = 'Save As', command = 'myfun')
root.config(menu = myMenu)

myMenu.add_cascade(label = 'File',menu = m1)


root.mainloop()