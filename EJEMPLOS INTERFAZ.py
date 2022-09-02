# -*- coding: utf-8 -*-
#!/usr/bin/env python
from Tkinter import *
import Tkinter as tk
import ttk
from ttk import *
import tkMessageBox

class Interfaz:
    def intergeneral_pag05(self):
        root = Tk()
        frm = tk.Frame(root, padx=10)
        frm.grid()
        tk.Label(frm, text="Hello World!").grid(column=0,row=0)
        tk.Button(frm, text="Quit", command=root.destroy).grid(column=1, row=0)
        root.mainloop()
    def primera_aplicacionGUI_pag12(self):
        #----VENTANA----
        window = Tk()
        window.title("Welcome to LikeGeeks app")
        window.mainloop()
    def widget_label_pag13(self):
        #----LABEL----
        window = Tk()
        window.title("Welcome to LikeGeeks app")
        lbl = Label(window, text="Hello")
        lbl.grid(column=0,row=0)
        window.mainloop()
    def widget_button_pag16(self):
        #----BUTTON----
        window = Tk()
        window.title("Welcome to LikeGeeks app")
        window.geometry('350x200')
        lbl = Label(window,text="Hello")
        lbl.grid(column=0, row=0)
        def clicked():
            lbl.configure(text="Button was clicked !!")
        btn = Button(window, text="Click Me", command=clicked)
        btn.grid(column=1, row=0)
        window.mainloop()
    def entry_textbox_pag20(self):
        #----ENTRY---
        window = Tk()
        window.title("Welcome to LikeGeeks app")
        window.geometry('350x200')
        lbl = Label(window,text="Hello")
        lbl.grid(column=0, row=0)
        txt = Entry(window, width=10)
        txt.grid(column=1, row=0)
        def clicked():
            res = "Welcome to " + txt.get()
            lbl.configure(text=res)
        btn = Button(window, text="Click Me",command=clicked)
        btn.grid(column=2,row=0)
        window.mainloop()
    def widget_combobox_pag24(self):
        #----COMBOBOX----
        window = Tk()
        window.title("Welcome to LikeGeeks app")
        window.geometry('350x200')
        combo = Combobox(window)
        combo['values'] = (1, 2, 3, 4, 5, "Text")
        combo.current(1)# set the selected item
        combo.grid(column=0, row=0)
        window.mainloop()
    def widget_checkbutton_pag26(self):
        #----CHECKBUTTON----
        window = Tk()
        window.title("Welcome to LikeGeeks app")
        window.geometry('350x200')
        chk_state = BooleanVar()
        chk_state.set(True)  # set check state
        chk = Checkbutton(window, text='Choose', var=chk_state)
        chk.grid(column=0, row=0)
        window.mainloop()
    def widget_radiobutton_pag28(self):
        #----RADIOBUTTON----
        window = Tk()
        window.title("Welcome to LikeGeeks app")
        selected = IntVar()
        rad1 = Radiobutton(window,text='First',value=1,variable=selected)
        rad2 = Radiobutton(window, text='Second', value=2,variable=selected)
        rad3 = Radiobutton(window, text='Third', value=3,variable=selected)
        def clicked():
            print(selected.get())
        btn = Button(window, text="Click Me", command=clicked)
        rad1.grid(column=0, row=0)
        rad2.grid( column=1, row=0)
        rad3.grid(column=2, row=0)
        btn.grid(column=3, row=0)
        window.mainloop()
    def messagebox_pag31(self):
        #----MESSAGEBOX----
        window = Tk()
        window.title("Welcome to LikeGeeks app")
        window.geometry('350x200')
        def clicked():
            tkMessageBox.showinfo('Message title', 'Message content')
        btn = Button(window,text='Click here',command=clicked)
        btn.grid(column=0,row=0)
        window.mainloop()
    def spinbox_pag33(self):
        #----SPINBOX----
        window = Tk()
        window.title("Welcome to LikeGeeks app")
        window.geometry('350x200')
        spin = Spinbox(window,from_=0,to=100,width=5)
        spin.grid(column=0, row=0)
        window.mainloop()
    def progressbar_pag36(self):
        #----PROGRESSBAR----
        window = Tk()
        window.title("Welcome to LikeGeeks app")
        window.geometry('350x200')
        style = ttk.Style()
        style.theme_use('default')
        style.configure("black.Horizontal.TProgressbar",background='black')
        bar = Progressbar(window, length=200, style='black.Horizontal.TProgressbar')
        bar['value'] = 70
        bar.grid(column=0,row=0)
        window.mainloop()
    def filemenu_pag38(self):
        #----FILEMENU----
        def donothing():
            filewin = Toplevel(root)
            button = Button(filewin, text="Do nothing button")
            button.pack()
        root = Tk()
        menubar = Menu(root)
        filemenu = Menu(menubar,tearoff=2)
        filemenu.add_command(label="New",command=donothing)
        filemenu.add_command(label="Open", command=donothing)
        filemenu.add_command(label="Save", command=donothing)
        filemenu.add_command(label="Save as...", command=donothing)
        filemenu.add_command(label="Close", command=donothing)

        filemenu.add_separator()

        filemenu.add_command(label="Exit", command=root.quit)
        menubar.add_cascade(label="File", menu=filemenu)
        editmenu = Menu(menubar, tearoff=0)
        editmenu.add_command(label="Undo",command=donothing)

        editmenu.add_separator()

        editmenu.add_command(label="Cut", command=donothing)
        editmenu.add_command(label="Copy", command=donothing)
        editmenu.add_command(label="Paste", command=donothing)
        editmenu.add_command(label="Delete",command=donothing)
        editmenu.add_command(label="Select All", command=donothing)
        menubar.add_cascade(label="Edit", menu=editmenu)
        helpmenu = Menu(menubar, tearoff=0)
        helpmenu.add_command(label="Help Index", command=donothing)
        helpmenu.add_command(label="About...",command=donothing)
        menubar.add_cascade(label="Help", menu=helpmenu)
        root.config(menu=menubar)
        root.mainloop()
    def tabla_pag41(self):
        #----TABLA----
        root = Tk()
        height = 5
        width = 5
        for i in range(height): # Rows
            for j in range(width): #Columns
                b = Entry(root, text="")
                b.grid(row=i, column=j)
        mainloop()
    def canvas_pag42(self):
        #----CANVAS----
        master = Tk()
        w = Canvas(master, width=200, height=100)
        w.pack()
        w.create_line(0, 0, 200, 100)
        w.create_line(0, 100, 200, 0, fill="red", dash=(4, 4))
        w.create_rectangle(50, 25, 150, 75, fill="blue")
        mainloop()
inter=Interfaz()
#inter.intergeneral_pag05()
#inter.primera_aplicacionGUI_pag12()
#inter.widget_label_pag13()
#inter.widget_button_pag16()
#inter.entry_textbox_pag20()
#inter.widget_combobox_pag24()
#inter.widget_checkbutton_pag26()
#inter.widget_radiobutton_pag28()
#inter.messagebox_pag31()
#inter.spinbox_pag33()
#inter.progressbar_pag36()
#inter.filemenu_pag38()
#inter.tabla_pag41()
#inter.canvas_pag42()