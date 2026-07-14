import tkinter as tk
from tkinter import messagebox

def greet_user():
    """Display a greeting message based on the entered name."""
    name = name_entry.get().strip()
    if not name:
        messagebox.showwarning("Input Error", " enter chat to sent.")
        return
    messagebox.showinfo("Message Sent", f"Your message has been sent.")

# Create the main application window
root = tk.Tk()
root.title("Simple Python GUI")
root.geometry("300x150")  # Width x Height

# Create and place a label
label = tk.Label(root, text="Enter your message:")
label.pack(pady=5)

# Create and place a text entry field
name_entry = tk.Entry(root, width=30)
name_entry.pack(pady=5)

# Create and place a button
greet_button = tk.Button(root, text="send message", command=greet_user)
greet_button.pack(pady=10)

# Start the Tkinter event loop
root.mainloop()
