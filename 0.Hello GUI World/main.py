#Hello GUI World
#icon from http://www.iconsmind.com

from tkinter import *
from tkinter import BOTH, StringVar, END
from PIL import ImageTk, Image

root = Tk()
root.title("Hello GUI World!")
root.iconbitmap('wave.ico')
root.geometry('400x400')
root.resizable(0,0)

#Define fonts and colors
root_color = '#224870'
input_color = '#2a4494'
output_color = '#4ea5d9'
root.config(bg=root_color)

#Define functions
def submit_name():
    """Say Hello to the user"""
    #create a label for the use
    if case_style.get() == 'normal':
        name_label = Label(output_frame, text="Hello "+ name.get() + "! Keep learning Tkinter!", bg=output_color)
    elif case_style.get() == 'upper':
        name_label = Label(output_frame, text=("Hello "+ name.get() + "! Keep learning Tkinter!").upper(), bg=output_color)
    
    #pack label on screen
    name_label.pack()

    #clear the entry field
    name.delete(0, END)

#Define Layout
#Define frame
input_frame = LabelFrame(root, bg=input_color)
output_frame = LabelFrame(root, bg=output_color)
input_frame.pack(pady=10)
output_frame.pack(padx=10, pady=(0,10), fill=BOTH, expand=True)

#Create widgets
name = Entry(input_frame, text="Enter your name", width=20)
submit_button = Button(input_frame, text = "Submit", command=submit_name)
name.grid(row=0,column=0, padx=10, pady=10)
submit_button.grid(row=0,column=1, padx=10, pady=10, ipadx=20)

#create radio putton
case_style = StringVar()
case_style.set('normal')
normal_button = Radiobutton(input_frame, text="Normal Case", variable=case_style, value='normal', bg=input_color)
upper_button = Radiobutton(input_frame, text="Upper case", variable=case_style, value='upper', bg=input_color)
normal_button.grid(row=1,column=0, padx=2,pady=2)
upper_button.grid(row=1,column=1, padx=2,pady=2)

#add image
smile_img = ImageTk.PhotoImage(Image.open('smile.png'))
smile_label = Label(output_frame, image=smile_img, bg=output_color)
smile_label.pack()

root.mainloop()