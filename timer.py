
import tkinter as tk
import time
import frames as f


hr_count = 0
mn_count = 0
sc_count = 0


def increase_hour():
  global hr_count
  hr_count += 1
  hour.configure(text = f"{hr_count:02.0f}")
  
def decrease_hour():
  global hr_count
  
  # checks if hr is 0 so negative numbers can't be set
  if (hr_count == 0):
    hr_count = 0
  elif (hr_count > 0):  
    hr_count -= 1
  
  hour.configure(text = f"{hr_count:02.0f}")
  
def increase_minute():
  global mn_count
  mn_count += 1
  minute.configure(text = f"{mn_count:02.0f}")
  
def decrease_minute():
  global mn_count
  
  if (mn_count == 0):
    mn_count = 0
  elif (mn_count > 0):
    mn_count -= 1
  
  minute.configure(text = f"{mn_count:02.0f}")
  
def increase_second():
  global sc_count
  sc_count += 1
  second.configure(text = f"{sc_count:02.0f}")
  
def decrease_second():
  global sc_count
  
  if (sc_count == 0):
    sc_count = 0
  elif (sc_count > 0):
    sc_count -= 1
  
  second.configure(text = f"{sc_count:02.0f}")


# hour timer label
hour = tk.Label(f.timer_frame,
                text = f"{hr_count:02.0f}", 
                bg = "white", 
                fg = "black", 
                width = 2,  
                font = f.b_font, 
                )
# minute timer label
minute = tk.Label(f.timer_frame, 
                  text = f"{mn_count:02.0f}", 
                  bg = "white", 
                  fg = "black", 
                  width = 2, 
                  font = f.b_font, 
                  )
# seconds timer label
second = tk.Label(f.timer_frame, 
                  text = f"{sc_count:02.0f}", 
                  bg = "white", 
                  fg = "black", 
                  width = 2, 
                  font = f.b_font, 
                  )
