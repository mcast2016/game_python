import tkinter
fnt1 = ("Times New Roman", 20)
fnt2 = ("Times New Roman", 40)
index = 0
timer = 0

key =""
def key_down(e):
    global key
    key = e.keysym
    print(key)
    
def main():
    print("main_1")
    global index, timer
    canvas.delete("STATUS")
    timer = timer + 1
    canvas.create_text(200,30, text="index"+str(index),fill = "white", font =fnt1,tag="STATUS")
    canvas.create_text(400,30, text="timer"+str(timer),fill = "cyan", font =fnt1,tag="STATUS")
    
    if index == 0:
        print("main_2")
        if timer ==1:
            print("main_2")
            canvas.create_text(300,150, text="TITLE",fill="white",font=fnt2,tag="TITLE")
            canvas.create_text(300,300, text="Press[SPACE]Key",fill="white",font=fnt2,tag="TITLE")
        if key == "space":
            print("main_3")
            canvas.delete("TITLE")
            canvas.create_rectangle(0,0,600,400,fill='blue', tag ="GAME")
            canvas.create_text(300,150,text="gaming now",fill='white',font=fnt2,tag="GAME")
            canvas.create_text(300,300,text="[E]exit",fill='yellow',font = fnt1,tag="GAME")
            index = 1
            timer = 0
                
    if index == 1:
        print("main_4")
        if key == "e":
            canvas.delete("GAME")
            canvas.create_rectangle(0,0,600,400,fill="maroon", tag="OVER")
            canvas.create_text(300,150,text="GAME OVER",fill="red",font=fnt2,tag="OVER")
            index =2
            timer =0
                
    if index == 2:
       if timer ==30:
            canvas.delete("OVER")
            index =0
            timer =0
                
    root.after(100,main)
    print("main_LAST")
    
root = tkinter.Tk()
print("root_1")
root.title("index & timer")
root.bind("<KeyPress>", key_down)
print("root_2")
canvas = tkinter.Canvas(width=600, height=400, bg="black")
canvas.pack()
main()
print("root_3")
root.mainloop()
