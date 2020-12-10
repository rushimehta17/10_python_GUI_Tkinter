#Notepad
#icon http://www.doublejdesign.co.uk
from tkinter import *
from PIL import ImageTk, Image
from tkinter import scrolledtext, messagebox

#Define window
root = Tk()
root.title('Notepad')
root.iconbitmap('4.notepad/pad.ico')
root.geometry('600x600')
root.resizable(0,0)

#Define fonts and colors
text_color = '#fffacd'
menu_color = '#dad9da'
root_color = '#6c809a'
root.config(bg=root_color)

#Define functions
def change_font(event):
    """Change the given font based off dropbox option"""
    if font_option.get() == 'none':
        my_font = (font_family.get(), font_size.get())
    else:
        my_font = (font_family.get(), font_size.get(), font_option.get())

    #change the font style
    input_text.config(font=my_font)

def new_note():
    """Create a new note which essentially clears the screen"""
    #Use a messagebox to ask for a new note
    question = messagebox.askyesno("New Note", "Are you sure you want to start a new note?")
    if question == 1:
        #ScrolledText widgets starting index is 1.0 not 0.
        input_text.delete("1.0", END)

def close_note():
    """Closes the note which essentially quits the program"""
    #Use messagebox to ask the question
    question = messagebox.askyesno("Close Note", "Are you sure you want to close the note?")
    if question == 1:
        root.destroy()


#define the layout
#Define frames
menu_frame = Frame(root, bg=menu_color)
text_frame = Frame(root, bg=text_color)
menu_frame.pack(padx=5, pady=5)
text_frame.pack(padx=5, pady=5)

#Layout for the menu
#Create the menu: new, open, save, close, font family, font size, font option
new_image = ImageTk.PhotoImage(Image.open('4.notepad/new.png'))
new_button = Button(menu_frame, image=new_image, command=new_note)
new_button.grid(row=0, column=0, padx=5, pady=5)

open_image = ImageTk.PhotoImage(Image.open('4.notepad/open.png'))
open_button = Button(menu_frame, image=open_image)
open_button.grid(row=0, column=1, padx=5, pady=5)

save_image = ImageTk.PhotoImage(Image.open('4.notepad/save.png'))
save_button = Button(menu_frame, image=save_image)
save_button.grid(row=0, column=2, padx=5, pady=5)

close_image = ImageTk.PhotoImage(Image.open('4.notepad/close.png'))
close_button = Button(menu_frame, image=close_image, command=close_note)
close_button.grid(row=0, column=3, padx=5, pady=5)

#Create a list of fonts to use
families = ['Terminal', 'Modern', 'Script', 'Courier', 'Arial', 'Calibri', 'Cambria', 'Georgia', 'MS Gothic', 'SimSun', 'Tahoma', 'Times New Roman', 'Verdana', 'Wingdings']
font_family = StringVar()
font_family_drop = OptionMenu(menu_frame, font_family, *families, command=change_font)
font_family.set('Terminal')
#Set the width so it will fit "times new roman" and remain constant 
font_family_drop.config(width=16)
font_family_drop.grid(row=0, column=4, padx=5, pady=5)

sizes = [8, 10, 12, 14, 16, 20, 24, 32, 48, 64, 72, 96]
font_size = IntVar()
font_size_drop = OptionMenu(menu_frame, font_size, *sizes, command=change_font)
font_size.set(12)
#Set width to be constant
font_size_drop.config(width=2)
font_size_drop.grid(row=0, column=5, padx=5, pady=5)

option = ['none', 'bold', 'italic']
font_option = StringVar()
font_option_drop = OptionMenu(menu_frame, font_option, *option, command=change_font)
font_option.set('none')
font_option_drop.config(width=5)
font_option_drop.grid(row=0, column=6,padx=5, pady=5)


#Layout for the text frame
my_font = (font_family.get(), font_size.get())
#Create the input_text as a scrolltext so you can scroll through the text
#Set default width and height to be more than the window size so that on the smallest text size, the field size is constant
input_text = scrolledtext.ScrolledText(text_frame, bg=text_color, width=100, height=100, font=my_font)
input_text.pack()
#Run the root mainloop
root.mainloop()