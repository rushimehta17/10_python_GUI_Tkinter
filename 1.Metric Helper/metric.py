#Metric Helper
from tkinter import *
from tkinter import ttk

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
def convert():
    '''COnvert from one metrix prefix to another'''
    metrix_values = {
        'fento':10**-15,
        'pico':10**-12,
        'nano':10**-9,
        'micro':10**-6,
        'milli':10**-3,
        'centi':10**-2,
        'deci':10**-1,
        'base value':10**0,
        'deca':10**1,
        'hecto':10**2,
        'kilo':10**3,
        'mega':10**6,
        'giga':10**9,
        'tera':10**12,
        'peda':10**15
    }
    #clear the output field
    output_field.delete(0, END)

    #Get all user information
    start_value = float(input_field.get())
    start_prefix = input_combobox.get()
    end_prefix = output_combobox.get()

    #Convert to base value
    base_value = start_value * metrix_values[start_prefix]
    #Convert to new metric value
    end_value = base_value / metrix_values[end_prefix]

    #Update output field with answer
    output_field.insert(0, str(end_value))

#Define layout
#Create input and output entry
input_field = Entry(root, width=20, font=field_font, borderwidth=3)
output_field = Entry(root, width=20, font=field_font, borderwidth=3)
equal_label = Label(root, text="=", font=field_font, bg=bg_color)

input_field.grid(row=0, column=0, padx=10, pady=10)
equal_label.grid(row=0, column=1, padx=10,pady=10)
output_field.grid(row=0, column=2, padx=10,pady=10)

input_field.insert(0, 'Enter your quantity')

#Create combobox for metrix value
metric_list = ['fento', 'pico', 'nano', 'micro', 'milli', 'centi', 'deci', 'base value', 'deca', 'hecto', 'kilo', 'mega', 'giga', 'tera', 'peta']
input_combobox = ttk.Combobox(root, value=metric_list, font=field_font, justify='center')
output_combobox = ttk.Combobox(root, value=metric_list, font=field_font, justify='center')

to_label = Label(root, text='to', font=field_font, bg=bg_color)

input_combobox.grid(row=1, column=0, padx=10, pady=10)
to_label.grid(row=1, column=1, padx=10, pady=10)
output_combobox.grid(row=1, column=2, padx=10, pady=10)

input_combobox.set('base value')
output_combobox.set('base value')

#Create a conversion button
convert_button = Button(root, text='Convert', font=field_font, bg=button_color, command=convert)
convert_button.grid(row=2, column=0, columnspan=3, padx=10, pady=10, ipadx=50)
#Mainloop
root.mainloop()