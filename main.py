import tkinter as tk
from tkinter import * 
from tkinter import messagebox, ttk

pisun_int = 0

root = Tk()
root.title("Писюн кликер")
root.geometry("300x400")

frame = Frame(
   root,
   padx=50,
   pady=10
)
frame.pack(fill=tk.BOTH, expand=True)
root.resizable(False, False)

label = Label(frame, text="Писюнов натапано: ")
label.grid(row=1, column=1)

btn = ttk.Button(image=photo)
btn.pack()
if __name__ == "__main__":
    root.mainloop()