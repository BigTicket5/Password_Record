from  tkinter import *
root = Tk()

def hello():
    print("Hello,World!")

def about():
    w = Label(root,text="Developer list\n Jackie")
    w.pack(side=TOP)
    
#create menu
menubar =  Menu(root)

filemenu  = Menu(menubar,tearoff=0)
filemenu.add_command(label='Open',command=hello)
filemenu.add_command(label='Save',command=hello)
filemenu.add_separator()
filemenu.add_command(label='Exit',command=root.quit)
menubar.add_cascade(label='File',menu=filemenu)

editmenu  = Menu(menubar,tearoff=0)
editmenu.add_command(label='Cut',command=hello)
editmenu.add_command(label='Copy',command=hello)
editmenu.add_command(label='Paste',command=hello)
menubar.add_cascade(label='Edit',menu=editmenu)

helpmenu = Menu(menubar,tearoff=0)
helpmenu.add_command(label='About',command=about)
menubar.add_cascade(label='Help',menu=helpmenu)


root.config(menu=menubar)
root.mainloop()