#Simple Calculator
from tkinter import *

#Define window
root = Tk()
root.title('Calculator')
root.iconbitmap('3.Simple Calculator/calc.ico')
root.geometry('300x400')
root.resizable(0,0)

#Define color and fonts
dark_green = '#93af22'
light_green = '#acc253'
white_green = '#edefe0'
button_font = ('Arial', 18)
display_font = ('Arial', 30)

#Define functions

#GUI layout
#Define frames
display_frame = LabelFrame(root)
button_frame = LabelFrame(root)
display_frame.pack()
button_frame.pack()

#Layout for the display frame
display = Entry(display_frame, width=50, font=display_font, bg=white_green, borderwidth=5, justify=RIGHT)
display.pack(padx=5, pady=5)

#Layout for the button frame
clear_button = Button(button_frame, text='Clear', font=button_font, bg=dark_green)
quit_button = Button(button_frame, text='Quit', font=button_font, bg=dark_green)

inverse_button = Button(button_frame, text='1/x', font=button_font, bg=light_green)
square_button = Button(button_frame, text='x^2', font=button_font, bg=light_green)
exponent_button = Button(button_frame, text='x^n', font=button_font, bg=light_green)
divide_button = Button(button_frame, text=' / ', font=button_font, bg=light_green)
multiply_button = Button(button_frame, text='*', font=button_font, bg=light_green)
subtract_button = Button(button_frame, text='-', font=button_font, bg=light_green)
add_button = Button(button_frame, text='+', font=button_font, bg=light_green)
equal_button = Button(button_frame, text='=', font=button_font, bg=dark_green)
decimal_button = Button(button_frame, text='.', font=button_font, bg='black', fg='white')
negate_button = Button(button_frame, text='+/-', font=button_font, bg='black', fg='white')

nine_button = Button(button_frame, text='9', font=button_font, bg='black', fg='white')
eight_button = Button(button_frame, text='8', font=button_font, bg='black', fg='white')
seven_button = Button(button_frame, text='7', font=button_font, bg='black', fg='white')
six_button = Button(button_frame, text='6', font=button_font, bg='black', fg='white')
five_button = Button(button_frame, text='5', font=button_font, bg='black', fg='white')
four_button = Button(button_frame, text='4', font=button_font, bg='black', fg='white')
three_button = Button(button_frame, text='3', font=button_font, bg='black', fg='white')
two_button = Button(button_frame, text='2', font=button_font, bg='black', fg='white')
one_button = Button(button_frame, text='1', font=button_font, bg='black', fg='white')
zero_button = Button(button_frame, text='0', font=button_font, bg='black', fg='white')

#First row
clear_button.grid(row=0, column=0, pady=1, sticky='WE', columnspan=2)
quit_button.grid(row=0, column=2, pady=1, sticky='WE', columnspan=2)
#Second row
inverse_button.grid(row=1, column=0, pady=1, sticky='WE')
square_button.grid(row=1, column=1, pady=1, sticky='WE')
exponent_button.grid(row=1, column=2, pady=1, sticky='WE')
divide_button.grid(row=1, column=3, pady=1, sticky='WE')
#Third row
seven_button.grid(row=2, column=0, pady=1, sticky='WE', ipadx=20)
eight_button.grid(row=2, column=1, pady=1, sticky='WE', ipadx=20)
nine_button.grid(row=2, column=2, pady=1, sticky='WE', ipadx=20)
multiply_button.grid(row=2, column=3, pady=1, sticky='WE', ipadx=20)
#Fourth row
four_button.grid(row=3, column=0, pady=1, sticky='WE', ipadx=20)
five_button.grid(row=3, column=1, pady=1, sticky='WE', ipadx=20)
six_button.grid(row=3, column=2, pady=1, sticky='WE', ipadx=20)
subtract_button.grid(row=3, column=3, pady=1, sticky='WE', ipadx=20)
#Fifth row
one_button.grid(row=4, column=0, pady=1, sticky='WE', ipadx=20)
two_button.grid(row=4, column=1, pady=1, sticky='WE', ipadx=20)
three_button.grid(row=4, column=2, pady=1, sticky='WE', ipadx=20)
add_button.grid(row=4, column=3, pady=1, sticky='WE', ipadx=20)
#Sixth row
negate_button.grid(row=5, column=0, pady=1, sticky='WE', ipadx=20)
zero_button.grid(row=5, column=1, pady=1, sticky='WE', ipadx=20)
decimal_button.grid(row=5, column=2, pady=1, sticky='WE', ipadx=20)
exponent_button.grid(row=5, column=3, pady=1, sticky='WE', ipadx=20)





#Run the mainloop
root.mainloop()