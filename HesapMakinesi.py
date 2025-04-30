import tkinter as tk
root = tk.Tk()
root.minsize(width=400, height=400)

result = 0
space_text = ""
memory = 0
memory_list = []

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

def square():
    global space_text,space,result
    result = result ** 2
    space_text = str(result)
    space.delete("1.0","end")
    space.insert("1.0",space_text)

def square_root():
    global space,space_text,result
    result = result ** 0.5
    space_text = str(result)
    space.delete("1.0","end")
    space.insert("1.0",space_text)

def plus_minus():
    global space,space_text,result
    result = -1 * result
    space_text = str(result)
    space.delete("1.0","end")
    space.insert("1.0",space_text)

def memory_store():
    global memory,memory_list,space_text
    memory = float(space_text)
    memory_list.append(memory)
    update_memory_list()

def update_memory_list():
    chosen_memory.set(memory_list[-1] if memory_list else "None")
    memory_option["menu"].delete(0, "end")
    for item in memory_list:
        memory_option["menu"].add_command(label=item,command=tk._setit(chosen_memory,item))

def select_memory(*args):
    global memory, chosen_memory
    if chosen_memory.get() != "None":
        memory = int(chosen_memory.get())
    update_memory_list()

def memory_recall():
    global memory,space,space_text
    if memory is not None:
        space_text = str(memory)
        space.delete("1.0", "end")
        space.insert("1.0", space_text)

def memory_clear():
    global memory,memory_list
    memory_list = []
    memory = None
    update_memory_list()

def memory_add():
    global memory,memory_list,space_text
    memory = memory + int(space_text)

def memory_subtract():
    global memory,memory_list,space_text
    memory = memory - int(space_text)

space = tk.Text(height=2,width=20)
space.grid(row=1,column=1,columnspan=4,sticky="nsew")
root.grid_rowconfigure(1, weight=1)
root.grid_columnconfigure(1, weight=1)

equal_button = tk.Button(text="=",command=calculate)
equal_button.grid(row=8,column=4,sticky="nsew")
root.grid_rowconfigure(8, weight=1)
root.grid_columnconfigure(4, weight=1)

plus_button = tk.Button(text="+",command=lambda: write_equation("+"))
plus_button.grid(row=7,column=4,sticky="nsew")
root.grid_rowconfigure(7, weight=1)
root.grid_columnconfigure(4, weight=1)

minus_button = tk.Button(text="-",command=lambda: write_equation("-"))
minus_button.grid(row=6,column=4,sticky="nsew")
root.grid_rowconfigure(6, weight=1)
root.grid_columnconfigure(4, weight=1)

multiply_button = tk.Button(text="x",command=lambda: write_equation("*"))
multiply_button.grid(row=5,column=4,sticky="nsew")
root.grid_rowconfigure(5, weight=1)
root.grid_columnconfigure(4, weight=1)

division_button = tk.Button(text="÷",command=lambda: write_equation("/"))
division_button.grid(row=4,column=4,sticky="nsew")
root.grid_rowconfigure(4, weight=1)
root.grid_columnconfigure(4, weight=1)

#numbers
button_1 = tk.Button(text="1",command=lambda: write_equation("1"))
button_1.grid(row=7,column=1,sticky="nsew")
root.grid_rowconfigure(7, weight=1)
root.grid_columnconfigure(1, weight=1)

button_2 = tk.Button(text="2",command=lambda: write_equation("2"))
button_2.grid(row=7,column=2,sticky="nsew")
root.grid_rowconfigure(7, weight=1)
root.grid_columnconfigure(2, weight=1)

button_3 = tk.Button(text="3",command=lambda: write_equation("3"))
button_3.grid(row=7,column=3,sticky="nsew")
root.grid_rowconfigure(7, weight=1)
root.grid_columnconfigure(3, weight=1)

button_4 = tk.Button(text="4",command=lambda: write_equation("4"))
button_4.grid(row=6,column=1,sticky="nsew")
root.grid_rowconfigure(6, weight=1)
root.grid_columnconfigure(1, weight=1)

button_5 = tk.Button(text="5",command=lambda: write_equation("5"))
button_5.grid(row=6,column=2,sticky="nsew")
root.grid_rowconfigure(6, weight=1)
root.grid_columnconfigure(2, weight=1)

button_6 = tk.Button(text="6",command=lambda: write_equation("6"))
button_6.grid(row=6,column=3,sticky="nsew")
root.grid_rowconfigure(6, weight=1)
root.grid_columnconfigure(3, weight=1)

button_7 = tk.Button(text="7",command=lambda: write_equation("7"))
button_7.grid(row=5,column=1,sticky="nsew")
root.grid_rowconfigure(5, weight=1)
root.grid_columnconfigure(1, weight=1)

button_8 = tk.Button(text="8",command=lambda: write_equation("8"))
button_8.grid(row=5,column=2,sticky="nsew")
root.grid_rowconfigure(5, weight=1)
root.grid_columnconfigure(2, weight=1)

button_9 = tk.Button(text="9",command=lambda: write_equation("9"))
button_9.grid(row=5,column=3,sticky="nsew")
root.grid_rowconfigure(5, weight=1)
root.grid_columnconfigure(3, weight=1)

button_0 = tk.Button(text="0",command=lambda: write_equation("0"))
button_0.grid(row=8,column=2,sticky="nsew")
root.grid_rowconfigure(8, weight=1)
root.grid_columnconfigure(2, weight=1)


percentage_button = tk.Button(text="%",command=lambda: write_equation("%"))
percentage_button.grid(row=3,column=1,sticky="nsew")
root.grid_rowconfigure(3, weight=1)
root.grid_columnconfigure(1, weight=1)

ce_button = tk.Button(text="CE",command=clear_entry)
ce_button.grid(row=3,column=2,sticky="nsew")
root.grid_rowconfigure(3, weight=1)
root.grid_columnconfigure(2, weight=1)

clear_button = tk.Button(text="C",command=clear)
clear_button.grid(row=3,column=3,sticky="nsew")
root.grid_rowconfigure(3, weight=1)
root.grid_columnconfigure(3, weight=1)

delete_button = tk.Button(text="←",font=("Arial",14,"bold"),command=delete)
delete_button.grid(row=3,column=4,sticky="nsew")
root.grid_rowconfigure(3, weight=1)
root.grid_columnconfigure(4, weight=1)

inverse_button = tk.Button(text="1/x",command=inverse)
inverse_button.grid(row=4,column=1,sticky="nsew")
root.grid_rowconfigure(4, weight=1)
root.grid_columnconfigure(1, weight=1)

square_button = tk.Button(text="x²",command=square)
square_button.grid(row=4,column=2,sticky="nsew")
root.grid_rowconfigure(4, weight=1)
root.grid_columnconfigure(2, weight=1)

square_root_button = tk.Button(text="²√",command=square_root)
square_root_button.grid(row=4,column=3,sticky="nsew")
root.grid_rowconfigure(4, weight=1)
root.grid_columnconfigure(3, weight=1)

plus_minus_button = tk.Button(text="+/-",command=plus_minus)
plus_minus_button.grid(row=8,column=1,sticky="nsew")
root.grid_rowconfigure(8, weight=1)
root.grid_columnconfigure(1, weight=1)

dot_button = tk.Button(text=".",command=lambda: write_equation("."))
dot_button.grid(row=8,column=3,sticky="nsew")
root.grid_rowconfigure(8, weight=1)
root.grid_columnconfigure(3, weight=1)

#memory
frame = tk.Frame()
frame.grid(row=2,column=1,columnspan=4,sticky="nsew")
frame.grid_rowconfigure(1,weight=1)

frame.grid_columnconfigure(1,weight=1)
frame.grid_columnconfigure(2,weight=1)
frame.grid_columnconfigure(3,weight=1)
frame.grid_columnconfigure(4,weight=1)
frame.grid_columnconfigure(5,weight=1)
frame.grid_columnconfigure(6,weight=1)


memory_store_button = tk.Button(frame,text="MS",command=memory_store)
memory_store_button.grid(row=2,column=5,sticky="nsew")

memory_recall_button = tk.Button(frame,text="MR",command=memory_recall)
memory_recall_button.grid(row=2,column=2,sticky="nsew")

memory_clear_button = tk.Button(frame,text="MC",command=memory_clear)
memory_clear_button.grid(row=2,column=1,sticky="nsew")

memory_add_button = tk.Button(frame,text="M+",command=memory_add)
memory_add_button.grid(row=2,column=3,sticky="nsew")

memory_subtract_button = tk.Button(frame,text="M-",command=memory_subtract)
memory_subtract_button.grid(row=2,column=4,sticky="nsew")

chosen_memory = tk.StringVar()
chosen_memory.set("None")
chosen_memory.trace("w", select_memory)

memory_option = tk.OptionMenu(frame, chosen_memory, *(memory_list if memory_list else ["None"]))
memory_option.grid(row=2,column=6,sticky="nsew")

root.mainloop()