import tkinter as tk
from tkinter import messagebox
from main import run_assistant  # from your main pipeline

def on_click():
    run_assistant()

# Set up GUI
root = tk.Tk()
root.title("Vernacular Voice Assistant")

root.geometry("400x300")
root.configure(bg="#f5f5f5")

label = tk.Label(root, text="🎙 Vernacular Voice Assistant", font=("Arial", 16, "bold"), bg="#f5f5f5")
label.pack(pady=20)

btn = tk.Button(root, text="Start Listening", command=on_click, font=("Arial", 14), bg="#4CAF50", fg="white", padx=10, pady=5)
btn.pack(pady=20)

note = tk.Label(root, text="Supports Telugu 🇮🇳 Hindi 🇮🇳 English 🇬🇧", font=("Arial", 10), bg="#f5f5f5")
note.pack()

root.mainloop()
