import tkinter
window = tkinter.Tk()
window.minsize(width=400,height=400)

space_text = ""
def write_equation(x):
    global space_text
    space_text = space_text + str(x)
    space.delete("1.0","end")
    space.insert("1.0",space_text)

def click_button(y):
    write_equation(y)

def calculate():
    pass

space = tkinter.Text(height=2,width=20)
space.grid(row=1,column=1,columnspan=4)

equal_button = tkinter.Button(text="=",command=lambda: calculate)
equal_button.grid(row=8,column=4)

plus_button = tkinter.Button(text="+",command=lambda: click_button("+"))
plus_button.grid(row=7,column=4)

minus_button = tkinter.Button(text="-",command=lambda: click_button("-"))
minus_button.grid(row=6,column=4)

multiply_button = tkinter.Button(text="x",command=lambda: click_button("*"))
multiply_button.grid(row=5,column=4)

division_button = tkinter.Button(text="÷",command=lambda: click_button("/"))
division_button.grid(row=4,column=4)


window.mainloop()