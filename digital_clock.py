
import tkinter as tk
import frames as f
import time


b_font = ("times", 70, "bold")

def get_time():
  hr = time.localtime()[3]
  mn = time.localtime()[4]
  sc = time.localtime()[5]
  
  return hr, mn, sc
  
  
def get_military_time():
  '''
  Get and display current 24h time.
  '''
  hr, mn, sc, = get_time()
  
  # convert hr to 24 hr
  mhr = (hr % 12) + 12
  
  military_time = f"{mhr}:{mn}:{sc}"
  
  military_label.config(text = military_time, 
                        font = b_font, 
                        )
  military_label.after(1000, get_military_time)
  

def get_digital_time():
  '''
  Get and display current time.
  '''
  hr, mn, sc, = get_time()
  
  # finds mod12 to get non 24h time
  dhr = hr % 12
  # if hr is less than 13, displays AM, else displays PM
  if (hr < 13):
    time = f"{dhr:02.0f}:{mn:02.0f}:{sc:02.0f} AM"
  elif (hr > 12):
    time = f"{dhr:02.0f}:{mn:02.0f}:{sc:02.0f} PM"

  digital_label.config(text = time, 
                       font = b_font, 
                       )
  digital_label.after(1000, get_digital_time)
  
  
# digital time label
digital_label = tk.Label(f.digital_frame, 
                         bg = "black", 
                         fg = "green", 
                         )

# military time label
military_label = tk.Label(f.digital_frame, 
                          bg = "black", 
                          fg = "green", 
                          )
