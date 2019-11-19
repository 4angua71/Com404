from tkinter import *
from tkinter import messagebox

class Gui(Tk):
    
    def __init__(self):
        super().__init__()
        
        # set window attributes
        self.title("Tickets")
        
        # add components
        self.__add_heading_label()
        self.__add_instruction_label()
        self.__add_tickets_entry()
        self.__add_buy_button()
        
        
    def __add_heading_label(self):
        
        self.heading_label = Label()
        self.heading_label.grid(row=1, column=0)
           
        # style
        self.heading_label.configure(font="Arial 9",text="Entrance Ticket:")
        
    def __add_instruction_label(self):
        self.instruction_label = Label()
        self.instruction_label.grid(row=2, column=0, sticky=W)
        
        # style
        self.instruction_label.configure(font="Arial 9",text="How many tickets are needed?")
        
    def __add_tickets_entry(self):
        self.ticket_entry = Entry()
        self.ticket_entry.grid(row=3, column=0)
        
        # style
        self.ticket_entry.configure(bg = "#fff", relief = SUNKEN, width = 30)
        
    def __add_buy_button(self):
        self.buy_button = Button()
        self.buy_button.grid(row=4, column=0)
        
        # style
        self.buy_button.configure(font="Arial 8",text="Buy" )
        # events
        self.buy_button.bind("<ButtonRelease-1>", self.__buy_button_clicked)
    
    def __buy_button_clicked(self, event):
        if (int(self.ticket_entry.get()) == 1):
            messagebox.showinfo("Purchased!","You have purchased 1 ticket")
        elif (int(self.ticket_entry.get()) > 1):
            messagebox.showinfo("Purchased!","You have purchased " + self.ticket_entry.get() + " tickets!")
        else:
            messagebox.showinfo("Purchased!","You have entered an invalid number of tickets!" )