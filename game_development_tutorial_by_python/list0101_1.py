import tkinter

root = tkinter.Tk()
root.geometry("400x200")
root.title("use python GUI")
label = tkinter.Label(root, text="First game process",font=("Times New Roman", 20))
label.place(x=80,y=60)
root.mainloop()