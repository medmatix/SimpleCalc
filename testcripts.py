#===============================================================================
# from tkinter import *
# 
# root = Tk()
# def cllbk():
#     print("This is a function")
# 
# root.bind("<Control-Shift-s>", lambda:cllbk) # Doesn't work
# root.bind("<Control-s>", lambda:cllbk) # Works perfectly
# 
# root.mainloop()
#===============================================================================

#===============================================================================
# from tkinter import *
# 
# root = Tk()
# 
# def callback(event):
#     print("clicked at", event.x, event.y)
#     
# def callback2():
#     print(" s Key")
# 
# frame = Frame(root, width=100, height=100)
# #===============================================================================
# # frame.bind("<Button-1>", callback)
# #===============================================================================
# frame.bind("<Control-s>", lambda: callback2)
# frame.pack()
# 
# root.mainloop()
#===============================================================================

from tkinter import *

root = Tk()

def areturn(event):
    print("\r")

def key(event):
    print("pressed", repr(event.char))
    #print("That's it!!!!!!")

def callbck(event):
    frame.focus_set()
    print("clicked at", event.x, event.y)

frame = Frame(root, width=100, height=100)
frame.bind("<Key>", key)
frame.bind("<Return>", areturn)
frame.bind("<Button-1>", callbck)
frame.pack()

root.mainloop()