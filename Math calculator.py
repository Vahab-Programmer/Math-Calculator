from tkinter import *
from turtle import RawTurtle
from sys import maxsize
def inside(x:int) -> int:return (x-2)*180 if x else 0
def inside_one(x:int) -> int:return inside(x)//x if x else 0
def out_one(x:int) -> int:return 180-inside_one(x) if x else 0
def side(x:int) -> int:return 360//(180-x) if x else 0
def calc_angles() -> None:
    if sides.get() <=2:
        angles.set(0)
        angle.set(0)
        out_angle.set(0)
        sides.set(0)
    try:
        angles.set(inside(sides.get()))
        angle.set(inside_one(sides.get()))
        out_angle.set(out_one(sides.get()))
        pointer.forward(1)
        canvas.delete("all")
        canvas.delete("all")
        create_shape()
    except TclError:
        angles.set(0)
        angle.set(0)
        out_angle.set(0)
        sides.set(0)
def calc_side() -> None:
    if angle.get() >=180:
        angles.set(0)
        angle.set(0)
        out_angle.set(0)
        sides.set(0)
    try:
        sides.set(side(angle.get()))
        angles.set(angle.get()*sides.get())
        out_angle.set(out_one(sides.get()))
        pointer.forward(1)
        canvas.delete("all")
        canvas.delete("all")
        create_shape()
    except TclError:
        angles.set(0)
        angle.set(0)
        out_angle.set(0)
        sides.set(0)
def create_shape() -> None:
    if sides.get() > 100 or sides.get() <=2:
        return None
    pointer.setheading(360)
    pointer.penup()
    pointer.goto(-30, 65)
    pointer.pendown()
    tside=sides.get()
    out=out_one(tside)
    for i in range(tside):
        pointer.forward(out)
        pointer.right(out)
def delete_divisible(num: int, number_list:set):
    result = number_list
    for v in number_list:
        if not v % num and v !=num:
            result.remove(v)
    return result
def calc_prime() -> None:
    global numbers
    max_n=max_num.get()
    min_n=min_num.get()
    tnumbers = list(range(1, max_n + 1))
    tnumbers.remove(1)
    for i in range(1, max_n + 1):
        multiply = int()
        if not i in tnumbers:
            continue
        for x in range(1, i + 1):
            if not i in tnumbers:
                continue
            if not i % x:
                multiply += 1
        if multiply == 2:
            tnumbers = delete_divisible(i, tnumbers)
    result = list()
    for b in tnumbers:
        if b > min_n:
            result.append(str(b))
            result.append(",")
    result.pop(-1)
    numbers.set("".join(result))
f=("Tahoma",11)
root=Tk()
root.title("Math Calculator")
root.geometry("500x400+400+150")
root.resizable(False,False)
frame1=Frame(root,width=485,height=190,borderwidth=2,relief="raised")
frame2=Frame(root,width=485,height=155,borderwidth=2,relief="raised")
frame1.place(x=8,y=2)
frame2.place(x=8,y=195)
canvas=Canvas(frame1,bg="white",width=245,height=178)
canvas.place(x=230,y=1)
pointer=RawTurtle(canvas,visible=False)
pointer.speed("fastest")
sides=IntVar(master=frame1)
angles=IntVar(master=frame1)
angle=IntVar(master=frame1)
out_angle=IntVar(master=frame1)
min_num=IntVar(master=frame2)
max_num=IntVar(master=frame2)
numbers=StringVar(master=frame2)
Button(frame1,text="Calculate Angles",command=calc_angles,width=23,font=f).place(x=10,y=115)
Button(frame1,text="Calculate Side",command=calc_side,width=23,font=f).place(x=10,y=150)
Button(frame2,text="Calculate Prime Numbers",command=calc_prime,width=57,font=f).place(x=8,y=100)
Spinbox(frame1,textvariable=sides,from_=3,to=100).place(x=80,y=10)
Entry(frame1,textvariable=angles,state="readonly").place(x=80,y=35)
Spinbox(frame1,textvariable=angle,from_=60,to=179).place(x=80,y=60)
Entry(frame1,textvariable=out_angle,state="readonly").place(x=80,y=85)
Spinbox(frame2,textvariable=min_num,from_=1,to=maxsize).place(x=80,y=65)
Spinbox(frame2,textvariable=max_num,from_=1,to=maxsize).place(x=295,y=65)
e1=Entry(frame2,textvariable=numbers,width=76)
s1=Scrollbar(frame2,command=e1.xview,orient="horizontal")
e1.config(xscrollcommand=s1.set)
e1.place(x=10,y=15)
s1.place(x=10,y=33,relwidth=0.955)
Message(frame1,text="sides",font=f,width=99).place(x=18,y=7)
Message(frame1,text="angles",font=f,width=99).place(x=13,y=29)
Message(frame1,text="angle",font=f,width=99).place(x=18,y=55)
Message(frame1,text="out angle",font=("tahoma",10),width=99).place(x=12,y=82)
Message(frame2,text="maximum:",font=("tahoma",10),width=99).place(x=220,y=62)
Message(frame2,text="minimum:",font=("tahoma",10),width=99).place(x=8,y=62)
Message(root,text="Programmed By Vahab GithubPage:http://Github.com/vahab-programmer",font=("tahoma",10),width=999).place(x=24,y=360)
pointer.forward(1)
canvas.delete("all")
root.mainloop()