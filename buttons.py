
import tkinter as tk
import frames as f
import switch_frame as sf
import digital_clock as dc


# Buttons in left tab
# clock button
tk.Button(f.tab_frame, 
          text = "Clock", 
          bg = "orange", 
          fg = "white", 
          width = 20, 
          font = f.s_font, 
          command = lambda: sf.show_analog_clock(sf.current_frame[0]), 
          ).pack(padx = 5, pady = 10)
# quit button
tk.Button(f.tab_frame, 
          text = "EXIT", 
          bg = "grey", 
          fg = "white", 
          width = 20, 
          font = f.s_font, 
          command = quit, 
          ).pack(padx = 5, pady = 10)

f.tab_frame.pack(side = "left", fill = "y")


# Button in analog clock
# switch to digital in analog clock
tk.Button(f.analog_canvas, 
          text = "Switch to digital", 
          bg = "orange", 
          fg = "white", 
          width = 15, 
          font = f.s_font, 
          command = lambda: sf.show_digital_clock(sf.current_frame[0]), 
          ).pack(anchor = "center", pady = (100, 0))


# Buttons in digital clock
# switch to analog in digital clock
tk.Button(f.digital_frame, 
          text = "Switch to analog", 
          bg = "orange", 
          fg = "white", 
          width = 15, 
          font = f.s_font, 
          command = lambda: sf.show_analog_clock(sf.current_frame[0]), 
          ).place(x = 350, y = 100)
