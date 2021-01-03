
import tkinter as tk
import time
import frames as f


nhr = 0
nmn = 0
nsc = 0


def increase_hour():
  global nhr
  
  nhr += 1
  hr_count = nhr % 13
  hour.configure(text = f"{hr_count:02.0f}")
  
def decrease_hour():
  global nhr

  nhr -= 1
  hr_count = nhr % 13
  hour.configure(text = f"{hr_count:02.0f}")
  
def increase_minute():
  global nmn
  
  nmn += 1
  mn_count = nmn % 60
  minute.configure(text = f"{mn_count:02.0f}")
  
def decrease_minute():
  global nmn
  
  nmn -= 1
  mn_count = nmn % 60
  minute.configure(text = f"{mn_count:02.0f}")
  
def increase_second():
  global nsc
  
  nsc += 1
  sc_count = nsc % 60
  second.configure(text = f"{sc_count:02.0f}")
  
def decrease_second():
  global nsc
  
  nsc -= 1
  sc_count = nsc % 60
  second.configure(text = f"{sc_count:02.0f}")
  
def update_second(seconds):
  second.configure(text = f"{(seconds - 1) % 60:02.0f}")
  
def start_timer():
  # gets text on label and converts to int
  # hour_cd = int (hour["text"])
  # minute_cd = int (minute["text"])
  
  second_cd = int (second["text"])
  
  if (second_cd != 0):
    second_cd -= 1
    second.after(1000, start_timer())

  # .sleep()

# hour timer label
hour = tk.Label(f.timer_frame,
                text = f"{0:02.0f}", 
                bg = "white", 
                fg = "black", 
                width = 2,  
                font = f.b_font, 
                )
# minute timer label
minute = tk.Label(f.timer_frame, 
                  text = f"{0:02.0f}", 
                  bg = "white", 
                  fg = "black", 
                  width = 2, 
                  font = f.b_font, 
                  )
# seconds timer label
second = tk.Label(f.timer_frame, 
                  text = f"{0:02.0f}", 
                  bg = "white", 
                  fg = "black", 
                  width = 2, 
                  font = f.b_font, 
                  )
