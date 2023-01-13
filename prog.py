from tkinter import *

root = Tk()
root.configure(bg='#5caf7f')
root.title("Roosiez Calculator")

e = Entry(root, width=43, borderwidth=5)
e.config(bd=5, bg='#5caf7f', relief='sunken', fg='white')
e.grid(row=0, column=0, columnspan=3, padx=10, pady=10)


def button_add():
    return

# Define buttons


button_1 = Button(root, text="1", padx=40, pady=20, command=button_add)
button_1.config(bd=5, bg='#5caf7f', relief='raised', fg='white')
button_2 = Button(root, text="2", padx=40, pady=20, command=button_add,)
button_2.config(bd=5, bg='#5caf7f', relief='raised', fg='white')
button_3 = Button(root, text="3", padx=40, pady=20, command=button_add,)
button_3.config(bd=5, bg='#5caf7f', relief='raised', fg='white')
button_4 = Button(root, text="4", padx=40, pady=20, command=button_add,)
button_4.config(bd=5, bg='#5caf7f', relief='raised', fg='white')
button_5 = Button(root, text="5", padx=40, pady=20, command=button_add,)
button_5.config(bd=5, bg='#5caf7f', relief='raised', fg='white')
button_6 = Button(root, text="6", padx=40, pady=20, command=button_add,)
button_6.config(bd=5, bg='#5caf7f', relief='raised', fg='white')
button_7 = Button(root, text="7", padx=40, pady=20, command=button_add,)
button_7.config(bd=5, bg='#5caf7f', relief='raised', fg='white')
button_8 = Button(root, text="8", padx=40, pady=20, command=button_add,)
button_8.config(bd=5, bg='#5caf7f', relief='raised', fg='white')
button_9 = Button(root, text="9", padx=40, pady=20, command=button_add,)
button_9.config(bd=5, bg='#5caf7f', relief='raised', fg='white')
button_0 = Button(root, text="0", padx=40, pady=20, command=button_add,)
button_0.config(bd=5, bg='#5caf7f', relief='raised', fg='white')

button_add = Button(root, text="+", padx=39, pady=20, command=button_add,)
button_add.config(bd=5, bg='#5caf7f', relief='raised', fg='white')
button_equal = Button(root, text="=", padx=91, pady=20, command=button_add,)
button_equal.config(bd=5, bg='#5caf7f', relief='raised', fg='white')
button_clear = Button(root, text="Clear", padx=79, pady=20, command=button_add,)
button_clear.config(bd=5, bg='#5caf7f', relief='raised', fg='white')

button_subtract = Button(root, text="-", padx=41, pady=20, command=button_add,)
button_subtract.config(bd=5, bg='#5caf7f', relief='raised', fg='white')
button_multiply = Button(root, text="*", padx=40, pady=20, command=button_add,)
button_multiply.config(bd=5, bg='#5caf7f', relief='raised', fg='white')
button_divide = Button(root, text="/", padx=41, pady=20, command=button_add,)
button_divide.config(bd=5, bg='#5caf7f', relief='raised', fg='white')

# Put the buttons on the screen

button_1.grid(row=3, column=0)
button_2.grid(row=3, column=1)
button_3.grid(row=3, column=2)

button_4.grid(row=2, column=0)
button_5.grid(row=2, column=1)
button_6.grid(row=2, column=2)

button_7.grid(row=1, column=0)
button_8.grid(row=1, column=1)
button_9.grid(row=1, column=2)

button_0.grid(row=4, column=0)
button_clear.grid(row=4, column=1, columnspan=2)
button_add.grid(row=5, column=0)
button_equal.grid(row=5, column=1, columnspan=2)

button_subtract.grid(row=6, column=0)
button_multiply.grid(row=6, column=1)
button_divide.grid(row=6, column=2)

root.mainloop()
