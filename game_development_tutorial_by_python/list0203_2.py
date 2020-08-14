import tkinter
import math

def trigo():
    try:
        d = float(entry.get())
        a = math.radians(d)
        s = math.sin(a)
        c = math.cos(a)
        t = math.tan(a)
        label_s["text"] = "sin" +str(s)
        label_c["text"] = "sin" +str(c)
        label_t["text"] = "sin" +str(t)
    except:
        print("change radian's value")
        
root = tkinter.Tk()
root.geometry("300x200")
root.title("Trigonometric function value")

entry = tkinter.Entry(width=10)
entry.place(x=20,y=20)
button = tkinter.Button(text="cal",command=trigo)
button.place(x=110,y=20)
label_s = tkinter.Label(text="sin")
label_s.place(x=20,y=60)
label_c = tkinter.Label(text="sin")
label_c.place(x=20,y=100)
label_t = tkinter.Label(text="sin")
label_t.place(x=20,y=140)

root.mainloop()