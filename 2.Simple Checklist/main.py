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
def add_item():
    '''Add an individual item to list box'''
    my_listbox.insert(END, list_entry.get())
    list_entry.delete(0, END)

#create frames
input_frame = Frame(root, bg=root_color)
output_frame = Frame(root, bg=root_color)
button_frame = Frame(root, bg=root_color)
input_frame.pack()
output_frame.pack()
button_frame.pack()

#Input frame layout
my_scrollbar = Scrollbar(output_frame)
list_entry = Entry(input_frame, width=35, borderwidth=3, font=my_font)
list_add_button = Button(input_frame, text='Add Item', borderwidth=2, font=my_font, bg=button_color, command=add_item)
list_entry.grid(row=0, column=0, padx=5, pady=5)
list_add_button.grid(row=0, column=1, padx=5, pady=5, ipadx=5)
my_scrollbar.grid(row=0, column=1, sticky='NS')

#output frsme layout
my_listbox = Listbox(output_frame, height=15, width=45, borderwidth=3, font=my_font)
my_listbox.grid(row=0, column=0)

#Button frame layout
list_remove_button = Button(button_frame, text='Remove Item', borderwidth=2, font=my_font, bg=button_color)
list_clear_button = Button(button_frame, text='Clear List', borderwidth=2, font=my_font, bg=button_color)
save_button = Button(button_frame, text='Save List', borderwidth=2, font=my_font, bg=button_color)
quit_button = Button(button_frame, text='Quit', borderwidth=2, font=my_font, bg=button_color, command=root.destroy)
list_remove_button.grid(row=0, column=0, padx=2, pady=10)
list_clear_button.grid(row=0, column=1, padx=2, pady=10, ipadx=10)
save_button.grid(row=0, column=2, padx=2, pady=10, ipadx=10)
quit_button.grid(row=0, column=3, padx=2, pady=10, ipadx=25)

#Run the root window's main loop
root.mainloop()
