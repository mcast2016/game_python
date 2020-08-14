import tkinter
from tkinter import messagebox
def btnFunc(event):
    messagebox.showinfo('message','Bingo!')

root=tkinter.Tk()

guiLabel=tkinter.Label(text=u'python sample')
guiLabel.pack()
guiEditbox=tkinter.Entry()
guiEditbox.pack()
guiButton=tkinter.Button(text=u'OK')
guiButton.bind("<Button-1>",btnFunc)
guiButton.pack()
root.mainloop()