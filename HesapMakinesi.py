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

#numbers
button_1 = tkinter.Button(text="1",command=lambda: click_button("1"))
button_1.grid(row=7,column=1)

button_2 = tkinter.Button(text="2",command=lambda: click_button("2"))
button_2.grid(row=7,column=2)

button_3 = tkinter.Button(text="3",command=lambda: click_button("3"))
button_3.grid(row=7,column=3)

button_4 = tkinter.Button(text="4",command=lambda: click_button("4"))
button_4.grid(row=6,column=1)

button_5 = tkinter.Button(text="5",command=lambda: click_button("5"))
button_5.grid(row=6,column=2)

button_6 = tkinter.Button(text="6",command=lambda: click_button("6"))
button_6.grid(row=6,column=3)

button_7 = tkinter.Button(text="7",command=lambda: click_button("7"))
button_7.grid(row=5,column=1)

button_8 = tkinter.Button(text="8",command=lambda: click_button("8"))
button_8.grid(row=5,column=2)

button_9 = tkinter.Button(text="9",command=lambda: click_button("9"))
button_9.grid(row=5,column=3)

button_0 = tkinter.Button(text="0",command=lambda: click_button("0"))
button_0.grid(row=8,column=2)

window.mainloop()