import tkinter as tk

def click(button_text):
    current = entry.get()
    entry.delete(0, tk.END)
    entry.insert(0, current + button_text)

def clear():
    entry.delete(0, tk.END)

def calculate():
    try:
        result = eval(entry.get())
        entry.delete(0, tk.END)
        entry.insert(0, str(result))
    except Exception:
        entry.delete(0, tk.END)
        entry.insert(0, "Error")


root = tk.Tk()
root.title("calculator")
root.geometry("300x400")  

# Vstupní pole
entry = tk.Entry(root, font=("Arial", 20), borderwidth=2, relief="solid", justify="right")
entry.grid(row=0, column=0, columnspan=4, sticky="nsew", padx=5, pady=5)


buttons = [
    ('7', '8', '9', '/'),
    ('4', '5', '6', '*'),
    ('1', '2', '3', '-'),
    ('0', '.', '=', '+')
]

for i, row in enumerate(buttons):
    for j, text in enumerate(row):
        if text == '=':
            btn = tk.Button(root, text=text, font=("Arial", 18), command=calculate)
        else:
            btn = tk.Button(root, text=text, font=("Arial", 18), command=lambda t=text: click(t))
        btn.grid(row=i+1, column=j, sticky="nsew", padx=2, pady=2)

# Clear button
clear_btn = tk.Button(root, text="C", font=("Arial", 18), command=clear)
clear_btn.grid(row=5, column=0, columnspan=4, sticky="nsew", padx=2, pady=2)


for i in range(6):  # 0 až 5 řádky
    root.rowconfigure(i, weight=1)
for j in range(4):  # 0 až 3 sloupce
    root.columnconfigure(j, weight=1)

root.mainloop()
