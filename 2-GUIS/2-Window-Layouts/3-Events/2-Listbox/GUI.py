from tkinter import *


class Gui(Tk):
    
    def __init__(self):
        super().__init__()
        
        # set window attributes
        self.title("Song Maker")
        
        # add components
        self.__add_heading_label()
        self.__add_instruction_label1()
        self.__add_lyric_frame()
        self.__add_lyric_entry()
        self.__add_lyric_button()
        self.__add_instruction_label2()
        self.__add_lyric_scrollbar()

        
        
    def __add_heading_label(self):
        
        self.heading_label = Label()
        self.heading_label.grid(row=0, column=0)
           
        # style
        self.heading_label.configure(font="Arial 9",text="Song Maker")
        
    def __add_instruction_label1(self):
        self.instruction_label1 = Label()
        self.instruction_label1.grid(row=1, column=0, sticky=W)
        
        # style
        self.instruction_label1.configure(font="Arial 9",text="Lyric to add:")
        
    def __add_lyric_frame(self):
        self.lyric_frame = Frame()
        self.lyric_frame.grid(row=2, column = 0)
    
    def __add_lyric_entry(self):
        self.lyric_entry = Entry(self.lyric_frame)
        self.lyric_entry.pack(side=LEFT)
    
    def __add_lyric_button(self):
        self.lyric_button = Button(self.lyric_frame)
        self.lyric_button.pack(side=RIGHT)
        # style
        self.lyric_button.configure(font="Arial 8",text="Add" )
   
    def __add_instruction_label2(self):
        self.instruction_label2 = Label()
        self.instruction_label2.grid(row=3, column=0, sticky=W)
        
        # style
        self.instruction_label2.configure(font="Arial 9",text="Lyrics:")
    
    def __add_lyric_scrollbar(self):
        self.lyric_scrollbar = Scrollbar()
        self.lyric_scrollbar.grid(row=4, column=0,)


scrollbar = Scrollbar(self)
scrollbar.pack( side = RIGHT, fill = Y )

mylist = Listbox(self, yscrollcommand = scrollbar.set )
for line in range(100):
   mylist.insert(END, "This is line number " + str(line))

mylist.pack( side = LEFT, fill = BOTH )
scrollbar.config( command = mylist.yview )
        
