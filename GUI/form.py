import tkinter as tk
from tkinter import ttk 
from csv import DictWriter # to create and add data to csv file
import os # for to check file is empty ot not 

root = tk.Tk() # Create the root (base) window where all widgets go
root.geometry("600x400+300+100") # Fixed window size, geometry("window width x window height + position right + position down")
root.title('My First GUI with Python') # Change the title of window

def label(string): # i create this function for label making
    return ttk.Label(root, text = string)

def TextBox(size, var):
    return ttk.Entry(width = size, textvariable = var)

def Submit(): # function for submit button
    Name = Name_var.get()
    Age = Age_var.get()
    Email = Email_var.get()
    Gender = Gender_var.get()
    text = f"Mr. {Name} Age is {Age} Gender {Gender} with Email {Email}"

    with open('form_file.csv', 'a') as f:
        dict_writer = DictWriter(f, fieldnames = ['Name', 'Age', 'Email', 'Gender'])
        if os.stat('form_file.csv').st_size == 0:
            dict_writer.writeheader()
        
        dict_writer.writerow({
            "Name": Name,
            "Age": Age,
            "Email": Email,
            "Gender": Gender
        })

    textbox1.delete(0, tk.END)
    textbox2.delete(0, tk.END)
    textbox3.delete(0, tk.END)
    lbl6 = label("Successfully Added")
    lbl6.grid(row = 6, column = 1)
    # lbl6.configure(forground = 'Green')
    print (text)

lbl1 = tk.Label(root, text = 'Hey There!') # Create a label on window
# lbl1.pack() # to show on window
lbl1.grid(row = 0, column = 1)

lbl2 = label("Name: ")
lbl2.grid(row = 1, column = 0)

lbl3 = label("Email: ")
lbl3.grid(row = 2, column = 0)

lbl4 = label("Age: ")
lbl4.grid(row = 3, column = 0)

lbl5 = label("Gender: ")
lbl5.grid(row = 4, column = 0)

Name_var = tk.StringVar()
textbox1 = TextBox(22, Name_var)
textbox1.grid(row = 1, column = 1)
textbox1.focus()

Email_var = tk.StringVar()
textbox2 = TextBox(22, Email_var)
textbox2.grid(row = 2, column = 1)

Age_var = tk.StringVar()
textbox3 = TextBox(22, Age_var)
textbox3.grid(row = 3, column = 1)

Gender_var = tk.StringVar()
Values = ['Male','Female', 'Other']
gender = ttk.Combobox(values = Values,textvariable = Gender_var , state = 'readonly')
gender.current(0) # to set default value to 1st
gender.grid(row = 4, column = 1)


btn_submit = ttk.Button(text = 'Submit', command = Submit)
btn_submit.grid(row = 5, column = 1)


root.mainloop() # Pause the window unit user  click the close button
