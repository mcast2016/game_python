from tkinter import *
from tkinter import ttk
import pandas as pd

root = Tk()
root.title('prepost CSV file')

frame1 = ttk.Frame(root, padding=16)
label1 = ttk.Label(frame1, text='csv path')
inputword = StringVar()
entry1 = ttk.Entry(frame1, textvariable=inputword)
button1=ttk.Button(
    frame1,
    text='OK',
    command=lambda: df = pd.read_csv('{{%s}}' % inputword.get()))
#layoout
frame1.pack()
label1.pack(side=LEFT)
entry1.pack(side=LEFT)
button1.pack(side=LEFT)

root.mainloop()