##import  sqlite3
##conn=sqlite3.connect (''ashika,db'');
##print("opened detabase created successfully");
##conn.execute('''CREATE TABLE USER ROLLNO INT NOT  NULL,NAME TEXT NOT NULL,ADDRESS CHART,
##SALARY REAL);''')
##print("table created succesfull")
##conn.close()
##
##from tkinter import*
##import sqlite3
##
##top=Tk()
##top.geometry('300x200')
##def add():
##    a=D1.get()
##    b=f.get()
##    c=g.get()
##    cursor.execute("insert into students values(?,?,?)"[a,b,c])
##    conn.commit()
##E1=Entry(top,bd=10)
##E.pack()
##E2=Entry(top,bd=11)
##E.pack()
##button=Button(top,text="insert",cammand=add)
##button.pack()
##conn=sqlite3.connect("abc.db")
##cursor=conn.cursor()
##cursor.execute("create table student if not exists(username txt,repassward text)" )
##print("database created")
##    
##


from tkinter import*
top=Tk()
top.geometry('400x300')
top.config(background='#333321')

l1=Label(top,text="Name")
l1.place(x=90,y=30)

l2=Label(top,text="age")
l2.place(x=100,y=50)


button=Button(top,text="add",pady=10,padx=10,command=add)
button.place(x=200,y=290)


title=Label(top,text="simple calculator",front=("Ink free',30),background='#title.place(x=50,y=50))
top.mainloop()



















