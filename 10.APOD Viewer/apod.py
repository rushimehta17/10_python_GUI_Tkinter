# Astronomy Picture Of the Day
from tkinter import *
from tkcalendar import DateEntry

#Define window
root = Tk()
root.title("Apod Viewer")
root.iconbitmap('10.APOD Viewer/rocket.ico')

#Define fonts and colors
text_font = ("Times New Roman", 14)
nasa_blue = "#043c93"
nasa_light_blue = "#7aa5d3"
nasa_red = "#ff1923"
nasa_white = "#ffffff"
root.config(bg=nasa_blue)

#Define functions

#Define layout
#Create frames
input_frame = Frame(root, bg=nasa_blue)
output_frame = Frame(root, bg=nasa_white)
input_frame.pack()
output_frame.pack(padx=50, pady=(0,25))

#Layout for the input frame
calender = DateEntry(input_frame, width=10, font=text_font, background=nasa_blue, foreground=nasa_white)
submit_button = Button(input_frame, text="Submit", font=text_font, bg=nasa_light_blue)
full_button = Button(input_frame, text="Full Photo", font=text_font, bg=nasa_light_blue)
save_button = Button(input_frame, text="Save Photo", font=text_font, bg=nasa_light_blue)
quit_button = Button(input_frame, text="Exit", font=text_font, bg=nasa_red, command=root.destroy)

calender.grid(row=0, column=0, padx=5, pady=10)
submit_button.grid(row=0, column=1, padx=5, pady=10, ipadx=35)
full_button.grid(row=0, column=2, padx=5, pady=10, ipadx=25)
save_button.grid(row=0, column=3, padx=5, pady=10, ipadx=25)
quit_button.grid(row=0, column=4, padx=5, pady=10, ipadx=50)

#Layout for the output frame
picture_date = Label(output_frame, text="Testing")
picture_explanation = Label(output_frame, text="Testing")
picture_label = Label(output_frame, text="Testing")

picture_date.grid()
picture_explanation.grid()
picture_label.grid()
#Run the root mainloop
root.mainloop()
