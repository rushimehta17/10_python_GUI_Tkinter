#Morse code translator
#Icon found from http://icons8.com
from tkinter import *
from playsound import playsound

#Define window
root = Tk()
root.title("Morse Code Translator")
root.iconbitmap('6.Morse Code Translator/morse.ico')
root.geometry('500x350')
root.resizable(0,0)

#Define fonts and colors
button_font = ('SimSun', 10)
root_color = '#778899'
frame_color = '#dcdcdc'
button_color = '#c0c0c0'
text_color = '#f8f8ff'
root.config(bg=root_color)

#Define functions
def convert():
    """Call the appropriate conversion function based off radio button value"""
    #English to morse code:
    if language.get() == 1:
        get_morse()
    elif language.get() == 2:
        get_english()

def get_morse():
    """Convert an english message to morse code"""
    #String to hold morse code message
    morse_code = ""

    #Get the input text and standardize it to lower case
    text = input_text.get("1.0", END)
    text = text.lower()

    #remove any letters of symbols not in our dict keys
    for letter in text:
        if letter not in english_to_morse.keys():
            text = text.replace(letter, '')
    
    #Break up into individual words based in space " " andput into a list
    word_list = text.split(" ")

    #Turn each individual word in word_list into a list of letters
    for word in word_list:
        letters = list(word)
        #For each letter, get the morse coderepresentation and append it to the string morse_code
        for letter in letters:
            morse_char = english_to_morse[letter]
            morse_code += morse_char
            #seperate individual letters with a space
            morse_code += " "
        #Seperate individual words with a |
        morse_code += "|"

    output_text.insert("1.0", morse_code)


def get_english():
    """Convert a morse code message to english"""
    #String to hold english message
    english = ""

    #Get the input text
    text = input_text.get("1.0", END)

    #Remove any letters or symbols not in out dict keys
    for letter in text:
        if letter not in morse_to_english.keys():
            text = text.replace(letter, '')

    #Break up each word based on | and put into a list
    word_list = text.split("|")

    #Turn each word into a list of letters
    for word in word_list:
        letters = word.split(" ")
        #For each letter, get the english representation and add it to the string in english
        for letter in letters:
            english_char = morse_to_english[letter]
            english += english_char
        #Seperate individual words with a space
        english += " "
    
    output_text.insert("1.0", english)

def clear():
    """Clear both text fields"""
    input_text.delete("1.0", END)
    output_text.delete("1.0", END)

def play():
    """Play tones for corresponding dots and dash"""
    #Determine where the morse code is
    if language.get() == 1:
        text = output_text.get("1.0", END)
    elif language.get() == 2:
        text = input_text.get("1.0", END)

    #Play the tones (., -, " ", |)
    for value in text:
        if value == ".":
            playsound('6.Morse Code Translator/dot.mp3')
            root.after(100)
        elif value == "-":
            playsound('6.Morse Code Translator/dash.mp3')
            root.after(200)
        elif value == " ":
            root.after(300)
        elif value == "|":
            root.after(700)


#Create our morse code dictionaries
english_to_morse = {'a': '.-', 'b': '-...', 'c': '-.-.', 'd': '-..',
                    'e': '.', 'f': '..-.', 'g': '--.', 'h': '....',
                    'i': '..', 'j': '.---', 'k': '-.-', 'l': '.-..',
                    'm': '--', 'n': '-.', 'o': '---', 'p': '.--.',
                    'q': '--.-', 'r': '.-.', 's': '...', 't': '-',
                    'u': '..--', 'v': '...-', 'w': '.--', 'x': '-..-',
                    'y': '-.--', 'z': '--..', '1': '.----',
                    '2': '..---', '3': '...--', '4': '....-', '5': '.....',
                    '6': '-....', '7': '--...', '8': '---..', '9': '----.',
                     '0': '-----', ' ':' ', '|':'|', "":"" }

morse_to_english = dict([(value, key) for key, value in english_to_morse.items()])

#Define layout
#Create frames
input_frame = LabelFrame(root, bg=frame_color)
output_frame = LabelFrame(root, bg=frame_color)
input_frame.pack(padx=16, pady=(16,8))
output_frame.pack(padx=16, pady=(8,16))

#Layout for the input frame
input_text = Text(input_frame, height=8, width=30, bg=text_color)
input_text.grid(row=0, column=1, rowspan=3, padx=5, pady=5)

language = IntVar()
language.set(1)
morse_button = Radiobutton(input_frame, text="English --> Morse Code", variable=language, value=1, font=button_font, bg=frame_color)
english_button = Radiobutton(input_frame, text="Morse Code --> English", variable=language, value=2, font=button_font, bg=frame_color)
guide_button = Button(input_frame, text="Guide", font=button_font, bg=button_color)

morse_button.grid(row=0, column=0, pady=(15,0))
english_button.grid(row=1, column=0)
guide_button.grid(row=2, column=0, sticky="WE", padx=10)

#Layout for the output frame
output_text = Text(output_frame, height=8, width=30, bg=text_color)
output_text.grid(row=0, column=1, rowspan=4, padx=5, pady=5)

convert_button = Button(output_frame, text="Convert", font=button_font, bg=button_color, command=convert)
play_morse = Button(output_frame, text="Play Morse", font=button_font, bg=button_color, command=play)
clear_button = Button(output_frame, text="Clear", font=button_font, bg=button_color, command=clear)
quit_button = Button(output_frame, text="Quit", font=button_font, bg=button_color, command=root.destroy)
convert_button.grid(row=0, column=0, padx=10, ipadx=50) #convert ipadx defines column width
play_morse.grid(row=1, column=0, padx=10, sticky='WE')
clear_button.grid(row=2, column=0, padx=10, sticky='WE')
quit_button.grid(row=3, column=0, padx=10, sticky='WE')

#Run the root window's mainloop
root.mainloop()