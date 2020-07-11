from tkinter import *

root = Tk()
root.title('Calculator')
root.geometry('300x400+400+150')
root.maxsize(300,400)
root.minsize(300,400)


Count_Dis = Entry(root,width = 45, borderwidth = 5)
Count_Dis.grid(row = 0, column = 0, columnspan = 3, padx = 10, pady = 10)


Btn_1 = Button(root, text = "1", padx = 30, pady = 15)
Btn_2 = Button(root, text = "2", padx = 30, pady = 15)
Btn_3 = Button(root, text = "3", padx = 30, pady = 15)
Btn_4 = Button(root, text = "4", padx = 30, pady = 15)
Btn_5 = Button(root, text = "5", padx = 30, pady = 15)
Btn_6 = Button(root, text = "6", padx = 30, pady = 15)
Btn_7 = Button(root, text = "7", padx = 30, pady = 15)
Btn_8 = Button(root, text = "8", padx = 30, pady = 15)
Btn_9 = Button(root, text = "9", padx = 30, pady = 15)
Btn_0 = Button(root, text = "0", padx = 30, pady = 15)

Btn_sub = Button(root, text = "-", padx = 30, pady = 15)
Btn_clr = Button(root, text = "C", padx = 30, pady = 15)
Btn_add = Button(root, text = "+", padx = 30, pady = 15)
Btn_equal = Button(root, text = "=", padx = 80, pady = 15)


Btn_7.grid(row = 1, column = 0)
Btn_8.grid(row = 1, column = 1)
Btn_9.grid(row = 1, column = 2)

Btn_4.grid(row = 2, column = 0)
Btn_5.grid(row = 2, column = 1)
Btn_6.grid(row = 2, column = 2)

Btn_1.grid(row = 3, column = 0)
Btn_2.grid(row = 3, column = 1)
Btn_3.grid(row = 3, column = 2)

Btn_0.grid(row = 4, column = 0)
Btn_clr.grid(row = 4, column = 1)
Btn_sub.grid(row = 4, column = 2)

Btn_equal.grid(row = 6, column = 0, columnspan = 2)
Btn_add.grid(row = 6, column = 2)





root.mainloop()