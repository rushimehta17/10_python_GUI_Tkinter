# Astronomy Picture Of the Day
from tkinter import *
from tkinter import filedialog
import requests, webbrowser
from tkcalendar import DateEntry
from PIL import ImageTk, Image
from io import BytesIO

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
def get_requests():
    """Get request data from NASA APOD API"""
    global response

    #Set the parameters fot the request
    url = "https://api.nasa.gov/planetary/apod"
    api_key = "DEMO_KEY" #Use your own key
    date = calender.get_date()

    querystring = {'api_key':api_key, 'date':date}

    #Call the request and turn it into a python usable format
    response = requests.request("GET", url, params=querystring)
    response = response.json()

    #Update output label
    set_info()

def set_info():
    """Update output labels based on API call"""
    #Example response
    '''{'copyright': 'Thomas Ashcraft', 'date': '2021-01-04', 'explanation': 'What causes sprite lightning? Mysterious bursts of light in the sky that momentarily resemble gigantic jellyfish have been recorded for over 30 years, but apart from a general association with positive cloud-to-ground lightning, their root cause remains unknown. Some thunderstorms have them -- most don\'t.  Recently, however, high speed videos are better detailing how sprites actually develop.  The featured video, captured in mid-2019, is fast enough -- 
        at about 100,000 frames per second -- to time-resolve several sprite "bombs" dropping and developing into the multi-pronged streamers that appear on still images. Unfortunately, the visual clues provided by videos like these do not fully resolve the sprite origins mystery. High speed vidoes do indicate to some researchers, though, that sprites are more likely to occur when plasma irregularities exist in the 
upper atmosphere.    Astrophysicists: Browse 2,300+ codes in the Astrophysics Source Code Library', 'media_type': 'video', 'service_version': 'v1', 'title': 'Sprite Lightning at 100,000 Frames Per Second', 'url': 'https://www.youtube.com/embed/zS_XgF9i8tc?rel=0'}'''

    #Update the picture date and explanation
    picture_date.config(text=response['date'])
    picture_explanation.config(text=response['explanation'])

    #We need to use 3 images in other functions; an img, a thumb, and a full_img
    global img
    global thumb
    global full_img

    url = response['url']

    if response['media_type'] == 'image':
        #Grab the photo that is stored in our response.
        img_response = requests.get(url, stream=True)

        #Get the content of response and use BytesIO to open it as an image
        #Keep a reference to this img as this is what we can use to save the image (Image nit PhotoImage)
        #Create the full screen image for a second window
        img_data = img_response.content
        img = Image.open(BytesIO(img_data))

        full_img = ImageTk.PhotoImage(img)

        #Create the thumbnail for the main screen
        thumb_date = img_response.content
        thumb = Image.open(BytesIO(thumb_date))
        thumb.thumbnail((200,200))
        thumb = ImageTk.PhotoImage(thumb)

        #Set the thumbnail image
        picture_label.config(image=thumb)
    elif response['media_type'] == 'video':
        picture_label.config(text=url, image='')
        webbrowser.open(url)

def full_photo():
    """Open the full size photo in a new window"""
    top = Toplevel()
    top.title("Full APOD Photo")
    top.iconbitmap('10.APOD Viewer/rocket.ico')

    #Load the full image to the top image
    img_label = Label(top, image=full_img)
    img_label.pack()

def save_photo():
    """Save the desired photo"""
    save_name = filedialog.asksaveasfilename(initialdir="10.APOD Viewer/", title="Save Image", filetype=(("JPEG", "*.jpg"), ("All Files", "*.*")))
    img.save(save_name + ".jpg")

#Define layout
#Create frames
input_frame = Frame(root, bg=nasa_blue)
output_frame = Frame(root, bg=nasa_white)
input_frame.pack()
output_frame.pack(padx=50, pady=(0,25))

#Layout for the input frame
calender = DateEntry(input_frame, width=10, font=text_font, background=nasa_blue, foreground=nasa_white)
submit_button = Button(input_frame, text="Submit", font=text_font, bg=nasa_light_blue, command=get_requests)
full_button = Button(input_frame, text="Full Photo", font=text_font, bg=nasa_light_blue, command=full_photo)
save_button = Button(input_frame, text="Save Photo", font=text_font, bg=nasa_light_blue, command=save_photo)
quit_button = Button(input_frame, text="Exit", font=text_font, bg=nasa_red, command=root.destroy)

calender.grid(row=0, column=0, padx=5, pady=10)
submit_button.grid(row=0, column=1, padx=5, pady=10, ipadx=35)
full_button.grid(row=0, column=2, padx=5, pady=10, ipadx=25)
save_button.grid(row=0, column=3, padx=5, pady=10, ipadx=25)
quit_button.grid(row=0, column=4, padx=5, pady=10, ipadx=50)

#Layout for the output frame
picture_date = Label(output_frame, font=text_font, bg=nasa_white)
picture_explanation = Label(output_frame, font=text_font, bg=nasa_white, wraplength=600)
picture_label = Label(output_frame,)

picture_date.grid(row=1, column=1, padx=10)
picture_explanation.grid(row=0, column=0, padx=10, pady=10, rowspan=2)
picture_label.grid(row=0, column=1, padx=10, pady=10)

#Get today's photo to start with
get_requests()

#Run the root mainloop
root.mainloop()