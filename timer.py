
import tkinter as tk
import time
import frames as f




def increase_hour(hr):
  return hr + 1

hr = 0
thr = increase_hour(hr)

# hour timer label
hour = tk.Label(f.timer_frame,
                text = hr, 
                bg = "white", 
                fg = "black", 
                width = 2,  
                font = f.b_font, 
                )
# minute timer label
minute = tk.Label(f.timer_frame, 
                  text = "00", 
                  bg = "white", 
                  fg = "black", 
                  width = 2, 
                  font = f.b_font, 
                  )
# seconds timer label
second = tk.Label(f.timer_frame, 
                  text = "00", 
                  bg = "white", 
                  fg = "black", 
                  width = 2, 
                  font = f.b_font, 
                  )
