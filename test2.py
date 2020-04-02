from tkinter import *

root = Tk()

labelframe = LabelFrame(root, text="This is a LabelFrame",relief=SUNKEN)
labelframe.pack(fill="both", expand="yes")
 
left = Entry(labelframe, text="Inside the LabelFrame")
left.pack()
def change():
    left.insert(1,1)
button=Button(root,text="click me",command=change)
button.pack()
 
root.mainloop()