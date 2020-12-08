#simple Checklist
from tkinter import *

#Define window
root = Tk()
root.title('Simple Checklist')
root.iconbitmap('2.Simple Checklist/check.ico')
root.geometry('400x400')
root.resizable(0,0)

#Define fonts and colors
my_font = ('Times New Roman', 12)
root_color = '#6c1cbc'
button_color = '#e2cff4'
root.config(bg=root_color)

#Define functions

#Define layout
#create frames
input_frame = Frame(root, bg=root_color)
output_frame = Frame(root, bg=root_color)
button_frame = Frame(root, bg=root_color)
input_frame.pack()
output_frame.pack()
button_frame.pack()

#Input frame layout
list_entry = Entry(input_frame, width=35, borderwidth=3, font=my_font)
list_add_button = Button(input_frame, text='Add Item', borderwidth=2, font=my_font, bg=button_color)
list_entry.grid(row=0, column=0)
list_add_button.grid(row=0, column=1)

#output frsme layout
my_listbox = Listbox(output_frame, height=15, width=45, borderwidth=3, font=my_font)
my_listbox.grid(row=0, column=0)

#Button frame layout
list_remove_button = Button(button_frame, text='Remove Item', borderwidth=2, font=my_font, bg=button_color)
list_clear_button = Button(button_frame, text='Clear List', borderwidth=2, font=my_font, bg=button_color)
save_button = Button(button_frame, text='Save List', borderwidth=2, font=my_font, bg=button_color)
quit_button = Button(button_frame, text='Quit', borderwidth=2, font=my_font, bg=button_color, command=root.destroy)
list_remove_button.grid(row=0, column=0)
list_clear_button.grid(row=0, column=1)
save_button.grid(row=0, column=2)
quit_button.grid(row=0, column=3)

#Run the root window's main loop
root.mainloop()
