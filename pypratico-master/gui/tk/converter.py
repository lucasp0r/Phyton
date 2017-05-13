# example from section 4.2 of the book
# "Modern Tkinter for Busy Python Programmers

import tkinter as tk
from tkinter import N, W, E, S
from tkinter import ttk

def calculate(*args):
    try:
        value = float(feet.get())
        meters.set(format(value * 12 * 0.0254, 'f'))
    except ValueError:
        pass

root = tk.Tk()
root.title("Feet to Meters")

mainframe = ttk.Frame(root, padding="3 3 12 12")
#mainframe.grid(column=0, row=0, sticky=(N, W, E, S))
#???
#mainframe.columnconfigure(0, weight=1)
#mainframe.rowconfigure(0, weight=1)

mainframe.pack()

feet = tk.StringVar()
meters = tk.StringVar()

feet_entry = ttk.Entry(mainframe, width=7, textvariable=feet)
feet_entry.grid(column=2, row=1, sticky=(W, E))

ttk.Label(mainframe, textvariable=meters).grid(column=2, row=2, sticky=(W, E))
ttk.Button(mainframe, text="Calculate", command=calculate).grid(column=3, row=3, sticky=W)

ttk.Label(mainframe, text="feet").grid(column=3, row=1, sticky=W)
ttk.Label(mainframe, text="is equivalent to").grid(column=1, row=2, sticky=E)
ttk.Label(mainframe, text="meters").grid(column=3, row=2, sticky=W)

for child in mainframe.winfo_children():
    child.grid_configure(padx=5, pady=5)

feet_entry.focus()
root.bind('<Return>', calculate)

root.mainloop()
