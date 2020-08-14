import tkinter
import datetime

def time_now():
    nowday = datetime.datetime.now()
    nowtime = "{0}:{1}:{2}".format(nowday.hour, nowday.minute, nowday.second)
    label1["text"] = nowtime
    root.after(1000,time_now)
    
root = tkinter.Tk()
root.geometry("400x100")
root.title("`easy_clock")
label1 = tkinter.Label(font = ("Times New Roman", 60))
label1.pack()
time_now()
root.mainloop()
    