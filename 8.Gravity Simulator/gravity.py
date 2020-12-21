#Gravity Simulator
from tkinter import *

#Define window
root = Tk()
root.title('Gravity simulator')
root.iconbitmap('8.Gravity Simulator/earth.ico')
root.geometry('500x650')
root.resizable(0,0)

#Define fonts and colors
#None use system defaults

#Define global variables
time = 0

#Define functions

#Define layout
#Create frame
canvas_frame = Frame(root)
input_frame = Frame(root)
canvas_frame.pack(pady=20)
input_frame.pack(fill=BOTH, expand=True)

#Canvas frame layout
main_canvas = Canvas(canvas_frame, width=400, height=400, bg='white')
main_canvas.grid(row=0, column=0, padx=5, pady=5)

line_0 = main_canvas.create_line(2,0,2,415)
line_1 = main_canvas.create_line(100,0,100,415)
line_2 = main_canvas.create_line(200,0,200,415)
line_3 = main_canvas.create_line(300,0,300,415)
line_4 = main_canvas.create_line(400,0,400,415)

balls = {}
balls['ball_1'] = main_canvas.create_oval(45, 405, 55, 415, fill='red')


#Run root window's main loop
root.mainloop()