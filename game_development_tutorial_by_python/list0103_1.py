import tkinter

root = tkinter.Tk()
root.title("drowing image in Canvas")
canvas = tkinter.Canvas(width=480, height=300)
canvas.pack()
img_bg = tkinter.PhotoImage(file="/home/pi/Downloads/py2_samples/Chapter1/park.png")
canvas.create_image(240,150, image=img_bg)
root.mainloop()
