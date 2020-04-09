import os
import pickle
import sys
import sqlite3 as sql
try:
    from Tkinter import *
except ImportError:
    from tkinter import *

try:
    import ttk
    py3 = False
except ImportError:
    import tkinter.ttk as ttk
    py3 = True

class HOTEL_MANGMENT_checkin:
    def __init__(self):
        root = Tk()
       
        _bgcolor = '#d9d9d9'  # X11 color: 'gray85'
        _fgcolor = '#000000'  # X11 color: 'black'
        _compcolor = '#ffffff' # X11 color: 'white'
        _ana1color = '#ffffff' # X11 color: 'white'
        _ana2color = '#ffffff' # X11 color: 'white'
        font11 = "-family {Segoe UI} -size 17 -weight bold -slant "  \
            "roman -underline 0 -overstrike 0"
        font14 = "-family {Times New Roman} -size 16 -weight bold " \
                 "-slant roman -underline 0 -overstrike 0"

        root.geometry("780x541+504+123")
        root.title("Room Details")
        root.configure(background="#ffffff")
        root.configure(highlightbackground="#ffffff")
        root.configure(highlightcolor="black")
        l2=[];
        G=[];
        cnx = sql.connect('project.sqlite')
        c=cnx.cursor()
        c.execute("SELECT RoomNo,Type FROM room")
        result=c.fetchall()
        for row in result:
            l2.append(row[0])
            G.append(row[1])
            

        self.Labelframe1 = LabelFrame(root)
        self.Labelframe1.place(relx=0.01, rely=0.04, relheight=0.95, relwidth=0.97)
        self.Labelframe1.configure(relief=GROOVE)
        self.Labelframe1.configure(font=font11)
        self.Labelframe1.configure(foreground="black")
        self.Labelframe1.configure(text='''ROOM CATEGORIES''')
        self.Labelframe1.configure(background="#93e6ad")
        self.Labelframe1.configure(highlightbackground="#93e6ad")
        self.Labelframe1.configure(highlightcolor="black")
        self.Labelframe1.configure(width=760)

        self.Frame1 = Frame(self.Labelframe1)
        self.Frame1.place(relx=0.03, rely=0.1, relheight=0.86, relwidth=0.47, y=-31, h=15)
        self.Frame1.configure(relief=GROOVE)
        self.Frame1.configure(borderwidth="2")
        self.Frame1.configure(relief=GROOVE)
        self.Frame1.configure(background="#83fa57")
        self.Frame1.configure(highlightbackground="#83fa57")
        self.Frame1.configure(highlightcolor="black")
        self.Frame1.configure(width=355)

        self.Label1 = Label(self.Frame1)
        self.Label1.place(relx=0.28, rely=0.02, height=37, width=117)
        self.Label1.configure(activebackground="#83fa57")
        self.Label1.configure(activeforeground="black")
        self.Label1.configure(background="#83fa57")
        self.Label1.configure(disabledforeground="#83fa57")
        self.Label1.configure(font=font11)
        self.Label1.configure(foreground="#000000")
        self.Label1.configure(highlightbackground="#83fa57")
        self.Label1.configure(highlightcolor="black")
        self.Label1.configure(text='''TYPE''')

        self.Text1 = Text(self.Frame1)
        self.Text1.place(relx=0.06, rely=0.16, relheight=0.8, relwidth=0.88)
        self.Text1.configure(background="#dfff40")
        self.Text1.configure(font=font14)
        self.Text1.configure(foreground="#000000")
        self.Text1.configure(highlightbackground="#dfff40")
        self.Text1.configure(highlightcolor="black")
        self.Text1.configure(insertbackground="black")
        self.Text1.configure(selectbackground="#dfff40")
        self.Text1.configure(selectforeground="black")
        self.Text1.configure(width=314)
        self.Text1.configure(wrap=WORD)



        self.Frame2 = Frame(self.Labelframe1)
        self.Frame2.place(relx=0.51, rely=0.1, relheight=0.86, relwidth=0.47, y=-31, h=15)
        self.Frame2.configure(relief=GROOVE)
        self.Frame2.configure(borderwidth="2")
        self.Frame2.configure(relief=GROOVE)
        self.Frame2.configure(background="#83fa57")
        self.Frame2.configure(highlightbackground="#83fa57")
        self.Frame2.configure(highlightcolor="black")
        self.Frame2.configure(width=355)

        self.Label2 = Label(self.Frame2)
        self.Label2.place(relx=0.37, rely=0.02, height=44, width=152)
        self.Label2.configure(activebackground="#83fa57")
        self.Label2.configure(activeforeground="black")
        self.Label2.configure(background="#83fa57")
        self.Label2.configure(disabledforeground="#a3a3a3")
        self.Label2.configure(font=font11)
        self.Label2.configure(foreground="#000000")
        self.Label2.configure(highlightbackground="#83fa57")
        self.Label2.configure(highlightcolor="black")
        self.Label2.configure(text='''ROOM NO.''')

        self.Text2 = Text(self.Frame2)
        self.Text2.place(relx=0.06, rely=0.16, relheight=0.8, relwidth=0.88)
        self.Text2.configure(background="#dfff40")
        self.Text2.configure(font=font14)
        self.Text2.configure(foreground="black")
        self.Text2.configure(highlightbackground="#dfff40")
        self.Text2.configure(highlightcolor="black")
        self.Text2.configure(insertbackground="black")
        self.Text2.configure(selectbackground="#dfff40")
        self.Text2.configure(selectforeground="black")
        self.Text2.configure(width=314)
        self.Text2.configure(wrap=WORD)
        for i in range(0,len(G)):
            s=str(l2[i])
            h=str(G[i])
            self.Text1.insert(INSERT,s+"\n")
            self.Text2.insert(INSERT,h+"\n")


        root.mainloop()


if __name__ == '__main__':
   
    hotel=HOTEL_MANGMENT_checkin()
