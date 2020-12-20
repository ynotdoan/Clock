
import tkinter as tk


window = tk.Tk()

window.title("Clock app")
window.configure(width = 500, height = 300)
window.configure(bg = "orange")

test_button = tk.Button(window, 
                        text = "Hello there", 
                        command = exit, 
                        height = 10, 
                        width = 40, 
                        bg = "blue", 
                        fg = "purple")
test_button.place(x = 20, y = 20)