import tkinter as tk

window = tk.Tk()
window.geometry("500x500")
window.title("First Python PJ")

def func():
    text="Hello, world!"
    textOutput = tk.Label(window, text=text, fg="blue", font="Helvetica, 16")
    textOutput.grid(row=0, column=1)

firstBtn = tk.Button(text="Yo", command=func)
firstBtn.grid(row=0, column=0)

if __name__ == "__main__":
    window.mainloop()