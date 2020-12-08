#Metric Helper
from tkinter import *

#Define window
root = Tk()
root.title('Metric Helper')
root.iconbitmap('1.Metric Helper/ruler.ico')
#root.geometry()
root.resizable(0,0)

#Define fonts and colors
field_font = ('cambria', 10)
bg_color = "#c75c5c"
button_color = "#f5cf87"
root.config(bg=bg_color)

#Define functions

#Define layout
#Create input and output entry
input_field = Entry(root, width=20, font=field_font)
output_field = Entry(root, width=20, font=field_font)
equal_label = Label(root, text="=", font=field_font, bg=bg_color)

input_field.grid(row=0, column=0)
equal_label.grid(row=0, column=1)
output_field.grid(row=0, column=2)

input_field.insert(0, 'Enter your quantity')

#Create dropdown for metrix value
metric_list = ["fento", 'pico', 'nan', 'micro', 'milli', 'centi', 'deci', 'base value', 'deca', 'hecto', 'kilo', 'mega', 'giga', 'tera', 'peta']
input_choice = StringVar()
output_choice = StringVar()
input_dropdown = OptionMenu(root, input_choice, *metric_list)
output_dropdown = OptionMenu(root, output_choice, *metric_list)
to_label = Label(root, text='to', font=field_font, bg=bg_color)

input_dropdown.grid(row=1, column=0)
to_label.grid(row=1, column=1)
output_dropdown.grid(row=1, column=2)

input_choice.set('base value')
output_choice.set('base value')

#Create a conversion button
convert_button = Button(root, text='Convert', font=field_font, bg=button_color)
convert_button.grid(row=2, column=0, columnspan=3)
#Mainloop
root.mainloop()