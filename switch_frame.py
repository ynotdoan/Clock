
import frames as f
import analog_clock as ac
import digital_clock as dc


def show_analog_clock(frame):
  frame.pack_forget()
  f.analog_canvas.pack(fill = "both", expand = True)
  ac.AnalogClock().draw_hands()
  
  
def show_digital_clock(frame):
  frame.pack_forget()
  f.digital_frame.pack(fill = "both", expand = True)
  dc.get_time()
