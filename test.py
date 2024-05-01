import tkinter as tk

window = tk.Tk()


w = tk.Text(master=window, height=1, borderwidth=0)
w.insert(1.0, "Hello, world!")
w.pack()

w.configure(state="disable")

window.mainloop()