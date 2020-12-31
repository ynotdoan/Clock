
import tkinter as tk
import math


b_font = ("times", 70, "bold")
s_font = ("times", 12, "bold")

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


# analog clock canvas
analog_canvas = tk.Canvas(wn, 
                          bg = "black", 
                          width = 1000
                          )


# digital clock frame
digital_frame = tk.Frame(wn, 
                         bg = "black", 
                         width = 1000, 
                         )


# timer frame
timer_frame = tk.Frame(wn, 
                       bg = "black", 
                       width = 1000, 
                       )
