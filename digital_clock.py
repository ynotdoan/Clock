
import tkinter as tk
from time import strftime


frame = tk.Frame(background = "pink", width = 1000)
frame.pack(side = "right", fill = "y")

def get_time():
  '''
  Get and display current time.
  '''
  current_time = strftime("%H:%M:%S %p")
  label.config(text = current_time)
  label.after(1000, get_time)
  
label = tk.Label(frame, background = "black", foreground = "green")
label.pack(anchor = "center")
get_time()
