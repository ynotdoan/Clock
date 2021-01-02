
import tkinter as tk
import time
import frames as f


nhr = 0
nmn = 0
nsc = 0
hr_count = 0
mn_count = 0
sc_count = 0

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
  
  
def start_timer():
  global hr_count, mn_count, sc_count, nhr, nmn, nsc
  
  print (sc_count)
  # while (hr_count != 0 and mn_count != 0 and sc_count != 0):
  #   nsc -= 1
  #   sc_count = nsc % 60
  #   second.configure(text = f"{sc_count:02.0f}")
  #   #second.after(1000, )
  
    

# hour timer label
hour = tk.Label(f.timer_frame,
                text = f"{nhr:02.0f}", 
                bg = "white", 
                fg = "black", 
                width = 2,  
                font = f.b_font, 
                )
# minute timer label
minute = tk.Label(f.timer_frame, 
                  text = f"{nmn:02.0f}", 
                  bg = "white", 
                  fg = "black", 
                  width = 2, 
                  font = f.b_font, 
                  )
# seconds timer label
second = tk.Label(f.timer_frame, 
                  text = f"{nsc:02.0f}", 
                  bg = "white", 
                  fg = "black", 
                  width = 2, 
                  font = f.b_font, 
                  )
