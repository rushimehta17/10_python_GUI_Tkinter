#Hello GUI World
#icon from http://www.iconsmind.com

from tkinter import *
from tkinter import BOTH

root = Tk()
root.title("Hello GUI World!")
root.iconbitmap('0.Hello GUI World/wave.ico')
root.geometry('400x400')
root.resizable(0,0)

#Define fonts and colors
root_color = '#224870'
input_color = '#2a4494'
output_color = '#4ea5d9'
root.config(bg=root_color)

#Define functions

#Define Layout
#Define frame
input_frame = LabelFrame(root, bg=input_color)
output_frame = LabelFrame(root, bg=output_color)
input_frame.pack(pady=10)
output_frame.pack(padx=10, pady=(0,10), fill=BOTH, expand=True)

#Create widgets
name = Entry(input_frame, text="Enter your name", width=20)
submit_button = Button(input_frame, text = "Submit")
name.grid(row=0,column=0, padx=10, pady=10)
submit_button.grid(row=0,column=1, padx=10, pady=10, ipadx=20)


root.mainloop()