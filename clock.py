
'''
Module for clock(s) feature.
'''

import tkinter as tk
import time
import math


def get_time():
  '''
  Gets current time.
  '''
  hr = time.localtime()[3]
  mn = time.localtime()[4]
  sc = time.localtime()[5]
  
  return hr, mn, sc


class Clock(tk.Canvas):
  '''
  Canvas to display clock.
  '''
  def __init__(self):
    tk.Canvas.__init__(self)
    self.configure(background = "black", width = 1000, )
    self.pack(side = "right", fill = "y")
    self.outline = self.create_oval(250, 250, 750, 750, 
                                    outline = "blue", 
                                    width = 10)
    switch_button = tk.Button(self, 
                              text = "Switch to digital", 
                              background = "blue", 
                              foreground = "white", 
                              width = 15, 
                              command = "")
    switch_button.place(x = 445, y = 50)

    t_start = 240 # point near edge of clock
    t_end = 220
    # creates lines for hour markings
    for i in range(12):
      self.create_line(500 + t_start * math.cos(2 * math.pi * i / 12),
                       500 + t_start * math.sin(2 * math.pi * i / 12),
                       500 + t_end * math.cos(2 * math.pi * i / 12),
                       500 + t_end * math.sin(2 * math.pi * i / 12),
                       fill = "red", 
                       width = 5)
    # creates lines for minute markings 
    for i in range(60):
      self.create_line(500 + t_start * math.cos(2 * math.pi * i / 60), 
                       500 + t_start * math.sin(2 * math.pi * i / 60), 
                       500 + (t_end + 10) * math.cos(2 * math.pi * i / 60), 
                       500 + (t_end + 10) * math.sin(2 * math.pi * i / 60), 
                       fill = "red", 
                       width = 2)