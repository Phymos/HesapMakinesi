import tkinter
window = tkinter.Tk()
window.minsize(width=400,height=400)

result = 0
space_text = ""
def write_equation(x):
    global space_text
    space_text = space_text + str(x)
    space.delete("1.0","end")
    space.insert("1.0",space_text)

def clear():
    global space_text,result,space
    result = 0
    space_text = ""
    space.delete("1.0","end")

def clear_entry():
    global result,space_text,space
    space_text = str(result)
    space.delete("1.0", "end")
    space.insert("1.0", space_text)

def calculate():
    global space_text,result
    result = eval(space.get("1.0","end"))
    space.delete("1.0","end")
    space.insert("1.0",result)
    space_text = str(eval(space.get("1.0","end")))

def delete():
    global space,space_text
    space_text = space_text[:-1]
    space.delete("1.0","end")
    space.insert("1.0",space_text)

def inverse():
    global space_text,space,result
    result = 1/result
    space_text = str(result)
    space.delete("1.0", "end")
    space.insert("1.0", space_text)

space = tkinter.Text(height=2,width=20)
space.grid(row=1,column=1,columnspan=4)

equal_button = tkinter.Button(text="=",command=calculate)
equal_button.grid(row=8,column=4)

plus_button = tkinter.Button(text="+",command=lambda: write_equation("+"))
plus_button.grid(row=7,column=4)

minus_button = tkinter.Button(text="-",command=lambda: write_equation("-"))
minus_button.grid(row=6,column=4)

multiply_button = tkinter.Button(text="x",command=lambda: write_equation("*"))
multiply_button.grid(row=5,column=4)

division_button = tkinter.Button(text="÷",command=lambda: write_equation("/"))
division_button.grid(row=4,column=4)

#numbers
button_1 = tkinter.Button(text="1",command=lambda: write_equation("1"))
button_1.grid(row=7,column=1)

button_2 = tkinter.Button(text="2",command=lambda: write_equation("2"))
button_2.grid(row=7,column=2)

button_3 = tkinter.Button(text="3",command=lambda: write_equation("3"))
button_3.grid(row=7,column=3)

button_4 = tkinter.Button(text="4",command=lambda: write_equation("4"))
button_4.grid(row=6,column=1)

button_5 = tkinter.Button(text="5",command=lambda: write_equation("5"))
button_5.grid(row=6,column=2)

button_6 = tkinter.Button(text="6",command=lambda: write_equation("6"))
button_6.grid(row=6,column=3)

button_7 = tkinter.Button(text="7",command=lambda: write_equation("7"))
button_7.grid(row=5,column=1)

button_8 = tkinter.Button(text="8",command=lambda: write_equation("8"))
button_8.grid(row=5,column=2)

button_9 = tkinter.Button(text="9",command=lambda: write_equation("9"))
button_9.grid(row=5,column=3)

button_0 = tkinter.Button(text="0",command=lambda: write_equation("0"))
button_0.grid(row=8,column=2)


percentage_button = tkinter.Button(text="%",command=lambda: write_equation("%"))
percentage_button.grid(row=3,column=1)

ce_button = tkinter.Button(text="CE",command=clear_entry)
ce_button.grid(row=3,column=2)

clear_button = tkinter.Button(text="C",command=clear)
clear_button.grid(row=3,column=3)

delete_button = tkinter.Button(text="←",font=("Arial",14,"bold"),command=delete)
delete_button.grid(row=3,column=4)

inverse_button = tkinter.Button(text="1/x",command=inverse)
inverse_button.grid(row=4,column=1)

window.mainloop()