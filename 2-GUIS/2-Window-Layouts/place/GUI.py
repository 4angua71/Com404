from tkinter import *

class Gui(Tk):
  def __init__(self):
    super().__init__()

     # set window attributes
    self.title("Newsletter")
    self.configure(bg="#ddd",
                   height=174, 
                   width=335)
    
    self.add_canvas() 
    
    self.add_heading_label()
    
    self.add_main_label()
    
    self.add_email_label()

    self.add_email_entry()

    self.add_email_button()




  def add_heading_label(self):
    # create   
    self.heading_label = Label()
    self.heading_label.place(x=30, y=20)
    
    # style
    self.heading_label.configure(font="Arial 14",
                                 text="RECEIVE OUR NEWSLETTER")

  def add_main_label(self):
    # create   
    self.main_label = Label()
    self.main_label.place(x=12, y=62)
    
    # style
    self.main_label.configure(font="Arial 9",
                                 text="Please enter your email below to recieve our newsletter.")

  def add_email_label(self):
    # create   
    self.email_label = Label()
    self.email_label.place(x=30, y=105)
    
    # style
    self.email_label.configure(font="Arial 9",
                                 text="Email:")
  
  def add_email_button(self):
    # create   
    self.email_button = Button()
    self.email_button.place(x=10, y=140)
    
    # style
    self.email_button.configure(font="Arial 8",text="Subscribe:",relief = RAISED, height=1, width=51, bg = "pink")

  def add_canvas(self):
    # create   
    self.canvas = Canvas()
    self.canvas.place(x=8, y=8)
    
    # style
    self.canvas.configure(bg= "#eee", height=154, width=315)
  
  def add_email_entry(self):
    # create   
    self.email_entry = Entry()
    self.email_entry.place(x=75, y=105)
    
    # style
    self.email_entry.configure(bg = "#fff", relief = SUNKEN, width = 30)

    # add window components by
    # ...creating an object of the component stored in an attribute
    # ...setting the attributes of the component using the attribute
    # ...assigning any event handlers to the component

  # handle events
  # (callback functions to handle events will go here)