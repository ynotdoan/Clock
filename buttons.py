
import tkinter as tk
import frames as f
import switch_frame as sf
import digital_clock as dc
import timer as tm

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
# timer button
tk.Button(f.tab_frame, 
          text = "Timer", 
          bg = "orange", 
          fg = "white", 
          width = 20, 
          font = f.s_font, 
          command = lambda: sf.show_timer(sf.current_frame[0]), 
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


# Buttons and label in timer
# instructions label
tk.Label(f.timer_frame, 
          text = "Use the '+' or '-' buttons to select a time limit and press 'GO' to start.",
          bg = "black", 
          fg = "white", 
          font = f.s_font, 
          ).pack(side = "top", anchor = "center", pady = (100, 0))
# labels for hr, mn, sc
tk.Label(f.timer_frame, 
         text = "HOUR", 
         bg = "black", 
         fg = "white", 
         font = f.s_font, 
         ).place(x = 240, y = 270)
tk.Label(f.timer_frame, 
         text = "MINUTE", 
         bg = "black", 
         fg = "white", 
         font = f.s_font, 
         ).place(x = 440, y = 270)
tk.Label(f.timer_frame, 
         text = "SECOND", 
         bg = "black", 
         fg = "white", 
         font = f.s_font, 
         ).place(x = 650, y = 270)
# set buttons
# hour +
tk.Button(f.timer_frame, 
          text = "+", 
          bg = "orange", 
          fg = "black", 
          width = 12, 
          font = f.s_font, 
          command = lambda: tm.increase_hour(), 
          ).place(x = 240, y = 200)
# hour -
tk.Button(f.timer_frame, 
          text = "-", 
          bg = "orange", 
          fg = "black", 
          width = 12, 
          font = f.s_font,  
          command = lambda: tm.decrease_hour(), 
          ).place(x = 240, y = 480)
# minute +
tk.Button(f.timer_frame, 
          text = "+", 
          bg = "orange", 
          fg = "black", 
          width = 12, 
          font = f.s_font, 
          command = lambda: tm.increase_minute(), 
          ).place(x = 440, y = 200)
# minute -
tk.Button(f.timer_frame, 
          text = "-", 
          bg = "orange", 
          fg = "black", 
          width = 12, 
          font = f.s_font,  
          command = lambda: tm.decrease_minute(), 
          ).place(x = 440, y = 480)
# seconds +
tk.Button(f.timer_frame, 
          text = "+", 
          bg = "orange", 
          fg = "black", 
          width = 12, 
          font = f.s_font, 
          command = lambda: tm.increase_second(), 
          ).place(x = 650, y = 200)
# seconds -
tk.Button(f.timer_frame, 
          text = "-", 
          bg = "orange", 
          fg = "black", 
          width = 12, 
          font = f.s_font,  
          command = lambda: tm.decrease_second(), 
          ).place(x = 650, y = 480)
# GO button
tk.Button(f.timer_frame, 
          text = "GO", 
          bg = "white", 
          fg = "orange", 
          width = 15, 
          height = 2, 
          font = f.s_font, 
          command = "", 
          ).pack(side = "bottom", anchor = "center", pady = (0, 150))