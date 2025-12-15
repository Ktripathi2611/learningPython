import tkinter as tk

# Create main window
window = tk.Tk()
window.title("Calculator")
window.geometry("300x400")

# Entry widget for display
display = tk.Entry(window, font=("Arial", 20), borderwidth=5, relief="ridge", justify="right")
display.grid(row=0, column=0, columnspan=4, padx=10, pady=10, ipady=10)

# Function to handle button clicks
def click_button(value):
    current = display.get()
    display.delete(0, tk.END)
    display.insert(0, current + value)

# Function to clear display
def clear_display():
    display.delete(0, tk.END)

# Function to evaluate expression
def evaluate():
    try:
        result = eval(display.get())
        display.delete(0, tk.END)
        display.insert(0, str(result))
    except Exception:
        display.delete(0, tk.END)
        display.insert(0, "Error")

# Button layout
buttons = [
    ("7", 1, 0), ("8", 1, 1), ("9", 1, 2), ("/", 1, 3),
    ("4", 2, 0), ("5", 2, 1), ("6", 2, 2), ("*", 2, 3),
    ("1", 3, 0), ("2", 3, 1), ("3", 3, 2), ("-", 3, 3),
    ("0", 4, 0), (".", 4, 1), ("+", 4, 2), ("=", 4, 3),
]

# Create buttons dynamically
for (text, row, col) in buttons:
    if text == "=":
        btn = tk.Button(window, text=text, width=5, height=2, font=("Arial", 14),
                        command=evaluate)
    else:
        btn = tk.Button(window, text=text, width=5, height=2, font=("Arial", 14),
                        command=lambda t=text: click_button(t))
    btn.grid(row=row, column=col, padx=5, pady=5)

# Clear button
clear_btn = tk.Button(window, text="C", width=22, height=2, font=("Arial", 14),
                      command=clear_display)
clear_btn.grid(row=5, column=0, columnspan=4, padx=5, pady=5)

# Run the application
window.mainloop()