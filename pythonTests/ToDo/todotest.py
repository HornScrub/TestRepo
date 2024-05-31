import todo
import io
from contextlib import redirect_stdout
import tkinter as tk

testList = [[1, True], [2, False]]
# Create a StringIO object to capture output
output = io.StringIO()

# Use redirect_stdout context manager to redirect output to the StringIO object
with redirect_stdout(output):
    todo.view_tasks("ToDoList.txt")

captured_output = output.getvalue()

print("Captured Output:", captured_output)

#Create a root window
root = tk.Tk()

# Set the title of the window
root.title("My First Tkinter Window")

# Set the size of the window (width x height)
root.geometry("800x600")

# Create a label widget
label1 = tk.Label(root, text="Hello, Tkinter!")
label1.pack(padx=160, pady=10)

label2 = tk.Label(root, text="What's up?")
label2.pack(padx=160, pady=50)

# Create a button widget
def on_button_click():
    label1.config(text="Button Clicked!")

button = tk.Button(root, text="Click Me", command=on_button_click)
button.pack(pady=20)

# Run the Tkinter event loop
root.mainloop()