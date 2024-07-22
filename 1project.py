import tkinter as tk
from tkinter import ttk
import pyttsx3

def text_to_speech():
    text = text_entry.get()
    engine = pyttsx3.init()
    engine.say(text)
    engine.runAndWait()

root = tk.Tk()
root.title("Text-to-Speech Converter")

# Create a label
label = ttk.Label(root, text="Enter text to convert to speech:")
label.grid(row=0, column=0, columnspan=2, padx=10, pady=10)

# Create an entry field
text_entry = ttk.Entry(root, width=40)
text_entry.grid(row=1, column=0, columnspan=2, padx=10, pady=10)

# Create a button for converting text to speech
convert_button = ttk.Button(root, text="Convert to Speech", command=text_to_speech)
convert_button.grid(row=2, column=0, columnspan=2, padx=10, pady=10)

root.mainloop()


