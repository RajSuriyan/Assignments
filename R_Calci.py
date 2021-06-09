from tkinter import *
class tkeasy():
    
    def print_text(self,a,r,c,lpos):
        labelo=Label(root,text=str(a),font=("Helvictica",48))
        labelo.grid(row=r,column=c,sticky=lpos)

    
def add():
    try:
        a=int(e1.get())
        b=int(e2.get())
        c=a+b
    except:
        side=Tk()
        Toplevel()
        side.title('Error!')
        side.geometry("400x400")
        my_label=Label(side,text="You enterd a text!!",font=("Helvictica",34))
        my_label.grid(row=2,column=2)
        side.mainloop()
            
    my_label=Label(root,text="Ans="+str(c),fg="black",font=("Helvictica",34))
    my_label.grid(row=4,column=0)
def sub():
    try:
        a=int(e1.get())
        b=int(e2.get())
        c=a-b
    except:
        side=Tk()
        Toplevel()
        side.title('Error!')
        side.geometry("400x400")
        my_label=Label(side,text="You enterd a text!!",font=("Helvictica",34))
        my_label.grid(row=2,column=2)
        side.mainloop()
    my_label=Label(root,text="Ans="+str(c),fg="red",font=("Helvictica",34))
    my_label.grid(row=4,column=1)
def mul():
    try:
        a=int(e1.get())
        b=int(e2.get())
        c=a*b
    except:
        side=Tk()
        Toplevel()
        side.title('Error!')
        side.geometry("400x400")
        my_label=Label(side,text="You enterd a text!!",font=("Helvictica",34))
        my_label.grid(row=2,column=2)
        side.mainloop()
    my_label=Label(root,text="Ans="+str(c),fg="green",font=("Helvictica",34))
    my_label.grid(row=4,column=2)
def div():
    try:
        a=int(e1.get())
        b=int(e2.get())
        c=a/b
    except:
        side=Tk()
        Toplevel()
        side.title('Error!')
        side.geometry("400x400")
        my_label=Label(side,text="You enterd a text!! or You divided "+str(e1.get())+"/"+str(e1.get())+"not possible",font=("Helvictica",34))
        my_label.grid(row=2,column=2)
        side.mainloop()
    my_label=Label(root,text="Ans="+str(float(c)),fg="blue",font=("Helvictica",34))
    my_label.grid(row=4,column=3)
def rem():
    try:
        a=int(e1.get())
        b=int(e2.get())
        c=a%b
    except:
        side=Tk()
        Toplevel()
        side.title('Error!')
        side.geometry("400x400")
        my_label=Label(side,text="You enterd a text!! or You divided "+str(e1.get())+"%"+str(e1.get())+"not possible",font=("Helvictica",34))
        my_label.grid(row=2,column=2)
        side.mainloop()
    my_label=Label(root,text="Ans="+str(float(c)),fg="magenta",font=("Helvictica",34))
    my_label.grid(row=4,column=4)


root=Tk()

root.title('Calci 1.0.0')
root.geometry('1920x1080')


label1= Label(root,text="Enter a number:",font=("Helvictica",34)) #raised,groove,ridge,sunken=relief ,height and width can be added,
label1.grid(row=1,column=0,sticky="E")

#unit1
label2=Label(root,text="Enter another Number:",font=("Helvictica",34))
label2.grid(row=2,column=0)

#sticky east west north and south   #columnspan and rowspan
e1=Entry(root,font=("Helvictica",34))
e1.grid(row=1,column=1)



#entry widgets
e2=Entry(root,font=("Helvictica",34))
e2.grid(row=2,column=1)      
instances=tkeasy()
instances.print_text("R_Calculator",0,1,E)

button2=Button(root,text="Addition",font=("Helvictica",34),fg="black",command=add)
button2.grid(row=3,column=0,sticky="E")
button3=Button(root,text="Subtraction",font=("Helvictica",34),fg="red",command=sub)
button3.grid(row=3,column=1,sticky="E")
button31=Button(root,text="Multiplication",font=("Helvictica",34),fg="green",command=mul)
button31.grid(row=3,column=2)
button4=Button(root,text="Division",font=("Helvictica",34),fg="blue",command=div)
button4.grid(row=3,column=3,sticky="E")
button5=Button(root,text="Remainder",font=("Helvictica",34),fg="magenta",command=rem)
button5.grid(row=3,column=4,sticky="E")



root.mainloop()
