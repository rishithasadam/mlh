import tkinter as tk

def greet():
    """Function to display a greeting message."""
    name = entry.get()
    if name:
        greeting_label.config(text="Hello, " + name + "!")
    else:
        greeting_label.config(text="Hello, there!")

# Create the main application window
root = tk.Tk()
root.title("Greeting App")

# Create and pack widgets
entry = tk.Entry(root, width=30)
entry.pack(pady=10)

greet_button = tk.Button(root, text="Greet", command=greet)
greet_button.pack(pady=5)

greeting_label = tk.Label(root, text="")
greeting_label.pack(pady=5)

# Run the main event loop
root.mainloop()
