
import tkinter as tk
import frames as f
import analog_clock as ac
import digital_clock as dc
import timer as tm


# holds the current frame
current_frame = []

def show_analog_clock(frame):
  frame.pack_forget()
  
  f.analog_canvas.pack(fill = "both", expand = True)
  ac.AnalogClock().draw_hands()
  
  # clears elements from list current_frame and appends current frame
  current_frame.clear()
  current_frame.append(f.analog_canvas)
  
  
def show_digital_clock(frame):
  frame.pack_forget()
  
  f.digital_frame.pack(fill = "both", expand = True)
  dc.digital_label.pack(side = "bottom", anchor = "n", expand = True)  
  dc.get_time()
  
  current_frame.clear()
  current_frame.append(f.digital_frame)

  show_digital_time(dc.military_label)


# Buttons/labels for digital clock ----------
digital_button = tk.Button(f.digital_frame, 
                           text = "Switch to digital clock", 
                           bg = "orange", 
                           fg = "white", 
                           width = 15, 
                           font = f.s_font, 
                           command = lambda: show_digital_time(dc.military_label), 
                           )
military_button = tk.Button(f.digital_frame, 
                            text = "Switch to 24h clock", 
                            bg = "orange", 
                            fg = "white", 
                            width = 15, 
                            font = f.s_font, 
                            command = lambda: show_military_time(dc.digital_label), 
                            )
# shows current mode, digital
current_digital = tk.Label(f.digital_frame, 
                           text = "Current mode: AM/PM", 
                           bg = "black", 
                           fg = "white",
                           font = f.s_font, 
                           )
# shows current mode, military
current_military = tk.Label(f.digital_frame, 
                            text = "Current mode: 24h", 
                            bg = "black", 
                            fg = "white",
                            font = f.s_font, 
                            )
# ----------

def show_military_time(label):
  '''
  Switches from digital time to military time.
  '''
  label.pack_forget()
  
  military_button.place_forget()
  digital_button.place(x = 510, y = 100)

  current_digital.place_forget()
  current_military.place(x = 510, y = 135)

  f.digital_frame.pack(fill = "both", expand = True)
  dc.military_label.pack(side = "bottom", anchor = "center", expand = True)
  dc.get_military_time()
  
  
def show_digital_time(label):
  '''
  Switches from military time to digital time.
  '''
  label.pack_forget()
  
  digital_button.place_forget()
  military_button.place(x = 510, y = 100)

  current_military.place_forget()
  current_digital.place(x = 510, y = 135)

  f.digital_frame.pack(fill = "both", expand = True)
  dc.digital_label.pack(side = "bottom", anchor = "center", expand = True)
  dc.get_digital_time()


def show_timer(frame):
  frame.pack_forget()
  
  f.timer_frame.pack(fill = "both", expand = True)
  tm.timer_pack() 
  
  current_frame.clear()
  current_frame.append(f.timer_frame)
  