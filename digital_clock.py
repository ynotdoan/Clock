
import tkinter as tk
import frames as f
from time import strftime


def get_time():
  '''
  Get and display current time.
  '''
  current_time = strftime("%H:%M:%S %p")
  digital_time.config(text = current_time, 
                      font = ("times", 50)
                      )
  digital_time.after(1000, get_time)

# digital time label
digital_time = tk.Label(f.digital_frame, 
                        background = "black", 
                        foreground = "green", 
                        )
digital_time.pack(side = "bottom", anchor = "n", expand = True)
