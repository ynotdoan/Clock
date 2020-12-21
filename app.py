
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
    
    TabButtons()
    
    
class Clock(tk.Frame):
  '''
  Frame to display clock showing current time.
  '''
  def __init__(self):
    tk.Frame.__init__(self)
    self.configure(background = "blue", width = 50, height = 50)
    self.pack(side = "right", padx = 10)
    
    
class Timer(tk.Frame):
  '''
  Frame to display timer.
  '''
  def __init__(self):
    tk.Frame.__init__(self)
    self.configure(background = "orange", width = 50, height = 50)
    self.pack(side = "right", padx = 10)
      
      
class TabButtons():
  def __init__(self):
    clock_button = tk.Button(text = "Clock", 
                             background = "pink", 
                             width = 10, 
                             command = lambda: Clock())
    clock_button.place(x = 10, y = 10)
    
    timer_button = tk.Button(text = "Timer", 
                             background = "green", 
                             width = 10, 
                             command = lambda: Timer())
    timer_button.place(x = 10, y = 45)
