#Weather forecast
from tkinter import *
import requests
from PIL import Image, ImageTk
from io import BytesIO

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
def search():
    """Use open weather api to look up current weather conditions given a city/ city, country"""
    global response

    #Get the api response
    #URL and my api key..... USE YOUR OWN API KEY!
    url = 'https://api.openweathermap.org/data/2.5/weather'
    api_key = '647e1da6fd960749e7f9faabec255ebc'

    #Search by the appropriate query, either city name or zip
    if search_method.get() == 1:
        querystring = {"q":city_entry.get(), "appid":api_key, 'units':'metric'}
    elif search_method.get() == 2:
        querystring = {"zip":city_entry.get(), "appid":api_key, 'units':'metric'}

    #Call API
    response = requests.request("GET", url, params=querystring)
    response = response.json()
    get_weather()
    get_icon()
    
    #Example response return
    '''{'coord': {'lon': 72.85, 'lat': 19.01}, 'weather': [{'id': 721, 'main': 'Haze', 'description': 'haze', 'icon': '50n'}], 
    'base': 'stations', 'main': {'temp': 300.15, 'feels_like': 302.66, 'temp_min': 300.15, 'temp_max': 300.15, 'pressure': 1012, 'humidity': 74}, 
    'visibility': 2500, 'wind': {'speed': 3.1, 'deg': 320}, 'clouds': {'all': 0}, 'dt': 1608214378, 
    'sys': {'type': 1, 'id': 9052, 'country': 'IN', 'sunrise': 1608168912, 'sunset': 1608208467}, 'timezone': 19800, 'id': 1275339, 'name': 'Mumbai', 'cod': 200}'''

def get_weather():
    """Grab information from API response and update our website labels"""
    #Gather the data to be used from the API response
    city_name = response['name']
    city_lat = str(response['coord']['lat'])
    city_lon = str(response['coord']['lon'])
    
    main_weather = response['weather'][0]['main']
    description = response['weather'][0]['description']

    temp = str(response['main']['temp'])
    feels_like = str(response['main']['feels_like'])
    temp_min = str(response['main']['temp_min'])
    temp_max = str(response['main']['temp_max'])
    humidity = str(response['main']['humidity'])

    #Update output labels
    city_info_label.config(text=city_name + "(" + city_lat + ", " + city_lon + ")", font=large_font, bg=output_color)
    weather_label.config(text="Weather: " + main_weather + ", " + description, font=small_font, bg=output_color)
    temp_label.config(text="Temperature: " + temp + " C", font=small_font, bg=output_color)
    feels_label.config(text="Feels Like: " + feels_like + " C", font=small_font, bg=output_color)
    temp_min_label.config(text="Min Temperature: " + temp_min + " C", font=small_font, bg=output_color)
    temp_max_label.config(text="Max Temperature: " + temp_max + " C", font=small_font, bg=output_color)
    humidity_label.config(text="Humidity: " + humidity, font=small_font, bg=output_color)

def get_icon():
    """Get the appropriate weather icon from API response"""
    global img

    #Get the icon id from API response.
    icon_id = response['weather'][0]['icon']

    #Get the icon from correct website
    url = 'http://openweathermap.org/img/wn/{icon}.png'.format(icon=icon_id)

    #Make a request at url to download the icon, stream=True automtically dl
    icon_response = requests.get(url, stream=True)

    #Turn into a form tkinter/python can use
    img_data = icon_response.content
    img = ImageTk.PhotoImage(Image.open(BytesIO(img_data)))

    #Update label
    photo_label.config(image=img)


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
city_info_label = Label(output_frame, bg=output_color)
weather_label = Label(output_frame, bg=output_color)
temp_label = Label(output_frame, bg=output_color)
feels_label = Label(output_frame, bg=output_color)
temp_min_label = Label(output_frame, bg=output_color)
temp_max_label = Label(output_frame, bg=output_color)
humidity_label = Label(output_frame, bg=output_color)
photo_label = Label(output_frame, bg=output_color)

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
submit_button = Button(input_frame, text='Submit', font=large_font, bg=input_color, command=search)

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