#Color Theme Maker
from tkinter import *

#define window
root = Tk()
root.title("Color Theme Maker")
root.iconbitmap("5.Color Theme Maker/color_wheel.ico")
root.geometry("450x500")
root.resizable(0,0)

#Define fonts and color
#NONE: using system defaults

#Define functions

#Define layout
input_frame = LabelFrame(root)
output_frame = LabelFrame(root)
input_frame.pack(fill=BOTH, expand=True, padx=5, pady=5)
output_frame.pack(fill=BOTH, expand=True, padx=5,pady=5)

#Setting up the input frame
#Create the labels, slider and buttons for each color
red_label = Label(input_frame, text="R")
red_slider = Scale(input_frame, from_=0, to=255)
red_button = Button(input_frame, text="Red")

green_label = Label(input_frame, text="G")
green_slider = Scale(input_frame, from_=0, to=255)
green_button = Button(input_frame, text="Green")

blue_label = Label(input_frame, text="B")
blue_slider = Scale(input_frame, from_=0, to=255)
blue_button = Button(input_frame, text="Blue")

#Create buttons for each complimentary color
yellow_button = Button(input_frame, text="Yellow")
cyan_button = Button(input_frame, text="Cyan")
magenta_button = Button(input_frame, text="Magenta")

#Create utility buttons
store_button = Button(input_frame, text="Store color")
save_button = Button(input_frame, text="Save")
quit_button = Button(input_frame, text="Quit", command=root.destroy)

#Put labels, sliders and buttons on the frame....Use ipadx with rgb buttons to define column width, then use sticky on others
red_label.grid(row=0, column=0)
red_slider.grid(row=1, column=0)
red_button.grid(row=2, column=0)

green_label.grid(row=0, column=1)
green_slider.grid(row=1, column=1)
green_button.grid(row=2, column=1)

blue_label.grid(row=0, column=2)
blue_slider.grid(row=1, column=2)
blue_button.grid(row=2, column=2)

yellow_button.grid(row=3, column=0)
cyan_button.grid(row=3, column=1)
magenta_button.grid(row=3, column=2)
store_button.grid(row=4, column=0, columnspan=3, sticky="WE")
save_button.grid(row=4, column=3)
quit_button.grid(row=4,column=4)




#run the root window mainloop
root.mainloop()