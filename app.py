
import tkinter as tk


class Window(tk.Tk):
  '''
  Builds GUI for app.
  '''
  def __init__(self):
    tk.Tk.__init__(self)
    self.title("Clock App")
    self.minsize(1200, 700) # width x height
    self.configure(background = "black")
    
    Clock()
    
    
class Clock(tk.Frame):
  '''
  Frame to display clock showing current time.
  '''
  def __init__(self):
    tk.Frame.__init__(self)
    self.configure(background = "blue", width = 50, height = 50)
    self.pack(side = "right", padx = 10)