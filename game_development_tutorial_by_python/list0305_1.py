import tkinter

#input key
key = ""
koff = False
def key_down(e):
    global key,koff
    key = e.keysym
    koff = False
    
def key_up(e):
    global key
    key = ""
    
DIR_UP = 0
DIR_DOWN = 1
DIR_LEFT =2
DIR_RIGHT = 3
ANIMATION = [0,1,0,2]

tmr = 0

pen_x = 90
pen_y = 90
pen_d = 0
pen_a = 0

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
    canvas.delete("SCXREEN")
    for y in range(9):
        for x in range(12):
            canvas.create_image(x*60+30, y*60+30, image=img_bg[map_data[y][x]], tag = "SCREEN")
            canvas.create_image(pen_x, pen_y, image=img_pen[pen_a], tag = "SCREEN")


def check_wall(cx, cy, di, dot):#each direction"s wall is searching
    chk = False
    if di == DIR_UP:
        mx = int((cx-30)/60)
        my = int((cy-30-dot)/60)
        if map_data[my][mx] <= 1:#LEFT&UP
            chk =  True
        mx = int((cx+29)/60)
        if map_data[my][mx] <= 1: #RIGHT&UP
            chk = True
    if di == DIR_DOWN:
        mx = int((cx-30)/60)
        my = int((cy+29+dot)/60)
        if map_data[my][mx] <= 1:#LEFT&DOWN
            chk =  True
        mx = int((cx+29)/60)
        if map_data[my][mx] <= 1: #RIGHT&DOWN
            chk = True
    if di == DIR_LEFT:
        mx = int((cx-30-dot)/60)
        my = int((cy-30)/60)
        if map_data[my][mx] <= 1:#LEFT&UP
            chk =  True
        my = int((cy+29)/60)
        if map_data[my][mx] <= 1: #RIGHT&DOWN
            chk = True
    if di == DIR_RIGHT:
        mx = int((cx+29+dot)/60)
        my = int((cy-30)/60)
        if map_data[my][mx] <= 1:#RIGHTT&UP
            chk =  True
        mx = int((cx+29)/60)
        if map_data[my][mx] <= 1: #RIGHT&DOWN
            chk = True
    return chk


def move_penpen(): #move penpen
    global pen_x, pen_y, pen_d, pen_a
    if key == "Up":
        pen_d = DIR_UP
        if check_wall(pen_x, pen_y, pen_d, 20) == False:
            pen_y = pen_y-20
    if key == "Down":
        pen_d = DIR_DOWN
        if check_wall(pen_x, pen_y, pen_d,20) == False:
            pen_y = pen_y + 20
    if key == "Left":
        pen_d = DIR_LEFT
        if check_wall(pen_x, pen_y, pen_d,20) == False:
            pen_x = pen_x - 20
    if key == "Right":
        pen_d = DIR_RIGHT
        if check_wall(pen_x, pen_y, pen_d,20) == False:
            pen_x = pen_x + 20
    pen_a = pen_d*3 + ANIMATION[tmr%4]
            
            
def main(): #main loop
    global key, koff,tmr
    tmr = tmr + 1
    draw_screen()
    move_penpen()
    if koff == True:
        key = ""
        koff = False
    root.after(100,main)


root = tkinter.Tk()

img_bg = [
    tkinter.PhotoImage(file = "/home/pi/Downloads/py2_samples/Chapter3/image_penpen/chip00.png"),
    tkinter.PhotoImage(file = "/home/pi/Downloads/py2_samples/Chapter3/image_penpen/chip01.png"),
    tkinter.PhotoImage(file = "/home/pi/Downloads/py2_samples/Chapter3/image_penpen/chip02.png"),
    tkinter.PhotoImage(file = "/home/pi/Downloads/py2_samples/Chapter3/image_penpen/chip03.png")
]
img_pen =[
    tkinter.PhotoImage(file = "/home/pi/Downloads/py2_samples/Chapter3/image_penpen/pen00.png"),
    tkinter.PhotoImage(file = "/home/pi/Downloads/py2_samples/Chapter3/image_penpen/pen01.png"),
    tkinter.PhotoImage(file = "/home/pi/Downloads/py2_samples/Chapter3/image_penpen/pen02.png"),
    tkinter.PhotoImage(file = "/home/pi/Downloads/py2_samples/Chapter3/image_penpen/pen03.png"),
    tkinter.PhotoImage(file = "/home/pi/Downloads/py2_samples/Chapter3/image_penpen/pen04.png"),
    tkinter.PhotoImage(file = "/home/pi/Downloads/py2_samples/Chapter3/image_penpen/pen05.png"),
    tkinter.PhotoImage(file = "/home/pi/Downloads/py2_samples/Chapter3/image_penpen/pen06.png"),
    tkinter.PhotoImage(file = "/home/pi/Downloads/py2_samples/Chapter3/image_penpen/pen07.png"),
    tkinter.PhotoImage(file = "/home/pi/Downloads/py2_samples/Chapter3/image_penpen/pen08.png"),
    tkinter.PhotoImage(file = "/home/pi/Downloads/py2_samples/Chapter3/image_penpen/pen09.png"),
    tkinter.PhotoImage(file = "/home/pi/Downloads/py2_samples/Chapter3/image_penpen/pen10.png"),
    tkinter.PhotoImage(file = "/home/pi/Downloads/py2_samples/Chapter3/image_penpen/pen11.png"),
]

root.title("HARAHARA penguin rabilince")
root.resizable(False,False)
root.bind("<KeyPress>", key_down)
root.bind("<KeyRelease>", key_up)
canvas = tkinter.Canvas(width=720,height=540)
canvas.pack()
main()
root.mainloop()