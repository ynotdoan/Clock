
import tkinter as tk


class Window(tk.Tk):
  '''
  Builds GUI for app.
  '''
  def __init__(self):
    super(Window, self).__init__()
    self.title("Clock App")
    self.minsize(1200, 700) # width x height
    
    self.bg()
    
    
  def bg(self):
    self.configure(background = "black")