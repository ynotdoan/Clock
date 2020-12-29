
'''
Module for main window and side tab buttons.
'''

import tkinter as tk
import analog_clock as ac
import digital_clock as dc


d_font = ("Times", 10) # defualt font for entire program

class Window(tk.Tk):
  '''
  Generates main window.
  '''
  def __init__(self):
    tk.Tk.__init__(self)
    self.title("Clock App")
    self.minsize(1200, 800) # widthxheight
    self.iconphoto(False, tk.PhotoImage(file = "clockApp-logo.PNG"))
    self.resizable(False, False)
    
    Tab()


def open_analog_clock():
  ac.AnalogClock(object).draw_hands()
  ac.canvas
  
def open_digital_clock():
  dc.frame


class Tab(tk.Frame):
  '''
  Side tab with buttons.
  '''
  def __init__(self):
    tk.Frame.__init__(self)
    self.configure(background = "white",)
    self.pack(side = "left", fill = "both", expand = True)
    
    clock_button = tk.Button(self, 
                             text = "Clock", 
                             background = "orange", 
                             width = 20, 
                             font = d_font, 
                             command = open_analog_clock)
    clock_button.pack(padx = 5, pady = 10)
    
    timer_button = tk.Button(self, 
                             text = "Timer", 
                             background = "orange", 
                             width = 20, 
                             font = d_font, 
                             command = open_digital_clock)
    timer_button.pack(padx = 5, pady = 10)
    
    exit_button = tk.Button(self, 
                            text = "EXIT", 
                            background = "orange", 
                            width = 20, 
                            font = d_font, 
                            command = quit)
    exit_button.pack(padx = 5, pady = 10)
