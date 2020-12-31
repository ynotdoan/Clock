
import tkinter as tk
import time
import frames as f


def timer_pack():
  '''
  Packs all labels.
  '''
  # instructions label
  tk.Label(f.timer_frame, 
           text = "Use the '+' or '-' buttons to select a time limit and press 'GO' to start.",
           bg = "black", 
           fg = "white", 
           font = f.s_font, 
           ).pack(side = "top", anchor = "center", pady = (100, 0))
  
  # time labels
  hour.place(x = 240, y = 300)
  # first :
  tk.Label(f.timer_frame, 
           text = ":", 
           bg = "black", 
           fg = "white", 
           font = f.b_font, 
           ).place(x = 380, y = 300)
  minute.place(x = 440, y = 300)
  # second :
  tk.Label(f.timer_frame, 
           text = ":", 
           bg = "black", 
           fg = "white", 
           font = f.b_font, 
           ).place(x = 585, y = 300)
  second.place(x = 650, y = 300)
  
  # set buttons
  # hour +
  tk.Button(f.timer_frame, 
            text = "+", 
            bg = "orange", 
            fg = "black", 
            width = 12, 
            font = f.s_font, 
            command = "", 
            ).place(x = 240, y = 200)
  # hour -
  tk.Button(f.timer_frame, 
            text = "-", 
            bg = "orange", 
            fg = "black", 
            width = 12, 
            font = f.s_font,  
            command = "", 
            ).place(x = 240, y = 480)
  # minute +
  tk.Button(f.timer_frame, 
            text = "+", 
            bg = "orange", 
            fg = "black", 
            width = 12, 
            font = f.s_font, 
            command = "", 
            ).place(x = 440, y = 200)
  # minute -
  tk.Button(f.timer_frame, 
            text = "-", 
            bg = "orange", 
            fg = "black", 
            width = 12, 
            font = f.s_font,  
            command = "", 
            ).place(x = 440, y = 480)
  # seconds +
  tk.Button(f.timer_frame, 
            text = "+", 
            bg = "orange", 
            fg = "black", 
            width = 12, 
            font = f.s_font, 
            command = "", 
            ).place(x = 650, y = 200)
  # seconds -
  tk.Button(f.timer_frame, 
            text = "-", 
            bg = "orange", 
            fg = "black", 
            width = 12, 
            font = f.s_font,  
            command = "", 
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


# hour timer label
hour = tk.Label(f.timer_frame,
                text = "00", 
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
