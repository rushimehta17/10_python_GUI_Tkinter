#Simon memory game
from tkinter import *

#Define window
root = Tk()
root.title('Simon Memory Game')
root.iconbitmap('7.Simon Memory Game/simon.ico')
root.geometry('400x400')
root.resizable(0,0)

#Define fonts and colors
game_font1 = ('Arial0', 12)
game_font2 = ('Arial', 8)
white = '#c6cbcd'
white_light = '#fbfcfc'
magenta = '#90189e'
magenta_light = '#f802f9'
cyan = '#078384'
cyan_light = '#00fafa'
yellow = '#9ba00f'
yellow_light = '#f7f801'
root_color = '#2eb4c6'
game_color = '#f6f7f8'
root.config(bg=root_color)

#Set global variable for the game
time = 500
score = 0
game_sequence = []
player_sequence = []

#Define functions

#Define Layout
#Define frame
info_frame = Frame(root, bg=root_color)
game_frame = LabelFrame(root, bg=game_color)
info_frame.pack(pady=(10,20))
game_frame.pack()

#Layout for the info frame
start_button = Button(info_frame, text="New Game", font=game_font1, bg=game_color)
score_label = Label(info_frame, text="Score: " + str(score), font=game_font1, bg=root_color)
start_button.grid(row=0, column=0, padx=20, ipadx=30)
score_label.grid(row=0, column=1)

#Layout for the game frame
#Make the game buttons
white_button = Button(game_frame, bg=white, activebackground=white_light, borderwidth=3)
magenta_button = Button(game_frame, bg=magenta, activebackground=magenta_light, borderwidth=3)
cyan_button = Button(game_frame, bg=cyan, activebackground=cyan_light, borderwidth=3)
yellow_button = Button(game_frame, bg=yellow, activebackground=yellow_light, borderwidth=3)

white_button.grid(row=0, column=0, columnspan=2, padx=10, pady=10, ipadx=60, ipady=50)
magenta_button.grid(row=0, column=2, columnspan=2, padx=10, pady=10, ipadx=60, ipady=50)
cyan_button.grid(row=1, column=0, columnspan=2, padx=10, pady=10, ipadx=60, ipady=50)
yellow_button.grid(row=1, column=2, columnspan=2, padx=10, pady=10, ipadx=60, ipady=50)

#Make radio button for difficulty
difficulty = StringVar()
difficulty.set('Medium')
Label(game_frame, text="Difficulty", font=game_font2, bg=game_color).grid(row=2, column=0)
Radiobutton(game_frame, text='Easy', variable=difficulty, value='Easy', font=game_font2, bg=game_color).grid(row=2, column=1)
Radiobutton(game_frame, text='Medium', variable=difficulty, value='Medium', font=game_font2, bg=game_color).grid(row=2, column=2)
Radiobutton(game_frame, text='Hard', variable=difficulty, value='Hard', font=game_font2, bg=game_color).grid(row=2, column=3)
#Run the root mainloop
root.mainloop()