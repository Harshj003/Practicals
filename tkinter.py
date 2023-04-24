#program 1
from tkinter import *
top = Tk()
top.title("SE-IT 17104074")
c = Canvas(top,bg="blue",height=1000,width=1000)
fnt = ('Times','22','bold italic underline')
text = c.create_text(250,40,text="My First Tkinter Application on canvas",font=fnt,fill="red",activefill="cyan3")
line = c.create_line(80,80,200,80,200,200,width=6,fill="cyan3") line = c.create_line(80,80,300,80,300,300,width=6,fill="cyan3") oval =
c.create_oval(120,120,400,300,width=6,fill="red",outline="green",activefill="cyan 3")
poly = c.create_polygon(320,320,320,420,420,320,width=6,fill="yellow",outline="green", activefill="cyan3")

rect = c.create_rectangle(360,460,550,550,width=6,fill="green",outline="green",activefill
="cyan3")
arc = c.create_arc(500,100,600,300,start=0,extent=180,width=6,outline="green",style=" arc")
file1=PhotoImage(file="python.png",height=300,width=300) file2=PhotoImage(file="Java.png",height=300,width=300) id=c.create_image(300,400,anchor=NE,image=file1,activeimage=file2)
c.pack() 
top.mainloop()

#program 2
from tkinter import * 
import tkinter as tk
fields = 'Last Name', 'First Name', 'DOB(mm/dd/yy)', 'email','Mobile No','Address','City','Pincode','State','Country'

def fetch(entries,v):

for entry in entries:

field = entry[0]

text = entry[1].get() print('%s: "%s"' % (field, text))
if v==1:

print('gender: Male') elif v==2:
print('gender: Female') def makeform(root, fields):
entries = []

for field in fields:

row = Frame(root)
 

lab = Label(row, width=15, text=field, anchor='w') ent = Entry(row)
row.pack(side=TOP, fill=X, padx=5, pady=5) lab.pack(side=LEFT)
ent.pack(side=RIGHT, expand=YES, fill=X) entries.append((field, ent))
return entries

if  name	== '   main    ':

root = tk.Tk()

root.title("APSIT-Student Registration Form")



ents = makeform(root, fields)

root.bind('<Return>', (lambda event, e=ents: fetch(e))) b1 = Button(root, text='Show',
command=(lambda e=ents: fetch(e,v.get()))) b1.pack(side=LEFT, padx=5, pady=5)
b2 = Button(root, text='Quit', command=root.quit) b2.pack(side=LEFT, padx=5, pady=5)
v = tk.IntVar()

tk.Label(root, text="""Gender""",justify = tk.LEFT,padx = 20).pack() tk.Radiobutton(root, text="male",padx = 20, variable=v, value=1).pack(anchor=tk.W) tk.Radiobutton(root, text="female",padx = 20, variable=v,value=2).pack(anchor=tk.W) root.mainloop()
