from tkinter import *
from tkinter.messagebox import showerror
def add_text(text):
    entry_var.set(entry_var.get() + text)
def calculate():
    try:
        expr = entry_var.get().replace('xx', '**') 
        result = eval(expr)
        entry_var.set(str(result))
    except:
        showerror("Error", "Invalid Expression!")
def clear():
    entry_var.set("")
def backspace():
    entry_var.set(entry_var.get()[:-1])
root = Tk()
root.title("Simple Calculator")
root.geometry("250x350")
root.resizable(False, False)
entry_var = StringVar()
Entry(root, textvariable=entry_var, font=("Arial", 18), justify="right").pack(fill="both", padx=10, pady=10)
buttons = [
    ['7', '8', '9', '/'],
    ['4', '5', '6', '*'],
    ['1', '2', '3', '-'],
    ['0', '.', 'xx', '+'],
    ['AC', 'C', '=', '()']
]
for row in buttons:
    frame = Frame(root)
    frame.pack(expand=True, fill="both")
    for btn in row:
        action = lambda b=btn: (
            calculate() if b == '=' else
            clear() if b == 'AC' else
            backspace() if b == 'C' else
            add_text('(') if b == '()' and entry_var.get()[-1:] != '(' else
            add_text(')') if b == '()' else
            add_text(b)
        )
        Button(frame, text=btn, font=("Arial", 14), command=action).pack(side="left", expand=True, fill="both")
root.mainloop()
