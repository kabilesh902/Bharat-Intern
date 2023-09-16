import tkinter as tk

def on_button_click(text):
    if text == "=":
        try:
            result = eval(entry.get())
            entry.delete(0, tk.END)
            entry.insert(tk.END, str(result))
        except Exception as e:
            entry.delete(0, tk.END)
            entry.insert(tk.END, "Error")
    elif text == "C":
        entry.delete(0, tk.END)
    else:
        entry.insert(tk.END, text)

root = tk.Tk()
root.title("Calculator")

entry = tk.Entry(root, font=("Helvetica", 16))
entry.grid(row=0, column=0, columnspan=4)

buttons = [
    "7", "8", "9", "/",
    "4", "5", "6", "*",
    "1", "2", "3", "-",
    "0", "C", "=", "+"
]

row_val = 1
col_val = 0

for button in buttons:
    button_obj = tk.Button(root, text=button, padx=20, pady=20, font=("Helvetica", 16), command=lambda b=button: on_button_click(b))
    button_obj.grid(row=row_val, column=col_val)
    col_val += 1

    if col_val > 3:
        col_val = 0
        row_val += 1

root.mainloop()
