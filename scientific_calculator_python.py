from tkinter import *
import math
import parser
import tkinter.messagebox

root = Tk()
root.title("Scientitific Calculator")
root.configure(background="powder blue")
root.resizable(width=False, height=False)
root.geometry("480x568+0+0")

calc = Frame (root)
calc.grid()



#========================== MENU ====================================#

def iExit():
    iExit = tkinter.messagebox.askyesno("Scientitific Calculator", "Confirm if you want to exit")
    if iExit > 0:
        root.destroy()
        return

menubar = Menu(calc)

filemenu = Menu(menubar, tearoff=0)
menubar.add_cascade(label = "Options", menu=filemenu)
filemenu.add_command(label = "Standard")
filemenu.add_command(label = "Scientific")
filemenu.add_separator()
filemenu.add_command(label = "Exit", command = iExit)

editmenu = Menu(menubar, tearoff=0)
menubar.add_cascade(label = "Edit", menu=editmenu)
editmenu.add_command(label = "Cut")
editmenu.add_command(label = "Copy")
editmenu.add_command(label = "Paste")

helpmenu = Menu(menubar, tearoff=0)
menubar.add_cascade(label = "Help", menu=helpmenu)
helpmenu.add_command(label = "View Help")


root.config(menu=menubar)
root.mainloop()
