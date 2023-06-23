from tkinter import *
from tkinter import filedialog
import pygame.mixer as mixer      # install pip py game for graphics and library sounds
import os

# Initializing the mixer
mixer.init()

# Play, Stop, Load, Pause, Resume and LoadDirectory functions
def play_song(song_name, songs_list, status):
    song_name.set(songs_list.get(ACTIVE))

    mixer.music.load(songs_list.get(ACTIVE))
    mixer.music.play()

    status.set("Now Playing")

def stop_song(status):
    mixer.music.stop()
    status.set("Stopped")

def load(listbox):
    os.chdir(filedialog.askdirectory(title='Open a Music Directory'))

    tracks = os.listdir()

    for track in tracks:
        listbox.insert(END, track)

def pause_song(status):
    mixer.music.pause()
    status.set("Paused")

def resume_song(status):
    mixer.music.unpause()
    status.set("Resumed")

# GUI Created
root = Tk()
root.geometry('700x220')
root.title(' Cherry Music Player')
root.resizable(0, 0)
root.configure(background='lightgray')

# All the frames
song_frame = LabelFrame(root, text='Current Song', bg='lightgray', width=400, height=80)
song_frame.place(x=0, y=0)

button_frame = LabelFrame(root, text='Control Buttons', bg='lightgray', width=400, height=120)
button_frame.place(y=80)

listbox_frame = LabelFrame(root, text='Playlist', bg='lightgray')
listbox_frame.place(x=400, y=0, height=200, width=300)

# All StringVar variables
current_song = StringVar(root, value='Not selected')
song_status = StringVar(root, value='')

# Playlist ListBox
playlist = Listbox(listbox_frame, font=('Arial', 11), selectbackground='sky blue')

scroll_bar = Scrollbar(listbox_frame, orient=VERTICAL)
scroll_bar.pack(side=RIGHT, fill=BOTH)

playlist.config(yscrollcommand=scroll_bar.set)
scroll_bar.config(command=playlist.yview)
playlist.pack(fill=BOTH, padx=5, pady=5)

# SongFrame Labels
Label(song_frame, text='CURRENTLY PLAYING:', bg='lightgray', font=('Sans Serif', 10, 'bold')).place(x=5, y=20)

song_lbl = Label(song_frame, textvariable=current_song, bg='light yellow', font=("Sans Serif", 16), width=25)
song_lbl.place(x=150, y=20)

# Buttons in the main screen
pause_button = Button(button_frame, text='Pause', bg='sky blue', font=("Sans Serif", 16), width=8,
                   command=lambda: pause_song(song_status))
pause_button.place(x=18, y=10)

stop_button = Button(button_frame, text='Stop', bg='sky blue', font=("Sans Serif", 16), width=8,
                  command=lambda: stop_song(song_status))
stop_button.place(x=105, y=10)

play_button = Button(button_frame, text='Play', bg='sky blue', font=("Sans Serif", 16), width=8,
                  command=lambda: play_song(current_song, playlist, song_status))
play_button.place(x=193, y=10)

resume_button = Button(button_frame, text='Resume', bg='sky blue', font=("Sans Serif", 16), width=8,
                    command=lambda: resume_song(song_status))
resume_button.place(x=294, y=10)

load_button = Button(button_frame, text='Load Directory', bg='sky blue', font=("Sans Serif", 16), width=39,
                  command=lambda: load(playlist))
load_button.place(x=10, y=55)

Label(root, textvariable=song_status, bg='light blue', font=('Arial', 10), justify=LEFT).pack(side=BOTTOM, fill=X)

# GUI Finalisation
root.mainloop()
