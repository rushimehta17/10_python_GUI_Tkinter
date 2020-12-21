#Gravity Simulator
from tkinter import *

#Define window
root = Tk()
root.title('Gravity simulator')
root.iconbitmap('8.Gravity Simulator/earth.ico')
root.geometry('500x670')
root.resizable(0,0)

#Define fonts and colors
#None use system defaults

#Define global variables
time = 0

#Define functions
def move(event):
    """Drag the balls vertically on the canvas to set the position"""
    #if the current object clicked has the "BALL" tag, we should allow it to be moved
    if "BALL" in main_canvas.gettags(CURRENT):
        #Record the x position of the ball and keep it the same
        x1 = main_canvas.coords(CURRENT)[0]
        x2= main_canvas.coords(CURRENT)[2]

        #Change the coords of the CURRENT object based on the event.y position of the mouse. Recall the ball has size 10
        main_canvas.coords(CURRENT, x1, event.y, x2, event.y+10)

        #Attempt to not move the ball off the canvas. CURRENT[3] is y2 coord
        if main_canvas.coords(CURRENT)[3] < 15:
            main_canvas.coords(CURRENT, x1, 5, x2, 15)
        #Below the bottom of the screen
        elif main_canvas.coords(CURRENT)[3] > 415:
            main_canvas.coords(CURRENT, x1, 405, x2, 415)

    #Update the height label for each ball
    update_height()

def update_height():
    """Update the height labels for each ball."""
    for i in range(1,5):
        heights['height_%d' % i].config(text="Height: " + str(round(415 - main_canvas.coords(balls['ball_%d' % i])[3], 2)))

def step():
    

#Define layout
#Create frame
canvas_frame = Frame(root)
input_frame = Frame(root)
canvas_frame.pack(pady=20)
input_frame.pack(fill=BOTH, expand=True)

#Canvas frame layout
main_canvas = Canvas(canvas_frame, width=400, height=415, bg='white')
main_canvas.grid(row=0, column=0, padx=5, pady=5)

line_0 = main_canvas.create_line(2,0,2,415)
line_1 = main_canvas.create_line(100,0,100,415)
line_2 = main_canvas.create_line(200,0,200,415)
line_3 = main_canvas.create_line(300,0,300,415)
line_4 = main_canvas.create_line(400,0,400,415)

balls = {}
balls['ball_1'] = main_canvas.create_oval(45,405,55,415, fill='red', tag="BALL")
balls['ball_2'] = main_canvas.create_oval(145,405,155,415, fill='green', tag="BALL")
balls['ball_3'] = main_canvas.create_oval(245,405,255,415, fill='blue', tag="BALL")
balls['ball_4'] = main_canvas.create_oval(345,405,355,415, fill='yellow', tag="BALL")

#input frame layout
#Row label
Label(input_frame, text='d').grid(row=0, column=0)
Label(input_frame, text='vi').grid(row=1, column=0)
Label(input_frame, text='a').grid(row=2, column=0, ipadx=22)
Label(input_frame, text='t').grid(row=3, column=0)

#Heights/Distance labels
heights = {}
for i in range(1,5):
    heights['height_%d' % i] = Label(input_frame, text='Height: ' + str(415 - main_canvas.coords(balls['ball_%d' % i])[3]))
    heights['height_%d' % i].grid(row=0, column=i)

#Velocity entry boxes
velocities = {}
for i in range(1,5):
    velocities['v_%d' % i] = Entry(input_frame, width=15)
    velocities['v_%d' % i].grid(row=1, column=i, padx=1)
    velocities['v_%d' % i].insert(0, '0')

#Acceleration entry boxes
accelerations = {}
for i in range(1,5):
    accelerations['a_%d' % i] = Entry(input_frame, width=15)
    accelerations['a_%d' % i].grid(row=2, column=i, padx=1)
    accelerations['a_%d' % i].insert(0, '0')

#Time slider
t_slider = Scale(input_frame, from_=0, to=1, tickinterval=.1, resolution=.01, orient=HORIZONTAL)
t_slider.grid(row=3, column=1, columnspan=4, sticky='WE')
t_slider.set(1)

#Buttons
step_button = Button(input_frame, text='Step')
run_button = Button(input_frame, text='Run')
graph_button = Button(input_frame, text='Graph')
reset_button = Button(input_frame, text='Reset')
quit_button = Button(input_frame, text='Quit', command=root.destroy)

#Make each ball 'dragable' in the vertical direction
root.bind('<B1-Motion>', move)


step_button.grid(row=4, column=1, pady=(10,0), sticky="WE")
run_button.grid(row=4, column=2, pady=(10,0), sticky="WE")
graph_button.grid(row=4, column=3, pady=(10,0), sticky="WE")
reset_button.grid(row=4, column=4, pady=(10,0), sticky="WE")
quit_button.grid(row=5, column=1, columnspan=4, sticky="WE")
#Run root window's main loop
root.mainloop()