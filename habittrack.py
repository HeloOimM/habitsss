import tkinter as tk
from tkinter import *
from tkinter.ttk import *
from tkinter import ttk
from tkinter import messagebox
h = tk.Tk()
h.geometry("800x800")
h.title("Habit...")
h.configure(bg="#e9edff")
total= tk.StringVar(value="...")
completed= tk.StringVar(value="...")
ongoing = tk.StringVar(value="...")
description = tk.StringVar()
habit = []
plus = []
minus = []
prog = tk.StringVar(value="... %")
def counter():
    global item
    length = len(habit)
    progress["maximum"]= len(habit)
    counts = 0
    for item in habit:
        if (item["checked"].get()):
            counts +=1
    completed.set(str(counts))
    ongoing.set(str(len(habit)-counts))
    total.set(str(len(habit)))
    prog.set(f"{str(int(counts/len(habit)*100))}%")
    progress["value"] = counts
def delt(stuff):
    stuff["frame"].destroy()
    habit.remove(stuff)
    counter()
def add(desc):
    global his
    global minus
    global plus
    global hlist
    try:
        if not desc:
            messagebox.showinfo("NOPE :)","No desc!")
        else:
            checkv = tk.BooleanVar(value=0)
            row = tk.Frame(hlist, bg="#ffffff")
            row.pack(fill="x",pady=2)
            cb = tk.Checkbutton(row,variable=checkv,command=counter,bg="#ffffff",font=("Noto Serif JP", 9, "bold"))
            cb.pack(side="left",padx=10)
            lb = tk.Label(row,text=desc,bg="#ffffff",font=("Noto Serif JP", 9, "bold"),wraplength=550,justify="left")
            lb.pack(side="left",padx=(8,0))
            hitems = {"name":desc,"checked":checkv,"frame":row}
            btn = tk.Button(row,text="Delete",command= lambda i=hitems: delt(i),font=("Noto Serif JP", 9, "bold"),bg = "#ff4242",fg="#ffffff")
            btn.pack(side="right",padx=10)
            habit.append(hitems)
            counter()
                    
    except Exception as E:
        messagebox.showinfo("WHATT :O","ERROR :?")
        
tk.Frame(h,bg = "#ffffff",padx=10,pady=10).place(x=20,y=120,width=250,height=150)
f2 = tk.Frame(h,bg = "#ffffff",padx=10,pady=10).place(x=280,y=120,width=250,height=150)
f3 = tk.Frame(h,bg = "#ffffff",padx=10,pady=10).place(x=540,y=120,width=250,height=150)
f4 = tk.Frame(h, bg="#ffffff", padx=10, pady=10)
f4.place(x=40, y=500, width=730, height=200)
f5 = tk.Frame(h,bg = "#ffffff",padx=10,pady=20)
f5.place(x=20,y=440,width=770,height=300)
canvas = tk.Canvas(f5,bg="#ffffff")
scrollbar = ttk.Scrollbar(f5, orient="vertical", command = canvas.yview)
hlist = tk.Frame(canvas, bg ="#ffffff")
hlist.bind("<Configure>", lambda e: canvas.configure(scrollregion=canvas.bbox("all")))
wid = canvas.create_window((0,0),window=hlist,anchor="nw")
canvas.bind("<Configure>", lambda c: canvas.itemconfigure(wid,width=c.width))
canvas.configure(yscrollcommand=scrollbar.set)
canvas.pack(side="left",fill="both",expand=True)
scrollbar.pack(side="right",fill="y")



tk.Label(h,font=('Noto Serif JP',30,'bold'),text="Habits...", bg = "#01004b",fg="white",justify="center").place(x=0,y=0,width=800,height=100)
tk.Label(h, text="Total", font=('Noto Serif JP', 10, 'bold'),bg = "#ffffff").place(x=20, y=130, height = 40, width = 100)
tk.Label(h, text="Completed", font=('Noto Serif JP', 10, 'bold'), bg = "#ffffff").place(x=280, y=130, height = 40, width = 100)
tk.Label(h, text="On progress", font=('Noto Serif JP', 10, 'bold'),bg="#ffffff").place(x=540, y=130, height = 40, width = 100)
tk.Label(h, text="Description", font=('Noto Serif JP', 8, 'bold'),bg="#e9edff").place(x=20, y=280, height = 40, width = 100)
tk.Label(h, textvariable=total, font=('Noto Serif JP', 8, 'bold'),bg="#ffffff",justify="left").place(x=20, y=200, height = 60, width = 100)
tk.Label(h, textvariable=completed, font=('Noto Serif JP', 8, 'bold'),bg="#ffffff",justify="left", fg = "green").place(x=280, y=200, height = 60, width = 100)
tk.Label(h, textvariable=ongoing, font=('Noto Serif JP', 8, 'bold'),bg="#ffffff",justify="left", fg = "red").place(x=540, y=200, height = 60, width = 100)
desc = tk.Entry(h, textvariable = description,font=('Noto Serif JP', 7, 'bold'))
desc.place(x=30, y=320, height =30, width =650)

progress = ttk.Progressbar(h,orient="horizontal",length=300,mode="determinate")
progress.place(x=30,y=400,height=20,width=650)
tk.Button(h,text="+",font=('Noto Serif JP',10,'bold'), command = lambda: add(desc.get()),bd="0",bg="#096215",fg="#fffefe").place(x = 690, y = 320, width = 80, height= 50)
tk.Label(h, text="Habit", font=('Noto Serif JP', 9, 'bold'),bg = "#ffffff").place(x=20, y=440, height =20, width = 100)
tk.Label(h, textvariable=prog, font=('Noto Serif JP', 9, 'bold'),bg="#e9edff",justify="left").place(x=680, y=400, height =20, width = 70)
h.mainloop()