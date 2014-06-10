'''
Created on 2014-6-10

@author: JMao
'''
from tkinter import BOTH,Frame,RIGHT, RAISED
from tkinter.ttk import Style,Button
class PwRd(Frame):
    def __init__(self,parent):
        Frame.__init__(self, parent,background="white")
        self.parent = parent
        self.initUI()
        
    def initUI(self):
        self.parent.title("Start")
        self.style=Style()
        self.style.theme_use("default")
        frame = Frame(self,relief=RAISED,borderwidth=1,background="white")
        frame.pack(fill=BOTH, expand=1)
        self.pack(fill=BOTH, expand=1)
        closeButton = Button(self, text="Close",command=self.quit)
        closeButton.pack(side=RIGHT, padx=5, pady=5)
        okButton = Button(self, text="OK")
        okButton.pack(side=RIGHT)
        
