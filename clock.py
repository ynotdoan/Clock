
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

def convert_time():
  '''
  Converts current time to display on clock.
  '''
  hr, mn, sc = get_time()
  
  minute = mn + sc / 60
  hour = hr % 12 + minute /60
  
  return hour, minute, sc


class Clock(tk.Canvas):
  '''
  Canvas to display clock.
  '''
  def __init__(self):
    tk.Canvas.__init__(self)
    self.configure(background = "black", width = 1000, )
    self.pack(side = "right", fill = "y")
    self.outline = self.create_oval(250, 250, 750, 750, 
                                    outline = "grey", 
                                    width = 10)
    switch_button = tk.Button(self, 
                              text = "Switch to digital", 
                              background = "white", 
                              foreground = "black", 
                              width = 15, 
                              command = "")
    switch_button.place(x = 445, y = 50)

    t_start = 240 # point near edge of clock
    t_end = 220
    # creates lines for minute markings 
    for i in range(60):
      self.create_line(500 + t_start * math.cos(2 * math.pi * i / 60), 
                       500 + t_start * math.sin(2 * math.pi * i / 60), 
                       500 + (t_end + 10) * math.cos(2 * math.pi * i / 60), 
                       500 + (t_end + 10) * math.sin(2 * math.pi * i / 60), 
                       fill = "white", 
                       width = 2)

    # creates lines for hour markings
    for i in range(12):
      self.create_line(500 + t_start * math.cos(2 * math.pi * i / 12),
                       500 + t_start * math.sin(2 * math.pi * i / 12),
                       500 + t_end * math.cos(2 * math.pi * i / 12),
                       500 + t_end * math.sin(2 * math.pi * i / 12),
                       fill = "red", 
                       width = 5)
            
  def update_hands(self, length, angle, color):
    '''
    Updates hands of clock.
    '''
    self.line = self.create_line(500, 500, 500, 500, 
                            fill = color, 
                            width = 4)
    x = 500 + length * math.cos(angle)
    y = 500 + length * math.sin(angle)
    self.coords(self.line, 500, 500, x, y)
    
  def draw_hands(self):
    '''
    Draws hands on clock.
    '''
    hour, minute, second = convert_time()
    
    # hour hand
    self.update_hands(120, 
                      2 * math.pi * hour / 12 - math.pi / 2, 
                      "blue")
    # minute hand
    self.update_hands(170, 
                      2 * math.pi * minute / 60 - math.pi / 2, 
                      "blue")
    # second hand
    self.update_hands(220, 
                      2 * math.pi * second / 60 - math.pi / 2, 
                      "red")
    
    self.after(1000, self.draw_hands)
