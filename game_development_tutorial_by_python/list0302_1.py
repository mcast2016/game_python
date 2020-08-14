import tkinter

map_data = [
    [0,1,1,1,1,0,0,1,1,1,1,0],
    [0,2,3,3,2,1,1,2,3,3,2,0],
    [0,3,0,0,3,3,3,3,0,0,3,0],
    [0,3,1,1,3,0,0,3,1,1,3,0],
    [0,3,2,2,3,0,0,3,2,2,3,0],
    [0,3,0,0,3,1,1,3,0,0,3,0],
    [0,3,1,1,3,3,3,3,1,1,3,0],
    [0,2,3,3,2,0,0,2,3,3,2,0],
    [0,0,0,0,0,0,0,0,0,0,0,0]
]

def draw_screen(): #open game monitor
    for y in range(9):
        for x in range(12):
            canvas.create_image(x*60+30, y*60+30, image=img_bg[map_data[y][x]])
                                
root = tkinter.Tk()
root.title("HARAHARA penguin rabilince")
root.resizable(False,False)
canvas = tkinter.Canvas(width=720,height=540)
canvas.pack()
img_bg = [
    tkinter.PhotoImage(file = "/home/pi/Downloads/py2_samples/Chapter3/image_penpen/chip00.png"),
    tkinter.PhotoImage(file = "/home/pi/Downloads/py2_samples/Chapter3/image_penpen/chip01.png"),
    tkinter.PhotoImage(file = "/home/pi/Downloads/py2_samples/Chapter3/image_penpen/chip02.png"),
    tkinter.PhotoImage(file = "/home/pi/Downloads/py2_samples/Chapter3/image_penpen/chip03.png")
]
draw_screen()
root.mainloop()
