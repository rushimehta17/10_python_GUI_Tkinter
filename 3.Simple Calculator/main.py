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
def submit_number(number):
    """Add a number or decomal to display"""
    #Insert the number or decimal pressed to end of display
    display.insert(END, number)

    #if decimal is pressed already disable it
    if "." in display.get():
        decimal_button.config(state=DISABLED)


def operate(operator):
    """Store the first number of operation to be used"""
    global first_number
    global operation

    #get the  operator and the current value of display. ie first number in calculator
    operation = operator
    first_number = display.get()

    #delete the value of first number from the display
    display.delete(0, END)

    #Display all operator buttons until equal or clear is pressed
    add_button.config(state=DISABLED)
    subtract_button.config(state=DISABLED)
    multiply_button.config(state=DISABLED)
    divide_button.config(state=DISABLED)
    exponent_button.config(state=DISABLED)
    inverse_button.config(state=DISABLED)
    square_button.config(state=DISABLED)

    #Return decimal to normal state
    decimal_button.config(state=NORMAL)

def equal():
    """Run the stored operation of two number"""
    #Performed desired mathematic
    if operation == 'add':
        value = float(first_number) + float(display.get())
    if operation == 'subtract':
        value = float(first_number) - float(display.get())
    if operation == 'multiply':
        value = float(first_number) * float(display.get())
    if operation == 'divide':
        if display.get() == "0":
            value = "ERROR"
        else:
            value = float(first_number) / float(display.get())
    elif operation == 'exponent':
        value = float(first_number) ** float(display.get())
    
    #Remove the current value and update with the answer
    display.delete(0, END)
    display.insert(0, value)

    #Return buttons to normal state
    enable_buttons()

def enable_buttons():
    """Enable all buttons on the calculator"""
    add_button.config(state=NORMAL)
    subtract_button.config(state=NORMAL)
    multiply_button.config(state=NORMAL)
    divide_button.config(state=NORMAL)
    exponent_button.config(state=NORMAL)
    inverse_button.config(state=NORMAL)
    square_button.config(state=NORMAL)
    decimal_button.config(state=NORMAL)

def clear():
    """Clear the display"""
    display.delete(0, END)
    
    #Returns buttons to enable state
    enable_buttons()

def inverse():
    """Calculate inverse of the given number"""
    #Do not allow for 1/0
    if display.get() == '0':
        value = 'ERROR'
    else:
        value = 1/float(display.get())
    
    #Remove the current value and update with answer
    display.delete(0, END)
    display.insert(0, value)

def square():
    """Calculate square of a given number"""
    value = float(display.get())**2
    
    #Remove the current value and update with answer
    display.delete(0, END)
    display.insert(0, value)

def negate():
    """Negate the current number"""
    value = -1 * float(display.get())
    
    #Remove the current value and update with answer
    display.delete(0, END)
    display.insert(0, value)



#GUI layout
#Define frames
display_frame = LabelFrame(root)
button_frame = LabelFrame(root)
display_frame.pack(padx=2, pady=(5,20))
button_frame.pack(padx=2, pady=5)

#Layout for the display frame
display = Entry(display_frame, width=50, font=display_font, bg=white_green, borderwidth=5, justify=RIGHT)
display.pack(padx=5, pady=5)

#Layout for the button frame
clear_button = Button(button_frame, text='Clear', font=button_font, bg=dark_green, command=clear)
quit_button = Button(button_frame, text='Quit', font=button_font, bg=dark_green, command=root.destroy)

inverse_button = Button(button_frame, text='1/x', font=button_font, bg=light_green, command=inverse)
square_button = Button(button_frame, text='x^2', font=button_font, bg=light_green, command=square)
exponent_button = Button(button_frame, text='x^n', font=button_font, bg=light_green, command=lambda:operate('exponent'))
divide_button = Button(button_frame, text=' / ', font=button_font, bg=light_green, command=lambda:operate('divide'))
multiply_button = Button(button_frame, text='*', font=button_font, bg=light_green, command=lambda:operate('multiply'))
subtract_button = Button(button_frame, text='-', font=button_font, bg=light_green, command=lambda:operate('subtract'))
add_button = Button(button_frame, text='+', font=button_font, bg=light_green, command=lambda:operate('add'))
equal_button = Button(button_frame, text='=', font=button_font, bg=dark_green, command=equal)
decimal_button = Button(button_frame, text='.', font=button_font, bg='black', fg='white', command=lambda:submit_number("."))
negate_button = Button(button_frame, text='+/-', font=button_font, bg='black', fg='white', command=negate)

nine_button = Button(button_frame, text='9', font=button_font, bg='black', fg='white', command=lambda:submit_number(9))
eight_button = Button(button_frame, text='8', font=button_font, bg='black', fg='white', command=lambda:submit_number(8))
seven_button = Button(button_frame, text='7', font=button_font, bg='black', fg='white', command=lambda:submit_number(7))
six_button = Button(button_frame, text='6', font=button_font, bg='black', fg='white', command=lambda:submit_number(6))
five_button = Button(button_frame, text='5', font=button_font, bg='black', fg='white', command=lambda:submit_number(5))
four_button = Button(button_frame, text='4', font=button_font, bg='black', fg='white', command=lambda:submit_number(4))
three_button = Button(button_frame, text='3', font=button_font, bg='black', fg='white', command=lambda:submit_number(3))
two_button = Button(button_frame, text='2', font=button_font, bg='black', fg='white', command=lambda:submit_number(2))
one_button = Button(button_frame, text='1', font=button_font, bg='black', fg='white', command=lambda:submit_number(1))
zero_button = Button(button_frame, text='0', font=button_font, bg='black', fg='white', command=lambda:submit_number(0))

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
four_button.grid(row=3, column=0, pady=1, sticky='WE')
five_button.grid(row=3, column=1, pady=1, sticky='WE')
six_button.grid(row=3, column=2, pady=1, sticky='WE')
subtract_button.grid(row=3, column=3, pady=1, sticky='WE')
#Fifth row
one_button.grid(row=4, column=0, pady=1, sticky='WE')
two_button.grid(row=4, column=1, pady=1, sticky='WE')
three_button.grid(row=4, column=2, pady=1, sticky='WE')
add_button.grid(row=4, column=3, pady=1, sticky='WE')
#Sixth row
negate_button.grid(row=5, column=0, pady=1, sticky='WE')
zero_button.grid(row=5, column=1, pady=1, sticky='WE')
decimal_button.grid(row=5, column=2, pady=1, sticky='WE')
equal_button.grid(row=5, column=3, pady=1, sticky='WE')





#Run the mainloop
root.mainloop()