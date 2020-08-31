import tkinter as tk
import os
from tkinter import filedialog, Text

# base of the app
root = tk.Tk()
root.geometry("500x500")
root.title("Guess the Number!")
root['bg'] = '#001524'

# Label Guess the number, attached to the root
introLbl = tk.Label(root, text="Guess the number", padx=10, pady=10,
                    fg="white", bg="#001524", font="Sans, 16")
introLbl.pack()

# Frame, attached to the root
frame = tk.Frame(root, bg="#15616d")
frame.place(relwidth="0.8", relheight="0.8", relx=0.1, rely=0.1)

# Inser here label
insertLbl = tk.Label(frame, text="Insert the number here", padx=10, pady=10,
                     fg="white", bg="#15616d", font="12")
insertLbl.place(relwidth="0.50", relheight="0.1", relx=0.25, rely=0.01)

user = tk.Entry(frame, width=2)
user.pack()
user.focus_set()


# Btn, attached to the frame
unoBtn = tk.Button(frame, text="Ciaone", padx=15, pady=15, font="12")
unoBtn.place(relwidth="0.4", relheight="0.1", relx=0.3, rely=0.8)


# Main
if __name__ == "__main__":
    root.mainloop()
