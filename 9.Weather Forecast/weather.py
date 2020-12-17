#Weather forecast
from tkinter import *

#Define window
root = Tk()
root.title('Weather Forecast')
root.iconbitmap('9.Weather Forecast/weather.ico')
root.geometry('400x400')
root.resizable(0,0)

#Define fonts and color
sky_color = '#76c3ef'
grass_color = '#aad207'
output_color = '#dcf0fb'
input_color = '#ecf2ae'
large_font = ('SimSun', 14)
small_font = ('SimSun', 10)

#Define functions

#Define layout
#create frames
sky_frame = Frame(root, bg=sky_color, height=250)
grass_frame = Frame(root, bg=grass_color)
sky_frame.pack(fill=BOTH, expand=True)
grass_frame.pack(fill=BOTH, expand=True)

output_frame = LabelFrame(sky_frame, bg=output_color, width=325, height=225)
input_frame = LabelFrame(grass_frame, bg=input_color, width=325)
output_frame.pack(pady=30)
output_frame.pack_propagate(0)
input_frame.pack(pady=15)

#output frame layout
city_info_label = Label(output_frame, bg=output_color, text='Testing')
weather_label = Label(output_frame, bg=output_color, text='Testing')
temp_label = Label(output_frame, bg=output_color, text='Testing')
feels_label = Label(output_frame, bg=output_color, text='Testing')
temp_min_label = Label(output_frame, bg=output_color, text='Testing')
temp_max_label = Label(output_frame, bg=output_color, text='Testing')
humidity_label = Label(output_frame, bg=output_color, text='Testing')
photo_label = Label(output_frame, bg=output_color, text='Testing')

city_info_label.pack(pady=8)
weather_label.pack()
temp_label.pack()
feels_label.pack()
temp_min_label.pack()
temp_max_label.pack()
humidity_label.pack()
photo_label.pack(pady=8)

#input frame layout
#Create input frame buttons and entry
city_entry = Entry(input_frame, width=20, font=large_font)
submit_button = Button(input_frame, text='Submit', font=large_font, bg=input_color)

search_method = IntVar()
search_method.set(1)
search_city = Radiobutton(input_frame, text='Search by city name', variable=search_method, value=1, font=small_font, bg=input_color)
search_zip = Radiobutton(input_frame, text='Search by zipcode', variable=search_method, value=2, font=small_font, bg=input_color)

city_entry.grid(row=0, column=0, padx=10, pady=(10,0))
submit_button.grid(row=0, column=1, padx=10, pady=(10,0))
search_city.grid(row=1, column=0, pady=2)
search_zip.grid(row=1, column=1, padx=5, pady=2)

#Run the root window mainloop
root.mainloop()