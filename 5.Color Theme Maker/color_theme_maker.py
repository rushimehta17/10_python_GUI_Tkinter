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
input_frame = LabelFrame(root, padx=5, pady=5)
output_frame = LabelFrame(root, padx=5, pady=5)
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
red_label.grid(row=0, column=0, sticky="W")
red_slider.grid(row=1, column=0, sticky="W")
red_button.grid(row=2, column=0, padx=1, pady=1, ipadx=20)

green_label.grid(row=0, column=1, sticky="W")
green_slider.grid(row=1, column=1, sticky="W")
green_button.grid(row=2, column=1, padx=1, pady=1, ipadx=15)

blue_label.grid(row=0, column=2, sticky="W")
blue_slider.grid(row=1, column=2, sticky="W")
blue_button.grid(row=2, column=2, padx=1, pady=1, ipadx=18)

yellow_button.grid(row=3, column=0, padx=1, pady=1, sticky="WE")
cyan_button.grid(row=3, column=1, padx=1, pady=1, sticky="WE")
magenta_button.grid(row=3, column=2, padx=1, pady=1, sticky="WE")
store_button.grid(row=4, column=0, columnspan=3, sticky="WE")
save_button.grid(row=4, column=3, padx=1, pady=1, sticky="WE")
quit_button.grid(row=4,column=4, padx=1, pady=1, sticky="WE")

#Create the color box and color labels
color_box = Label(input_frame, bg='black', height=6, width=15)
color_tuple = Label(input_frame, text='(0), (0), (0)')
color_hex = Label(input_frame, text='#000000')

#Put colorbox and labels on the frame
color_box.grid(row=1, column=3, columnspan=2, padx=35, pady=10, ipadx=10, ipady=10)
color_tuple.grid(row=2, column=3, columnspan=2)
color_hex.grid(row=3, column=3, columnspan=2)

#setting up the output frame
#Initialize a dictionary to hold all stored colors
stored_colors = {}
stored_color = IntVar()

#Create radio buttons to select store colors and populate each row with placeholder values
for i in range(6):
    radio = Radiobutton(output_frame, variable=stores_color, value=i)
    radio.grid(row=i, column=0, sticky="W")

    recall_button = Button(output_frame, text="Recall color", state=DISABLED)
    new_color_tuple = Label(output_frame, text="(255), (255), (255)")
    new_color_hex = Label(output_frame, text="#ffffff")
    new_color_black_box = Label(output_frame, bg='black', width=3, height=1)
    new_color_box = Label(output_frame, bg='white', width=3, height=1)

    recall_button.grid(row=i, column=1, padx=20)
    new_color_tuple.grid(row=i, column=2, padx=20)
    new_color_hex.grid(row=i, column=3, padx=20)
    new_color_black_box.grid(row=i, column=4, pady=2, ipadx=5, ipady=5)
    new_color_box.grid(row=i, column=4)

    #.cget() return the value of specific option. Store the text value of the tuple label and hex label
    stored_colors[stored_color.get()] = [new_color_tuple.cget('text'), new_color_hex.cget('text')]
    

#run the root window mainloop
root.mainloop()