import tkinter as tk
import math

# --- Functions ---
def click_button(value):
    current = str(entry.get())
    entry.delete(0, tk.END)
    entry.insert(0, current + value)

def clear():
    entry.delete(0, tk.END)

def delete():
    current = entry.get()
    entry.delete(0, tk.END)
    entry.insert(0, current[:-1])

def calculate():
    try:
        expression = entry.get()
        # Replace safe functions
        expression = expression.replace("^", "**")
        result = eval(expression, {"__builtins__": None}, math.__dict__)
        entry.delete(0, tk.END)
        entry.insert(0, str(result))
    except Exception as e:
        entry.delete(0, tk.END)
        entry.insert(0, "Error")

# --- UI Setup ---
root = tk.Tk()
root.title("Scientific Calculator")
root.configure(bg="black")

entry = tk.Entry(root, width=25, font=("Arial", 18), borderwidth=5, relief="ridge", justify="right")
entry.grid(row=0, column=0, columnspan=6, padx=10, pady=10)

# --- Buttons ---
buttons = [
    ("7",1,0), ("8",1,1), ("9",1,2), ("/",1,3), ("sin",1,4), ("cos",1,5),
    ("4",2,0), ("5",2,1), ("6",2,2), ("*",2,3), ("tan",2,4), ("log",2,5),
    ("1",3,0), ("2",3,1), ("3",3,2), ("-",3,3), ("sqrt",3,4), ("^",3,5),
    ("0",4,0), (".",4,1), ("(",4,2), (")",4,3), ("+",4,4), ("pi",4,5),
]

for (text, r, c) in buttons:
    b = tk.Button(root, text=text, width=6, height=2, font=("Arial", 14),
                  bg="#333", fg="white",
                  command=lambda t=text: click_button(t if t not in ["sin","cos","tan","log","sqrt","pi"] else f"math.{t}(" if t!="pi" else "math.pi"))
    b.grid(row=r, column=c, padx=3, pady=3)

# Extra buttons
tk.Button(root, text="C", width=6, height=2, font=("Arial", 14), bg="red", fg="white", command=clear).grid(row=5, column=0)
tk.Button(root, text="⌫", width=6, height=2, font=("Arial", 14), bg="orange", fg="black", command=delete).grid(row=5, column=1)
tk.Button(root, text="=", width=15, height=2, font=("Arial", 14), bg="green", fg="white", command=calculate).grid(row=5, column=2, columnspan=2)

root.mainloop()
