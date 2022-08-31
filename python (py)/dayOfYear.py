from tkinter import Tk, Label, Button, Entry
from tkinter.font import Font, families
from tkinter import *

class Root(Tk):
   def __init__(self):
       super().__init__()
       self.titleLabel= Label(self,text="Math Day Of Year:\nCreator:Mohammad Mahdi Ranjbar\nGithub:\nTelegram:https://t.me/Devsrc",bg="#000000",fg="#00ffff")
       self.titleLabel.pack()

       self.uLabel=Label(self,text="")
       self.uLabel.pack()

       self.uLabel=Label(self,text="Day:",bg="black",fg="#00ffff")
       self.uLabel.pack()

       self.dEntry=Entry(self,width=100,bg="#000000",fg="#00fe0d",border="10")
       self.dEntry.pack()

       self.uLabel=Label(self,text="")
       self.uLabel.pack()

       self.uLabel=Label(self,text="Month:",bg="#000000",fg="#00ffff")
       self.uLabel.pack()

       self.mEntry=Entry(self,width=100,bg="#000000",fg="#00fe0d",border="10")
       self.mEntry.pack()

       self.uLabel=Label(self,text=" ")
       self.uLabel.pack()

       self.button=Button(self,text="Math",width=40,command=self.onclick,border="10",bg="black",fg="#00ffff")
       self.button.pack()

       self.Label=Label(self,text="Output:",font=20,bg="#000000",fg="yellow")
       self.Label.pack()

   def onclick (self):
       d=int(self.dEntry.get())
       m=int(self.mEntry.get())

       if 1<=m and m<=6 :
           day=(m-1)*31+d
           self.Label.configure(text=f"Output:{day} Day",background="green")

       elif 7<=m and m<=12:
           day=(m-1)*30+6+d
           self.Label.configure(text=f"Output:{day} Day",background="green")
       else:
           self.Label.configure(text=f"Output:Error",background="red")
root=Root()
root.configure(bg='#000000')
root.minsize(width=400,height=400)
root.title("Day OF Year")
root.mainloop()
