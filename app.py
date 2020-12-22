
import tkinter as tk


class Window(tk.Tk):
  '''
  Builds GUI for app.
  '''
  def __init__(self, *args, **kwargs):
    tk.Tk.__init__(self, *args, **kwargs)
    self.title("Clock App")
    self.minsize(1200, 700) # width x height
    self.configure(background = "black")
    
    container = tk.Frame(self)
    container.pack(side = "right", fill = "both", expand = True)
    
    self.frames = {}
    for F in (Clock, Timer):
      frame = F(container, self)
      self.frames[F] = frame
      frame.grid(row = 0, column = 0, sticky ="nsew")
      
    self.show_frame(Clock)
    
    TabButtons(self, self)

    
  def show_frame(self, frame_name):
    '''
    Switches between frames.
    '''
    frame = self.frames[frame_name]
    frame.tkraise()
    
    
class Clock(tk.Frame):
  '''
  Frame to display clock showing current time.
  '''
  def __init__(self, parent, controller):
    tk.Frame.__init__(self, parent)
    label = tk.Label(self, text = "Page 1") 
    label.grid(row = 0, column = 4, padx = 10, pady = 10)
    
    
class Timer(tk.Frame):
  '''
  Frame to display timer.
  '''
  def __init__(self, parent, controller):
    tk.Frame.__init__(self, parent)
    label = tk.Label(self, text = "Page 2") 
    label.grid(row = 0, column = 4, padx = 10, pady = 10)
      
      
class TabButtons(tk.Frame):
  '''
  Constant frame that displays buttons to switch between Clock/Timer.
  '''
  def __init__(self, parent, controller):
    tk.Frame.__init__(self, parent)
    
    tab = tk.Frame(background = "purple", width = 100)
    tab.pack(side = "left", fill = "y")
    
    clock_button = tk.Button(tab, 
                             text = "Clock", 
                             background = "pink", 
                             width = 10, 
                             command = lambda: controller.show_frame(Clock))
    clock_button.place(x = 10, y = 10)
    
    timer_button = tk.Button(tab, 
                             text = "Timer", 
                             background = "green", 
                             width = 10, 
                             command = lambda: controller.show_frame(Timer))
    timer_button.place(x = 10, y = 45)
    
    exit_button = tk.Button(tab, 
                            text = "EXIT", 
                            background = "brown", 
                            width = 10, 
                            command = quit)
    exit_button.place(x = 10, y = 85)
