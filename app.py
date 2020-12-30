
import tkinter as tk
import math


s_font = ("times", 12)

wn = tk.Tk()
wn.title("Clock App")
wn.minsize(1200, 800) #widthxheight
wn.iconphoto(False, tk.PhotoImage(file = "clockApp-logo.png"))
wn.resizable(False, False)


# tab frame
tab_frame = tk.Frame(wn, 
                     bg = "white", 
                     width = 200, 
                     )
tab_frame.pack(side = "left", fill = "y")
# clock button
tk.Button(tab_frame, 
          text = "Clock", 
          bg = "orange", 
          fg = "white", 
          width = 20, 
          font = s_font, 
          command = "", 
          ).pack(padx = 5, pady = 10)
# timer button
tk.Button(tab_frame, 
          text = "Timer", 
          bg = "orange", 
          fg = "white", 
          width = 20, 
          font = s_font, 
          command = "", 
          ).pack(padx = 5, pady = 10)
# quit button
tk.Button(tab_frame, 
          text = "EXIT", 
          bg = "grey", 
          fg = "white", 
          width = 20, 
          font = s_font, 
          command = quit, 
          ).pack(padx = 5, pady = 10)


# canvas for analog clock
analog_canvas = tk.Canvas(wn, 
                          bg = "black", 
                          width = 1000
                          )
