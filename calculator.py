import tkinter as tk

# Function to update the display when a button is clicked
def button_click(symbol):
    current = display.get()
    if current == "Error!":
        display.set("")
    if symbol == "C":
        display.set("")
    elif symbol == "=":
        try:
            result = eval(current)
            display.set(result)
        except:
            display.set("Error!")
    else:
        display.set(current + symbol)

# Create the main window
root = tk.Tk()
root.title("Calculator by Rishi Developer")

# Entry widget to display the calculation
display = tk.StringVar()
entry = tk.Entry(root, textvariable=display, font=('Arial', 20), bd=10, insertwidth=4, width=14, justify='right')
entry.grid(row=0, column=0, columnspan=4)

# List of button symbols
buttons = [
    ('7', '8', '9', '/'),
    ('4', '5', '6', '*'),
    ('1', '2', '3', '-'),
    ('C', '0', '=', '+')
]

# Create buttons and place them in the grid
for i in range(len(buttons)):
    for j in range(len(buttons[i])):
        button_text = buttons[i][j]
        button = tk.Button(root, text=button_text, font=('Arial', 20), padx=30, pady=20, command=lambda button_text=button_text: button_click(button_text))
        button.grid(row=i+1, column=j, sticky='nsew')

# Configure row and column weights to make buttons expandable
for i in range(len(buttons)+1):
    root.grid_rowconfigure(i, weight=1)
for j in range(len(buttons[0])):
    root.grid_columnconfigure(j, weight=1)

# Run the application
root.mainloop()