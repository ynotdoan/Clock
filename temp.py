#This makes a clock in python

#import modules
import time
import tkinter as tk
import math

#make a hand class
class Hand:
  def __init__(self,length,color):
    self.length=length
    self.line = canvas.create_line(150, 150, 150, 150, fill=color)

  def update_hand(self, angle):
    x_endpoint = 150 + self.length*math.cos(angle)
    y_endpoint = 150 + self.length*math.sin(angle)
    canvas.coords(self.line, 150, 150, x_endpoint, y_endpoint)

#make master screen
master=tk.Tk()
master.geometry("300x300")

#add a canvas
canvas=tk.Canvas(master,bg="black", width=300, height=300)
canvas.pack()

#add the outline of the clock body
outline=canvas.create_oval(25,25,275,275,outline="white",width=2)

#draw all of the hour markings
t_start=110
t_end=120
for i in range(12):
  canvas.create_line(150+t_start*math.cos(2*math.pi*i/12),
             150+t_start*math.sin(2*math.pi*i/12),
             150+t_end*math.cos(2*math.pi*i/12),
             150+t_end*math.sin(2*math.pi*i/12),
             fill="white")

#define hands
h_hand = Hand(50, 'white')
m_hand = Hand(80, 'white')
s_hand = Hand(100, 'red')

#draw the hands
def draw_hands():
  #get hour, minute, and second
  hour=time.localtime()[3]
  minute=time.localtime()[4]
  second=time.localtime()[5]

  #calculate minute_real
  minute_real=minute+second/60

  #calculate hour_real
  hour_real=hour%12+minute_real/60

  #draw hour hand
  h_hand.update_hand(2*math.pi*(hour_real)/12-math.pi/2)

  #draw minute hand
  m_hand.update_hand(2*math.pi*minute_real/60-math.pi/2)

  #draw second hand
  s_hand.update_hand(2*math.pi*second/60-math.pi/2)

  master.after(1000, draw_hands)

# start update hands loop
draw_hands()

# start mainloop (required in non-REPL environments)
master.mainloop()