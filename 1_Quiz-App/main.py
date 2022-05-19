from tkinter import*
from tkinter import messagebox as m
import mysql.connector
from turtle import *
import os
from operator import itemgetter


#loading_bar

def loading_bar():
    title("Quiz Application")
    s = ("Impact", "15")
    color("orange")
    write("Quiz App", font=s, align="center")
    color("orange")

    begin_fill()
    bgcolor("black")
    shape("square")
    speed(2)
    forward(200)
    right(90)
    forward(20)
    right(90)
    forward(200)
    end_fill()

    begin_fill()
    color("grey")
    forward(200)
    right(90)
    forward(20)
    right(90)
    forward(200)
    end_fill()
    forward(200)
    right(90)
    forward(20)
    right(90)
    forward(400)
loading_bar()
os.system("cls")




# login part
root = Tk()
root.title("Quiz Application")
root.geometry("655x333")

# msql connector
con = mysql.connector.connect(host="localhost", user="root", password="", database="quiz_app")
cursor = con.cursor()

conn = mysql.connector.connect(host="localhost", user="root", password="", database="quiz_app")
cursor2 = conn.cursor()


#login_area
l = Label(root, text="Login Area", fg="orange", font="Impact 12")
l.place(x=50, y=10)

#user name
user = Label(root, text="User Name")
user.place(x=20, y=40)

u = StringVar()
ue = Entry(root, borderwidth=1, textvariable=u)
ue.place(x=20, y=60)

#password
password = Label(root, text="Password")
password.place(x=20, y=90)

p = StringVar()
pe = Entry(root, borderwidth=1, textvariable=p)
pe.place(x=20, y=110)



#login
def check():

    sqlCommand1 = "select username from register"
    sqlCommand2 = "select password from register"

    cursor.execute(sqlCommand1)
    cursor2.execute(sqlCommand2)


    global ue
    username = ue.get()

    global pe
    password = pe.get()

    us = []
    ps = []

    for i in cursor:
        us.append(i)
    for j in cursor2:
        ps.append(j)

    res = list(map(itemgetter(0), us))
    res2 = list(map(itemgetter(0), ps))

    k = len(res)
    i = 1
    while i<k:
        if res[i]==username and res2[i]==password:
            m.showinfo(title="Done", message="successfully you logged")
            break
        i+=1

        manu = Tk()
        manu.title("Quiz Application")
        manu.geometry("655x333")

        f = Frame(manu, bg="white", padx=120, pady=80)

        # choose option
        l = Label(f, text="Choose A Option", font="Impact 13", fg="orange", bg="white")
        l.grid(pady=20, padx=2)

        # python
        def python():
            manu.destroy()
            f2 = Tk()
            f2.title("Python Question")
            f2.geometry("655x333")

            # python question -1
            l = Label(f2, text="1.When python started?", fg="black")
            l.grid(row=0, column=0, pady=20, padx=2)

            def right():
                l5 = Label(f2, text="right answer!", fg="green", bg="white", padx=90)
                l5.place(x=20, y=100)

            b1 = Button(f2, text="a.1989", bg="orange", bd=0, command=right)
            b1.grid(row=1, column=0, pady=5, padx=5)

            def wrong():
                l5 = Label(f2, text="wrong answer!", fg="red", bg="white", padx=80)
                l5.place(x=20, y=100)

            b2 = Button(f2, text="b.1980", bg="orange", bd=0, command=wrong)
            b2.place(x=120, y=65)

            f2.mainloop()

        python = Button(f, text="Python", bg="orange", pady=5, padx=50, bd=0, command=python)
        python.grid(row=1, column=0)

        # java
        # question

        def java():
            manu.destroy()
            f2 = Tk()
            f2.title("Java Question")
            f2.geometry("655x333")

            # java question -1
            l = Label(f2, text="1.When java started?", fg="black")
            l.grid(row=0, column=0, pady=20, padx=2)

            def right():
                l5 = Label(f2, text="right answer!", fg="green", bg="white", padx=90)
                l5.place(x=20, y=100)

            def wrong():
                l5 = Label(f2, text="wrong answer!", fg="red", bg="white", padx=80)
                l5.place(x=20, y=100)

            b1 = Button(f2, text="a.1989", bg="orange", bd=0, command=wrong)
            b1.grid(row=1, column=0, pady=5, padx=5)

            b2 = Button(f2, text="b.1995", bg="orange", bd=0, command=right)
            b2.place(x=120, y=65)

            f2.mainloop()

        java = Button(f, text="Java", bg="orange", pady=5, padx=60, bd="0", command=java)
        java.grid(row=1, column=1, padx=2)

        # c programm

        # c question
        def cp():
            manu.destroy()
            f2 = Tk()
            f2.title("C Program Question")
            f2.geometry("655x333")

            # java question -1
            l = Label(f2, text="1.When c program started?", fg="black")
            l.grid(row=0, column=0, pady=20, padx=2)

            def right():
                l5 = Label(f2, text="right answer!", fg="green", bg="white", padx=90)
                l5.place(x=20, y=100)

            def wrong():
                l5 = Label(f2, text="wrong answer!", fg="red", bg="white", padx=80)
                l5.place(x=20, y=100)

            b1 = Button(f2, text="a.1989", bg="orange", bd=0, command=wrong)
            b1.grid(row=1, column=0, pady=5, padx=5)

            b2 = Button(f2, text="b.1972", bg="orange", bd=0, command=right)
            b2.place(x=120, y=65)

            f2.mainloop()

        c = Button(f, text="C", bg="orange", pady=5, padx=65, bd="0", command=cp)
        c.grid(row=2, column=0, padx=2)

        # C++ programm

        def cp2():
            manu.destroy()
            f2 = Tk()
            f2.title("C Program Question")
            f2.geometry("655x333")

            # java question -1
            l = Label(f2, text="1.When c program started?", fg="black")
            l.grid(row=0, column=0, pady=20, padx=2)

            def right():
                l5 = Label(f2, text="right answer!", fg="green", bg="white", padx=90)
                l5.place(x=20, y=100)

            def wrong():
                l5 = Label(f2, text="wrong answer!", fg="red", bg="white", padx=80)
                l5.place(x=20, y=100)

            b1 = Button(f2, text="a.1989", bg="orange", bd=0, command=wrong)
            b1.grid(row=1, column=0, pady=5, padx=5)

            b2 = Button(f2, text="b.1979", bg="orange", bd=0, command=right)
            b2.place(x=120, y=65)

            f2.mainloop()

        c = Button(f, text="C++", bg="orange", pady=5, padx=59, bd=0, command=cp2)
        c.grid(row=2, column=1, padx=2, pady=2)

        f.grid(pady=40, padx=40)
        manu.mainloop()

        break



    else:
        m.showerror(title="error", message="no account found")

login = Button(root, text="Login", bg="orange", padx=20, bd=0, command=check)
login.place(x=45, y=135)


#register part
you = Label(root, text="don't have any account?", fg="blue")
you.place(x=16, y=170)

def new_account():
        root.destroy()
        account = Tk()
        account.geometry("655x333")
        account.title("Quiz Application")

        con = mysql.connector.connect(host="localhost", user="root", password="", database="quiz_app")
        cursor = con.cursor()



        # join  quiz
        join = Label(account, text="Join quiz app", fg="orange", font="Impact 12")
        join.place(x=50, y=10)

        # set user name
        user = Label(account, text="set user name")
        user.place(x=20, y=40)

        global ue
        ue = Entry(account, borderwidth=1)
        ue.place(x=20, y=60)

        # set password
        password = Label(account, text="set new password")
        password.place(x=20, y=80)

        global pe
        pe = Entry(account, borderwidth=1)
        pe.place(x=20, y=100)

        # confirm password
        confirm = Label(account, text="confirm password")
        confirm.place(x=20, y=120)

        global ce
        ce = Entry(account, borderwidth=1)
        ce.place(x=20, y=140)

        # message show
        def error():
                m.showerror(title="error", message="password not matched")

        # insertion part of database
        def insert1():
                create = "insert into register (username,password,confirmpassword) values (%s,%s,%s)"
                values = [ue.get(), pe.get(), ce.get()]
                cursor.execute(create, values)
                if pe.get() == ce.get():
                        con.commit()
                        m.showinfo(title="Done", message="Account Created")
                else:
                        error()
                con.commit()

        #CREATE ACCOUNT
        caccount = Button(account, text="create", bg="orange", padx=20, bd=0, command=insert1)
        caccount.place(x=40, y=165)


create = Button(root, text="cliclk here", fg="orange", bd=0, command=new_account)
create.place(x=15, y=193)


root.mainloop()