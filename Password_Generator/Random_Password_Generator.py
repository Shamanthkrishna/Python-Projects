import random
from tkinter import *
import string
from tkinter.font import Font
import pyperclip
import zxcvbn
import os

def generate_password():
    password_length = int(length_entry.get())
    include_letters = letters_var.get()
    include_numbers = numbers_var.get()
    include_symbols = symbols_var.get()

    if not (include_letters or include_numbers or include_symbols):
        lbl.config(text="Select at least one character type")
        return

    characters = ""
    if include_letters:
        characters += string.ascii_letters
    if include_numbers:
        characters += string.digits
    if include_symbols:
        characters += string.punctuation

    password = ''.join(random.choice(characters) for _ in range(password_length))
    lbl.config(text=password)
    update_password_history(password)
    update_password_strength(password)

def copy_to_clipboard():
    pyperclip.copy(lbl.cget("text"))

def update_password_strength(password):
    result = zxcvbn.zxcvbn(password)
    score = result['score']
    feedback = result['feedback']['suggestions']
    strength_text = f"Strength: {['Very Weak', 'Weak', 'Fair', 'Good', 'Strong'][score]}"
    if feedback:
        strength_text += "\nSuggestions: " + ', '.join(feedback)
    strength_lbl.config(text=strength_text)

def update_password_history(password):
    password_history.insert(END, password)
    if password_history.size() > 10:  # limit history to 10 entries
        password_history.delete(0)
    
    save_to_file(password)

def save_to_file(password):
    result = zxcvbn.zxcvbn(password)
    score = result['score']
    feedback = result['feedback']['suggestions']
    strength_text = f"Strength: {['Very Weak', 'Weak', 'Fair', 'Good', 'Strong'][score]}"
    feedback_text = ', '.join(feedback) if feedback else 'No suggestions'
    
    with open("password_history.txt", "a") as file:
        file.write(f"Password: {password}\n")
        file.write(f"{strength_text}\n")
        file.write(f"Suggestions: {feedback_text}\n\n")

root = Tk()
root.geometry("400x400")
root.title("Password Generator")

# Password length
length_label = Label(root, text="Password Length:")
length_label.pack(pady=5)
length_entry = Entry(root)
length_entry.pack(pady=5)
length_entry.insert(0, "12")

# Character type options
letters_var = BooleanVar(value=True)
numbers_var = BooleanVar(value=True)
symbols_var = BooleanVar(value=True)

letters_check = Checkbutton(root, text="Include Letters", var=letters_var)
letters_check.pack(pady=5)
numbers_check = Checkbutton(root, text="Include Numbers", var=numbers_var)
numbers_check.pack(pady=5)
symbols_check = Checkbutton(root, text="Include Symbols", var=symbols_var)
symbols_check.pack(pady=5)

# Generate button
btn = Button(root, text="Generate Password", command=generate_password)
btn.pack(pady=10)

# Password display
myFont = Font(family="Times New Roman", size=12)
lbl = Label(root, font=myFont, text="")
lbl.pack(pady=10)

# Copy to clipboard button
copy_btn = Button(root, text="Copy to Clipboard", command=copy_to_clipboard)
copy_btn.pack(pady=5)

# Password strength display
strength_lbl = Label(root, text="")
strength_lbl.pack(pady=10)

# Password history
history_label = Label(root, text="Password History:")
history_label.pack(pady=5)
password_history = Listbox(root)
password_history.pack(pady=5)

root.mainloop()
