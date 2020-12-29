
'''
Module for clock(s) feature.
'''

import tkinter as tk
import time
import math


canvas = tk.Canvas(background = "black", width = 1000)
canvas.pack(side = "right", fill = "y")

outline = canvas.create_oval(250, 250, 750, 750, 
                                outline = "grey", 
                                width = 10)
switch_button = tk.Button(canvas, 
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
  canvas.create_line(500 + t_start * math.cos(2 * math.pi * i / 60), 
                     500 + t_start * math.sin(2 * math.pi * i / 60), 
                     500 + (t_end + 10) * math.cos(2 * math.pi * i / 60), 
                     500 + (t_end + 10) * math.sin(2 * math.pi * i / 60), 
                     fill = "white", 
                     width = 2)

# creates lines for hour markings
for i in range(12):
  canvas.create_line(500 + t_start * math.cos(2 * math.pi * i / 12),
                     500 + t_start * math.sin(2 * math.pi * i / 12),
                     500 + t_end * math.cos(2 * math.pi * i / 12),
                     500 + t_end * math.sin(2 * math.pi * i / 12),
                     fill = "red", 
                     width = 5)


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


class AnalogClock():
  '''
  Canvas to display clock.
  '''
  def __init__(self, length):
    self.length = length
    self.line = canvas.create_line(500, 500, 500, 500, 
                                 fill = "white", 
                                 width = 4)

  def update_hands(self, angle):
    '''
    Updates hands of clock.
    '''
    x = 500 + self.length * math.cos(angle)
    y = 500 + self.length * math.sin(angle)
    canvas.coords(self.line, 500, 500, x, y)
    
  def draw_hands(self):
    '''
    Draws hands on clock.
    '''
    hour, minute, second = convert_time()

    # hour hand
    hour_hand.update_hands(2 * math.pi * hour / 12 - math.pi / 2)
    # minute hand
    minute_hand.update_hands(2 * math.pi * minute / 60 - math.pi / 2) 
    # seconds hand
    second_hand.update_hands(2 * math.pi * second / 60 - math.pi / 2)    
    # calls draw_hands() to update hands every 1000 ms
    canvas.after(1000, self.draw_hands)   


hour_hand = AnalogClock(130)
minute_hand = AnalogClock(180)
second_hand = AnalogClock(230)

# AnalogClock(object).draw_hands()
# canvas.mainloop()
